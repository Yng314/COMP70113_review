# 3/5 Q1-Text Generation 复习汇总（可直接背）

## 1. 范围 Double Check（按老师口径）

### 来自 `REVISION_PLAN.md`
- 3/5 Q1-Text 范围：`tokenization`、`teacher forcing`、`KV cache`
- 对应页码：
  - EP：2-5，29-43（重点 34-41，42-43）
  - Text：11，25-28，37-39，50-56
  - Prelim：56-58

### 来自 `review_transcript.txt`
- 明确提到 Text 部分重点是：`tokenization`、`KV caching`、`teacher forcing`
- 明确提到 tokenization 三类对比会出题
- 明确提到 KV cache 考点是“缓存 K/V，不缓存 Q”
- 明确提到 teacher forcing 是训练稳定关键概念

### 结论
- Q1-Text 的主标签是 3 个：`tokenization`、`teacher forcing`、`KV cache`
- `causal attention` 和 `autoregressive` 是这 3 个标签的支撑机制，属于会被问到的上下文考点
- 不需要展开论文实现细节或工程优化细节

## 2. Q1-Text 要点（考试表达版）

### A. Tokenization
- `token` 不等于“一个完整单词”；可为词、子词或字符片段
- `token id` 是离散索引；`embedding` 是查表得到的连续向量
- 三类 tokenization：
  - word-level：直观，但 OOV 明显，词表做大成本高
  - character-level：OOV 少，但序列变长、计算更重、语义组合更难学
  - subword-level：在词表规模、序列长度、OOV 风险之间折中

### B. Attention / Causal / AR（支撑点）
- 注意力核心式：`softmax(QK^T / sqrt(d_k))V`
- 除 `sqrt(d_k)`：防止点积过大导致 softmax 过饱和，缓解梯度过小，稳定训练
- causal mask：屏蔽未来位置信息（在 `score[i,j]` 定义下屏蔽上三角），保证只能看 `j <= i`
- autoregressive 分解：`P(x) = Π_t P(x_t | x_<t)`

### C. KV Cache
- 缓存历史 token 的 `K/V`，不缓存 `Q`
- 解码时只对当前步新 token 计算新的 `Q`（以及当前步 `K/V` 后追加）
- 核心收益：避免每步重算整段历史的 K/V，做增量解码
- 主要代价：cache 显存随上下文长度增长

### D. Teacher Forcing
- 训练时：每步使用真实前缀 token 作为条件预测下一 token
- 推理时：没有真值前缀，只能喂模型上一步输出（self-feeding）
- 作用：稳定条件分布学习，减小错误前缀对后续训练的污染
- 现象：推理阶段可能出现误差累积（exposure bias）

## 3. 高频易错点清单
- 把 token 误当成“必然一个单词”
- 把 `token id` 和 `embedding` 混为一谈
- 把 causal mask 和 BERT 的 `[MASK]` 任务混为一谈
- 说 KV cache 缓存 `Q/K/V`（正确是历史 `K/V`）
- 说 KV cache 把复杂度直接变成 `O(1)`（不准确，关键是减少重复全量重算）
- 把 teacher forcing 当推理技巧（它是训练技巧）
- 把“模型输出一个词”说成模型直接输出确定词（先输出分布，再解码选词）

## 4. Teacher Forcing 概念卡（单独背诵）

### 定义
训练时，每个位置都用真实前一个 token 作为条件，预测当前 token。

### 目标
稳定学习 `p(x_t | x_<t)`，减少错误前缀传播对训练的干扰。

### 训练 vs 推理
- train：ground-truth prefix
- infer：model-generated prefix

### 结果
训练更稳定；推理存在 exposure bias 风险。

### 一句话模板
Teacher forcing conditions next-token prediction on ground-truth previous tokens during training, while inference uses model-generated tokens autoregressively.

## 5. 30 秒自检（考前口头版）
- 你能否一句话区分 token、token id、embedding？
- 你能否说清 word/char/subword 的核心 trade-off？
- 你能否解释为什么要除 `sqrt(d_k)`？
- 你能否说清 causal mask 屏蔽哪一块矩阵、为什么？
- 你能否准确说出 KV cache 缓存什么、不缓存什么、代价是什么？
- 你能否用 2 句说清 teacher forcing 与推理差异？
