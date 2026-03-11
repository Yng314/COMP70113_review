# 2026-03-09 Generative AI Revision Summary

## 范围 Double Check 结论

- 今天对应考试 `Q2-CNN (20%)`。
- 明确要求：
  - 会算卷积层输出尺寸
  - 会算 `filter size` / 每个 filter 参数量
  - 会算整层总参数量
  - 会区分 `C_in`、`C_out`
  - 会算浅层网络的 `receptive field`
  - 会理解 `stride`、`pooling`、`feature maps`
- 明确不要求：
  - 超深网络复杂变体
  - 工程实现细节
  - 论文级复杂推导
- 题型对应：
  - 短计算题
  - 概念短答题
  - 公式代入题

## 当天合并 PDF

- 路径：[2026-03-09_Q2-CNN_slides_merged.pdf](/Users/young/Coding/MRes/Courses/generativeai/genai_review/2026-03-09_Q2-CNN_slides_merged.pdf)
- 主顺序页：`1-11`
- 重复页：`12-15`，已移到末尾并标记 `重复`

## 今日要点

- 卷积层输入输出基本形状：
  - `x_in ∈ R^{C_in × H × W}`
  - `x_out ∈ R^{C_out × H_out × W_out}`
- 最关键关系：
  - `输出通道数 = filter 个数 = C_out`
  - `每个 filter` 必须覆盖全部输入通道
- 每个 filter 参数量：
  - `C_in × K_h × K_w`
- 整层总参数量：
  - 无 bias：`C_out × C_in × K_h × K_w`
  - 有 bias：`C_out × (C_in × K_h × K_w + 1)`
- 输出尺寸公式：
  - `H_out = floor((H_in + 2P - K_h) / S_h) + 1`
  - `W_out = floor((W_in + 2P - K_w) / S_w) + 1`
- pooling：
  - 通常没有可学习参数
  - 通常主要改变 `H/W`，不改变通道数
- 深层 CNN 的直觉：
  - 空间分辨率通常下降
  - 通道数通常增加
  - 单个位置的 `receptive field` 变大
- CNN 的优势与边界：
  - 优势：局部连接 + 权重共享，参数高效
  - 边界：不擅长直接建模 long-range relationships

## 高频易错点

- 把“每个 filter 参数量”和“整层总参数量”混掉。
- 把 `C_in` 和 `C_out` 写反。
- 计算总参数量时把 `H/W` 也乘进去。
- 忘记 bias 是“每个输出通道一个”。
- 以为 pooling 会改通道数。
- 算 `receptive field` 时写成 `3+3=6` 或 `3x3 -> 9x9`。
- 写输出尺寸时忘记 `floor`。

## 关键概念卡

### 1. 卷积层形状卡

- `x_in ∈ R^{C_in × H × W}`
- `x_out ∈ R^{C_out × H_out × W_out}`
- `C_out = number of filters`

### 2. 参数量卡

- 每个 filter：
  - `C_in × K_h × K_w`
- 整层总参数量（含 bias）：
  - `C_out × (C_in × K_h × K_w + 1)`

### 3. 输出尺寸卡

- `H_out = floor((H_in + 2P - K_h) / S_h) + 1`
- `W_out = floor((W_in + 2P - K_w) / S_w) + 1`
- pooling 同样按这个思路算尺寸

### 4. Receptive Field 卡

- 一层 `3x3`：`3`
- 两层 `3x3`：`5`
- 三层 `3x3`：`7`
- 若 `stride=1`，每多一层 `3x3`，通常 `+2`
- 通用计算法：
  - 定义 `r_l`：第 `l` 层一个位置对应原输入的 `receptive field`
  - 定义 `j_l`：第 `l` 层相邻两个位置在原输入上相隔多远
  - 初始化：
    - `r_0 = 1`
    - `j_0 = 1`
  - 若第 `l` 层的 `kernel = k`、`stride = s`：
    - `r_l = r_{l-1} + (k - 1) * j_{l-1}`
    - `j_l = j_{l-1} * s`
  - 这个公式对 `Conv` 和 `Pooling` 都能用
  - 计算顺序必须按网络前向顺序，从前往后逐层算，不能倒着跳算
- 快速例子：
  - `Conv(3,1) -> Conv(3,2) -> Pool(2,2) -> Conv(3,1)`
  - 初始：`r=1, j=1`
  - 第1层后：`r=3, j=1`
  - 第2层后：`r=5, j=2`
  - 第3层后：`r=7, j=4`
  - 第4层后：`r=15, j=4`
  - 所以最后 `receptive field = 15 x 15`

### 5. 概念短答卡

- CNN 参数少：
  - `local connectivity + weight sharing`
- CNN 局限：
  - `not well-suited to modelling long-range relationships`

