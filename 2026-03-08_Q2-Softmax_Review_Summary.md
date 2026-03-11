# 2026-03-08 Generative AI Revision Summary

## 范围 Double Check 结论

- 今天对应考试 `Q2-Softmax (15%)`。
- 明确要求：
  - 会写 `softmax` 公式
  - 会从 `logits` 得到 `softmax probabilities`
  - 会写 `cross-entropy loss`
  - 会写最终梯度结论 `p - y`
  - 会识别 `one-hot label`
- 明确不要求：
  - 考场上完整重推复杂反向传播
  - 逐页证明所有中间偏导
  - 工程实现细节
- 题型对应：
  - 短计算题
  - 概念解释题
  - 手写公式题

## 当天合并 PDF

- 路径：[2026-03-08_Q2-Softmax_slides_merged.pdf](/Users/young/Coding/MRes/Courses/generativeai/genai_review/2026-03-08_Q2-Softmax_slides_merged.pdf)
- 主顺序页：`1-16`
- 重复页：`17-25`，已移到末尾并标记 `DUPLICATE`

## 今日要点

- `softmax` 的作用是把 `logits z` 变成概率分布 `p`：
  - `p_k = e^{z_k} / \sum_j e^{z_j}`
- `cross-entropy loss` 只看正确类概率：
  - `L = -log p_y`
  - 等价写法：`L = -\sum_j y_j log(p_j)`
- `one-hot label` 的含义：
  - 正确类那一位是 `1`
  - 其他位都是 `0`
- `softmax + CE` 的最终梯度结论：
  - `\partial L / \partial z = p - y`
- 多样本训练时，总 loss 是逐样本求和：
  - `L = -\sum_i \sum_j y_j^{(i)} log(p_j^{(i)})`
- `maximum likelihood` 与 `minimize cross-entropy` 等价

## 高频易错点

- 不要把 `logits` 当成概率。
- 不要把 `exp(logits)` 当成最终 `softmax` 输出。
- 不要把 `loss` 写成看“预测最大类”的概率；它看的是“真实正确类”的概率。
- 不要把梯度写成 `y - p`；正确是 `p - y`。
- 不要在多样本题里把 `-log(0.9) - log(0.4)` 直接错算成 `1.3`。
- 不要在考场上花时间重推中间导数页；老师明确说重点是最终结论。

## 关键概念卡

### 1. Softmax

- 定义：把一组 `logits` 变成概率分布。
- 公式：`p_k = e^{z_k} / \sum_j e^{z_j}`
- 必须满足：
  - 每一项 `>= 0`
  - 总和 `= 1`

### 2. Cross-Entropy

- 单样本：`L = -log p_y`
- 等价写法：`L = -\sum_j y_j log(p_j)`
- 直觉：
  - 正确类概率越大，loss 越小
  - 正确类概率越小，loss 越大

### 3. One-hot Label

- 3 分类例子：
  - 第 1 类：`[1,0,0]`
  - 第 2 类：`[0,1,0]`
  - 第 3 类：`[0,0,1]`
- 作用：帮助你快速定位“loss 看哪一格”

### 4. 最终梯度

- 必背：`\partial L / \partial z = p - y`
- 解释：
  - `p` 是模型预测概率
  - `y` 是真实 one-hot 标签
- 考试中优先写这个，不要重推整页反传

### 5. 多样本 CE Loss

- `L = -\sum_i \sum_j y_j^{(i)} log(p_j^{(i)})`
- 记忆法：
  - 单样本先会
  - 多样本就是把每个样本的 loss 加起来

## 对应考试形式的模拟题

1. 已知 `z = [1, 0, -1]`，真实标签 `y = [1,0,0]`。写出：
   - `p_1 = ?`
   - `L = ?`

2. 已知 `p = [0.2, 0.5, 0.3]`，`y = [0,1,0]`。写出 `\partial L/\partial z`。

3. 已知 `y = [0,0,1]`，`a = [0.1,0.2,0.7]`。写出：
   - `likelihood = \prod_j a_j^{y_j} = ?`
   - `CE loss = ?`

4. 一个 `4` 分类 softmax classifier，输入特征维度是 `6`。写出 `W` 和 `b` 的维度。

5. 有两个样本，正确类概率分别是 `0.9` 和 `0.4`。写出总的 cross-entropy loss。

## 模拟题答案与解析

- 你的答案：
  1. `p_1 = exp(1)/(exp(1)+exp(0)+exp(-1))`
     `L = -log(exp(1)/(exp(1)+exp(0)+exp(-1)))`
  2. `[0.2, -0.5, 0.3]`
  3. `likelihood = 0.7`
     `CE loss = -log(0.7)`
  4. `W: 4*6, b: 4*1`
  5. `1.3`
- 判分：`4 / 5`

### 1. 正确

- `p_1 = e^1 / (e^1 + e^0 + e^{-1})`
- `L = -log(p_1)`
- 这是标准写法。

### 2. 正确

- `\partial L/\partial z = p - y = [0.2, 0.5, 0.3] - [0,1,0] = [0.2, -0.5, 0.3]`

### 3. 正确

- `likelihood = 0.1^0 * 0.2^0 * 0.7^1 = 0.7`
- `CE loss = -log(0.7)`

### 4. 正确

- 标准写法：
  - `W : 4 x 6`
  - `b : 4 x 1`

### 5. 错误

- 正确答案应为：
  - `L = -log(0.9) - log(0.4)`
  - 也可写成 `-(log 0.9 + log 0.4)`
- 如果取自然对数，数值约为 `1.0217`
- 你这里的错误不是概念错，而是把符号表达直接误算成了一个错误数值。

## 今天最容易错的点

- 一看到多样本 loss 就急着算数值，容易算错。考试里先写标准式子最稳。
- `loss` 看的是“真实类概率”，不是“最大概率类”。
- `softmax -> CE -> p - y` 这条链要固定住顺序。

## 考试可背诵版本

- `z = Wx + b`
- `p_k = e^{z_k} / \sum_j e^{z_j}`
- `L = -log p_y = -\sum_j y_j log(p_j)`
- `\partial L / \partial z = p - y`
- 多样本：
  - `L = -\sum_i \sum_j y_j^{(i)} log(p_j^{(i)})`
- `maximize likelihood <=> minimize cross-entropy`
