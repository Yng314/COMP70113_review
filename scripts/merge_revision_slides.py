#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable

from PyPDF2 import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class PageSpec:
    source_label: str
    path: Path
    pdf_page: int


@dataclass
class PageEntry:
    spec: PageSpec
    title: str
    text_norm: str
    duplicate_of: str | None = None


def parse_page_list(raw: str) -> list[int]:
    pages: list[int] = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_raw, end_raw = part.split("-", 1)
            start = int(start_raw)
            end = int(end_raw)
            if end < start:
                raise ValueError(f"invalid range: {part}")
            pages.extend(range(start, end + 1))
        else:
            pages.append(int(part))
    return pages


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return re.sub(r"_+", "_", value).strip("_")


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9 ]+", "", text)
    return text.strip()


def build_title(text: str, fallback: str) -> str:
    text = " ".join(text.split())
    if not text:
        return fallback
    title = text[:96].strip()
    return title if len(text) <= 96 else f"{title}..."


def cross_file_similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a[:1600], b[:1600]).ratio()


def load_entries(specs: Iterable[PageSpec], near_duplicate_threshold: float) -> tuple[list[PageEntry], list[PageEntry]]:
    readers: dict[Path, PdfReader] = {}
    main_entries: list[PageEntry] = []
    duplicate_entries: list[PageEntry] = []

    for spec in specs:
        reader = readers.setdefault(spec.path, PdfReader(str(spec.path)))
        page = reader.pages[spec.pdf_page - 1]
        text = page.extract_text() or ""
        norm = normalize_text(text)
        entry = PageEntry(
            spec=spec,
            title=build_title(text, f"{spec.source_label} p.{spec.pdf_page}"),
            text_norm=norm,
        )

        matched: PageEntry | None = None
        for previous in main_entries:
            if previous.spec.path == entry.spec.path:
                continue
            if entry.text_norm and entry.text_norm == previous.text_norm:
                matched = previous
                break
            if len(entry.text_norm) >= 80 and len(previous.text_norm) >= 80:
                if cross_file_similarity(entry.text_norm, previous.text_norm) >= near_duplicate_threshold:
                    matched = previous
                    break

        if matched is not None:
            entry.duplicate_of = (
                f"{matched.spec.source_label} p.{matched.spec.pdf_page}"
            )
            duplicate_entries.append(entry)
        else:
            main_entries.append(entry)

    return main_entries, duplicate_entries


def add_pages(
    writer: PdfWriter,
    entries: Iterable[PageEntry],
    parent_outline,
) -> None:
    readers: dict[Path, PdfReader] = {}
    for entry in entries:
        reader = readers.setdefault(entry.spec.path, PdfReader(str(entry.spec.path)))
        writer.add_page(reader.pages[entry.spec.pdf_page - 1])
        page_index = len(writer.pages) - 1
        label = f"{entry.spec.source_label} p.{entry.spec.pdf_page} - {entry.title}"
        if entry.duplicate_of:
            label = f"[重复] {label} (首现: {entry.duplicate_of})"
        writer.add_outline_item(label, page_index, parent=parent_outline)


def parse_spec_args(items: list[str]) -> list[PageSpec]:
    specs: list[PageSpec] = []
    for item in items:
        label, rel_path, page_expr = item.split("::", 2)
        path = (ROOT / rel_path).resolve()
        for page in parse_page_list(page_expr):
            specs.append(PageSpec(label, path, page))
    return specs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument(
        "--spec",
        action="append",
        required=True,
        help="LABEL::relative/path.pdf::1-3,7,9-10",
    )
    parser.add_argument("--near-duplicate-threshold", type=float, default=0.92)
    args = parser.parse_args()

    specs = parse_spec_args(args.spec)
    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    main_entries, duplicate_entries = load_entries(specs, args.near_duplicate_threshold)

    writer = PdfWriter()
    root_outline = writer.add_outline_item(args.title, 0)
    main_outline = writer.add_outline_item("Main Sequence", 0, parent=root_outline)
    add_pages(writer, main_entries, main_outline)

    if duplicate_entries:
        duplicate_start = len(writer.pages)
        duplicate_outline = writer.add_outline_item("重复页", duplicate_start, parent=root_outline)
        add_pages(writer, duplicate_entries, duplicate_outline)

    with output_path.open("wb") as handle:
        writer.write(handle)

    print(f"OUTPUT={output_path}")
    print(f"MAIN_COUNT={len(main_entries)}")
    print(f"DUPLICATE_COUNT={len(duplicate_entries)}")
    for entry in duplicate_entries:
        print(
            f"DUPLICATE={entry.spec.source_label} p.{entry.spec.pdf_page} -> {entry.duplicate_of}"
        )


if __name__ == "__main__":
    main()
