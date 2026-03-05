# Generative AI（70113）复习计划（3/5–3/18）

> 说明：下表页码均指 **PDF 页码**（从 1 开始，按 PDF 阅读器显示的页数）。老师提到的“约 20% 来自之前课程 slides”的部分，我把对应 lecture PDF 的关键页码也一起补进了表格的参考列里（用缩写标注），并基于你重传的 OCR 版本做过二次校对。

## Slides 索引（同一目录下的 PDF + 路径）

所有文件都在：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/`

- EP（Exam Prep 总纲 + 例题/推导）：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/Generative_AI_-_Exam_Preparation-2.pdf`
- Text（Text Generation 讲义）：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/(0) Text Generation.pdf`
- Audio（Audio Generation 讲义）：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/(0) Audio Generation.pdf`
- 3D（3D Generation 讲义）：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/(0) 3D Generation.pdf`
- Video（Video Generation 讲义）：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/(0) Video Generation.pdf`
- VAE/GAN（Image Generation: VAE & GAN 讲义）：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/(0) Image Generation (VAE and GAN).pdf`
- Diffusion（Image Generation: Diffusion 讲义）：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/(0) Image Generation (Diffusion).pdf`
- Intro（课程介绍/Generative Modeling & KL 示例）：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/(0) Generative AI - Introduction.pdf`
- Prelim（Softmax/CNN/Token/Attention 预备知识）：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/(1) Generative AI - Preliminary.pdf`
- Transcript（老师 exam prep 口头说明转写）：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/review_transcript.txt`

## 复习计划（Markdown 表格）

> Transcript 补充边界：老师明确说课堂里介绍过的很多 research paper 细节不是考试重点；复习以课程核心概念、公式、推导骨架和题型节奏为主。

| 日期 | 重点（按考试分布） | 当天内容 | Slides（PDF页码，含课程 slides 补充） | 考试要求/不要求（来自 transcript） | 产出/练习 |
|---|---|---|---|---|---|
| 3/5 | Q1-Text + 考试节奏 | 考试结构/配速；tokenization、teacher forcing、KV cache | EP: 2–5, 29–44（重点34–41、42–44）；Text: 11, 25–28, 37–39, 55–60；Prelim: 56–58 | 要求：Q1 共20题，10–20分钟完成，重点看 tokenization 公式和概念；不要求：在单题上久耗，卡住先留空二刷。 | 做“Q1-Text要点+易错点”1页；teacher forcing 单独补一张概念卡 |
| 3/6 | Q1-Audio | waveform、spectrogram、voice cloning、quantization | EP: 83–87；Audio: 5–7, 24–25, 33–37, 40–41, 61–62 | 要求：理解 waveform vs spectrogram、voice cloning 的 speaker embedding 思路；不要求：实现/工程细节。 | 整理“单选陷阱点”清单（≥10条） |
| 3/7 | Q1-3D + Q1-Video | SDF、NeRF、Gaussian splatting、SDS；optical flow、temporal consistency、latent ops | EP: 88–97, 98–100；3D: 9–47, 88–101；Video: 27–28, 30–36, 73–75, 88 | 要求：概念区分题（NeRF vs 3DGS、SDF/SDS、optical flow/temporal consistency）；不要求：论文级复杂推导。 | Q1计时自测：20题=15–20min；错因归类 |
| 3/8 | Q2-Softmax（15%） | softmax + cross-entropy loss 与梯度手推 | EP: 16–24；Prelim: 6–21 | 要求：会写 CE loss 和最终梯度结论 `p - y`；不要求：考试里完整重推复杂反传（老师明确说别花5分钟证明）。 | 计时手算小题（每题≤3min）≥5题 |
| 3/9 | Q2-CNN（20%） | 输出尺寸、参数量、receptive field | EP: 25–28；Prelim: 45–55 | 要求：filter size/参数量/感受野计算（浅层可枚举）；不要求：超深网络复杂变体细节。 | 公式卡：尺寸/参数/感受野模板各1份 |
| 3/10 | Q2-Transformer&Attn（55%）(1/2) | LM类型；BERT vs GPT；scaled dot-product attention、复杂度、causal；ViT | EP: 29–33, 38–40；Text: 3–7, 14–18, 33–36；Video: 41–42（ViT 相关） | 要求：BERT/T5/GPT 训练目标区别、为何除以 `sqrt(d_k)`、causal masking；不要求：背过多架构 trivia。 | 写出 attention 公式+复杂度+BERT/GPT 区别（可背诵版） |
| 3/11 | Q2-Transformer&Attn（55%）(2/2) + LoRA（10%） | KV-cache；AR学习框架；LoRA参数效率/秩 | EP: 41–46；Text: 37–40（KV cache/efficient attention）, 56–60（AR/teacher forcing）, 74–81（LoRA） | 要求：KV cache 缓存 K/V 不缓存 Q；teacher forcing 训练逻辑；LoRA 的 rank/参数量与初始化（A 高斯、B=0）；不要求：RLHF/项目案例扩展细节。 | Q2混合计时：10题（每题≤3min）+错题清单 |
| 3/12 | Q3-KL（30%） | KL定义/性质；Gaussian相关计算/推导要点 | EP: 8–13, 74–80；Intro: 24–29；Diffusion: 33–41 | 要求：KL 非对称、非负、参考分布方向；会写表达式和高斯相关计算；不要求：`log` 数值近似（老师明确说不要数值算 log）。 | “KL/Gaussian KL最终公式+符号表”1页 |
| 3/13 | Q3-VAE（20%） | VAE结构；reparameterization trick | EP: 47–55；VAE/GAN: 28–36（选看 Diffusion: 7–13） | 要求：为什么真后验难算、`q_phi(z given x)` 近似、encoder 输出 `mu/sigma`；不要求：完整 ELBO 长推导（放到 3/14 练）。 | 写出 VAE 解题骨架（intractable posterior -> variational approximation -> reparameterization）+2道短题 |
| 3/14 | Q3-ELBO（20%）+ GAN（20%） | ELBO推导骨架；GAN minimax/角色 | EP: 56–65, 66–68；VAE/GAN: 37–46（ELBO）, 59–62（GAN objective）（选看 Diffusion: 9–18） | 要求：ELBO 三项含义与“下界”逻辑、GAN 的 min-max 角色；不要求：过长证明细枝末节。 | ELBO压缩到3–5行；GAN目标式写对（自检符号） |
| 3/15 | Q3-Diffusion（30%） | forward Markov链；T-step闭式；reverse/latent diffusion；Generative Trilemma | EP: 69–82, 100；Diffusion: 15–45, 53–60, 71–78（latent diffusion）（选看 Video: 55–63） | 要求：forward transition 与 forward jump（两步到一般步）推导主线；latent diffusion 和 trilemma 结论；不要求：论文系统实现细节。 | 计时推导/写结论：`q(x_t given x_0)` 等关键式重复练 |
| 3/16 | 汇总(1/3) | A4终稿（公式+推导骨架+易错点）；按权重二刷Attn/KL/Diffusion | EP: 38–46, 8–13, 69–82；Text: 84–86（recap）；VAE/GAN: 91–100（recap）；Diffusion: 3（Trilemma）, 71–78 | 要求：A4 只放“可直接写上答卷”的公式与骨架；不要求：塞入研究论文细节。 | A4可带页完成；补最弱2块 |
| 3/17 | 汇总(2/3) | 全真90min模拟（严格配速：Q1 15–20min；卡题>2min跳过留空二刷） | EP: 全部；按错题回看对应课程 PDF | 要求：按真实节奏做题（先顺序做完，再二刷留空题）；不要求：死磕个别难题。 | 模拟卷复盘：错题清单→对应页码回补 |
| 3/18 | 汇总(3/3) | 查漏补缺+轻量回忆（只看错题/A4/易错点） | 按错题定位（优先 EP + 各 PDF recap 页） | 要求：保持手感与答题速度；不要求：新开大块陌生内容。 | 小计时：Q1一轮 + Q2/Q3各3题，稳节奏 |