## 对应考试形式的模拟题

1. 已知输入 `x ∈ R^{3 × 32 × 32}`，卷积层使用 `16` 个 `5 × 5` filters，`stride=1`，`padding=0`，带 bias。写出：
   - `a)` 输出 shape
   - `b)` 每个 filter 参数量
   - `c)` 总参数量

2. 已知输入 `x ∈ R^{8 × 28 × 28}`，卷积层输出为 `R^{20 × 12 × 12}`，kernel 为正方形，`stride=2`，`padding=0`。问：kernel size 是多少？

3. 某层输入为 `R^{16 × 64 × 64}`，输出为 `R^{32 × 64 × 64}`，使用 `3 × 3` 卷积。写出：
   - `a)` filters 个数
   - `b)` 若带 bias，总参数量

4. 一层 `2 × 2 max pooling`，`stride=2`，输入为 `R^{24 × 10 × 10}`。写出：
   - `a)` 输出 shape
   - `b)` 该层可学习参数量

5. 连续两层 `3 × 3` 卷积，`stride=1`，无 pooling。问：最后一层一个输出位置对应原输入的 `receptive field` 是多少？

6. 用一句考试风格的话回答：为什么 CNN 的参数量通常比同规模全连接层更少？

## 模拟题答案与解析

- 你的答案：
  - `1a: 16*28*28`
  - `1b: 5*5*3`
  - `1c: 5*5*16*3+16`
  - `2: 20*5*5 或者 20*6*6`
  - `3a: 32`
  - `3b: 32*64*64*16+32`
  - `4a: 24*5*5`
  - `4b: 无`
  - `5: 5*5`
  - `6: cause cnn focus on partial and share parameters`
- 判分：`8.5 / 10`

### 1. 正确

- `a)` 输出 shape：
  - `16 × 28 × 28`
- `b)` 每个 filter 参数量：
  - `5 × 5 × 3 = 75`
- `c)` 总参数量：
  - `16 × (5 × 5 × 3 + 1) = 1216`

### 2. 部分正确

- 你意识到 kernel size 可能与 `5` 或 `6` 有关，这是对的。
- 但题目问的是 kernel size，不是总参数量，也不是 `20 × 5 × 5` 这种写法。
- 按标准带 `floor` 的公式：
  - `12 = floor((28 - K) / 2) + 1`
  - 所以 `K=5` 或 `K=6` 都可能得到 `12`
- 如果考试题写得规范，一般会避免这种歧义。
- 你这里的主要问题是：
  - 看错了题目在问“kernel size”，误写成了和输出通道相关的表达

### 3. `a)` 正确，`b)` 错误

- `a)` filters 个数：
  - `32`
- `b)` 总参数量应为：
  - `32 × (16 × 3 × 3 + 1) = 4640`
- 你的错误在于把空间尺寸 `64 × 64` 也乘进了参数量。
- 记住：
  - 参数量只和 `C_in`、`C_out`、kernel size、bias 有关
  - 与输入图片的 `H/W` 无关

### 4. 正确

- `a)` 输出 shape：
  - `24 × 5 × 5`
- `b)` pooling 参数量：
  - `0`

### 5. 正确

- 连续两层 `3x3`、`stride=1`：
  - `receptive field = 5x5`

### 6. 正确

- 更标准的考试写法：
  - `CNN has fewer parameters because it uses local connectivity and weight sharing, instead of connecting every output to every input like a fully connected layer.`

## 今天最容易错的点

- 你最容易把“空间尺寸”误乘进“参数量”。
- 你会做基础参数题，但一旦题目换问法，比如“kernel size”或“总参数量”，就容易把 `C_out`、`H/W`、kernel 概念混到一起。
- receptive field 这块已经明显变稳了。
- receptive field 题里要固定按网络顺序从前往后推：
  - 先更新 `r`
  - 再更新 `j`
  - 不能把不同层的 `stride` 和 `kernel` 直接相加或乱乘

## 考试可背诵版本

- `C_out = number of filters`
- `params per filter = C_in × K_h × K_w`
- `total params with bias = C_out × (C_in × K_h × K_w + 1)`
- `H_out = floor((H_in + 2P - K_h) / S_h) + 1`
- pooling usually has `0` learnable parameters
- `1 layer 3x3 -> RF = 3`
- `2 layers 3x3 -> RF = 5`
- `3 layers 3x3 -> RF = 7`
- RF 通用模板：
  - 初始：`r=1, j=1`
  - 每过一层：`r = r + (k-1)*j`
  - 每过一层：`j = j*s`
  - 按网络顺序从前往后算
- CNN:
  - `good at local pattern extraction`
  - `not well-suited to modelling long-range relationships directly`
