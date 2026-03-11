# 2026-03-10 复习汇总：Q2 Transformer & Attention (Part 1)

## 范围 double check 结论
- 主考点：
  - scaled dot-product attention
  - attention scaling
  - BERT vs GPT objectives
- 支撑考点：
  - encoder-only / encoder-decoder / decoder-only
  - SHA vs MHA
  - attention computation flow
- 不要求重点展开：
  - tokenization
  - KV cache
  - teacher forcing
  - Flash Attention / MoE / RLHF 工程细节
- 对应考试形式：
  - Q2 风格短题
  - 一句题干，1-3 分钟作答
  - 重点考概念区分、公式、原因解释

## 当天合并 PDF 路径
- /Users/young/Coding/MRes/Courses/generativeai/genai_review/2026-03-10_Q2-Transformer_Attn_part1_study_pack.pdf

## 今日要点
- BERT 是 encoder-only，训练目标是 masked language modeling
- T5 是 encoder-decoder，学习条件概率 P(Y|X)
- GPT 是 decoder-only，训练目标是 autoregressive / causal language modeling
- GPT 公式：
  - P(X)=∏_{n=1}^N P(x_n|x_{1:n-1})
- Transformer block 的核心子层：
  - Multi-head Attention
  - FFN
- attention 三步流程：
  - S = QK^T
  - A = Softmax(S)
  - O = AV
- scaled dot-product attention：
  - O = Softmax(QK^T / sqrt(d_k))V
- 为什么除以 sqrt(d_k)：
  - 防止 QK^T 过大
  - 防止 softmax 过尖
  - 避免梯度过小
  - 提高训练稳定性
- MHA 比 SHA 强：
  - 不同 head 学习不同依赖关系
  - 表示更丰富

## 高频易错点
- 把 BERT 和 GPT 的训练目标混淆
- 会讲概念，但不会写公式
- 把 QK^T 说成 QV^T
- 忘记 O = AV
- 把 softmax 说成“选最大值”，而不是“变成概率分布”
- 把 scaling 原因说不完整，漏掉梯度和训练稳定性

## 关键概念卡

### 概念卡 1：三类语言模型
- BERT：encoder-only + masked LM
- T5：encoder-decoder + P(Y|X)
- GPT：decoder-only + autoregressive LM

### 概念卡 2：attention 流程
- 先算相似度：S = QK^T
- 再归一化：A = Softmax(S)
- 最后加权求和：O = AV

### 概念卡 3：Q/K/V
- Q：发起查询
- K：用于匹配，和 Q 计算相关性
- V：提供被加权汇总的内容

### 概念卡 4：attention scaling
- 除以 sqrt(d_k) 是为了防止分数过大
- 否则 softmax 过尖，梯度容易变小
- 作用：提高训练稳定性

### 概念卡 5：MHA
- split into multiple heads
- compute attention in parallel
- concatenate outputs
- 不同 head 学不同关系

## 对应考试形式的模拟题
1. 用一句话区分 BERT 和 GPT 的训练目标。
2. T5 属于哪类语言模型？它学习的概率是什么？
3. 写出 GPT 的 autoregressive language modeling 公式，并解释其中 P(x_n | x_{1:n-1}) 的含义。
4. 用一句话说明一个 Transformer block 的两个核心子层分别是什么。
5. 在 attention 中，Q、K、V 各自起什么作用？
6. 写出 scaled dot-product attention 的公式。
7. 为什么 attention 中要除以 sqrt(d_k)？如果不除，会发生什么？
8. 用一句话区分 Single-head attention 和 Multi-head attention。
9. 为什么 Multi-head attention 通常比 Single-head attention 更强？
10. 写出 attention 的三步符号流程，并说明 Softmax 的作用。

## 模拟题答案与解析

### 1.
- 答案：BERT 的训练目标是 masked language modeling；GPT 的训练目标是 autoregressive / causal language modeling。
- 解析：BERT 是补空；GPT 是按前文预测下一个 token。

### 2.
- 答案：T5 属于 encoder-decoder，学习的是 P(Y|X)。
- 解析：先编码输入，再生成输出。

### 3.
- 答案：P(X)=∏_{n=1}^N P(x_n|x_{1:n-1})
- 解析：第 n 个 token 的概率依赖于前面所有 token。

### 4.
- 答案：Transformer block 的两个核心子层是 Multi-head Attention 和 FFN。
- 解析：attention 负责建模依赖，FFN 负责逐位置非线性变换。

### 5.
- 答案：Q 用于查询，K 用于匹配并与 Q 计算分数，V 提供被加权汇总的内容。
- 解析：QK^T 产生成绩，V 提供内容。

### 6.
- 答案：O = Softmax(QK^T / sqrt(d_k))V
- 解析：这是 scaled dot-product attention 的标准公式。

### 7.
- 答案：除以 sqrt(d_k) 是为了防止 QK^T 过大，避免 softmax 过尖；否则容易导致梯度过小、训练不稳定。
- 解析：这是今天最关键的“为什么”。

### 8.
- 答案：single-head 只用一个头计算 attention；multi-head 将表示拆成多个头并行计算后再拼接。
- 解析：区别在“一个视角” vs “多个视角”。

### 9.
- 答案：因为不同 head 可以学习不同类型的依赖关系，所以表示更丰富。
- 解析：MHA 的优势不是“更多层”，而是“多种关系并行建模”。

### 10.
- 答案：
  - S = QK^T
  - A = Softmax(S)
  - O = AV
- 解析：Softmax 把相似度分数归一化为 attention 权重概率分布。

## 本次模拟题判分与错因
- 当前得分：7/10

### 主要失分点
- 第 3 题：只解释了含义，没有写公式
- 第 5 题：Q/K/V 定义不够精确
- 第 6 题：没有写公式
- 第 10 题：attention 三步符号流程没有写完整

## 下一轮优先复盘内容
- GPT 公式默写
- scaled dot-product attention 公式默写
- attention 三步流程默写
- Q / K / V 标准定义
