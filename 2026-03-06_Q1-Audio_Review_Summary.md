# 2026-03-06 Generative AI Revision Summary

## 范围 Double Check 结论

- 今天对应考试 `Q1-Audio` 单选题。
- 明确要求：
  - `waveform` 与 `spectrogram` 的区别
  - 为什么很多 TTS 系统先预测 `spectrogram`
  - `voice cloning` 中 `speaker embedding` 的作用
  - `speech tokenizer`、`quantization`、`VQ-VAE`、`VQGAN` 的基本定位
- 明确不要求：
  - TTS / vocoder 的工程实现细节
  - 具体论文结构细节
  - 复杂推导和训练细节
- 题型对应：
  - 概念辨析型单选
  - 常见问法是“哪个说法正确/错误”“哪个模块负责什么”“哪个表示更适合什么任务”

## 当天合并 PDF

- 路径：[2026-03-06_Q1-Audio_slides_merged.pdf](/Users/young/Coding/MRes/Courses/generativeai/genai_review/output/pdf/2026-03-06_Q1-Audio_slides_merged.pdf)

## 今日要点

- `waveform` 是时域原始信号，横轴时间，纵轴振幅。
- `spectrogram` 是时频表示，横轴时间，纵轴频率，颜色或亮度表示能量。
- 经典 TTS 常见流程：`text -> mel spectrogram -> waveform`。
- `Tacotron` 的考试定位是 `text -> mel spectrogram`。
- `WaveNet` / `HiFi-GAN` 的考试定位是 `spectrogram -> waveform`，属于 `vocoder`。
- `voice cloning` 的关键是 `speaker embedding`，表示说话人特征，不表示文本内容。
- `speech tokenizer` 的关键是把连续语音变成离散 token，方便像语言模型一样建模。
- `quantization` 是把连续表示映射到有限码本，形成离散表示。
- `VQ-VAE` 的关键是 `continuous latent -> codebook quantization -> discrete codes`。
- `VQGAN` 可以记成：`VQ-VAE + adversarial loss`。

## 高频易错点

- 不要把 `waveform` 和 `spectrogram` 混淆。
- 不要说 `spectrogram` 是离散 token；它通常仍是连续表示。
- 不要把 `speaker embedding` 说成文本内容表示；它表示说话人风格/身份特征。
- 不要把 `Tacotron` 和 `vocoder` 混淆。
- 不要把 `WaveNet` / `HiFi-GAN` 说成文本到语音的前端模型。
- 不要把 `waveform -> spectrogram` 和 `quantization` 当成同一件事。
- 不要把 `VQ-VAE` 和普通 `VAE` 混为一谈。
- 不要把 `VQGAN` 当成“只有 GAN，没有 VQ codebook”的模型。

## 关键概念卡

### 1. Waveform vs Spectrogram

- `waveform`：原始时域信号。
- `spectrogram`：时频能量表示。
- 考试一句话：
  - `waveform` tells how amplitude changes over time.
  - `spectrogram` tells how frequency energy changes over time.

### 2. 为什么先预测 Spectrogram

- 原始 `waveform` 采样点太密，直接建模难。
- `spectrogram` 更结构化，更适合学习音素、节奏、韵律。
- 常见思路：主模型先预测 `mel spectrogram`，再由 `vocoder` 恢复波形。

### 3. Voice Cloning

- 核心：复制说话人风格，不是复制文本内容。
- `speaker embedding` 来自参考语音。
- 它表示 `speaker identity/style`，不是 `linguistic content`。

### 4. Speech Tokenization

- 目标：把连续语音变成离散 token。
- 本质：让语音也能像文本一样做序列建模。
- 不是传统 TTS 本身，而是一种表示和编码方法。

### 5. Quantization / VQ-VAE / VQGAN

- `quantization`：连续表示映射到有限码本。
- `VQ-VAE`：连续 latent 经 codebook 变成离散 codes。
- `VQGAN`：`VQ-VAE + adversarial loss`。

## 对应考试形式的模拟题

1. 关于 `waveform`，哪项正确？  
   A. 它表示频率能量随时间变化  
   B. 它是语音在时域上的原始振幅信号  
   C. 它天然是离散 token 序列  
   D. 它比 spectrogram 更直接表示语义

2. 关于 `spectrogram`，哪项正确？  
   A. 横轴频率、纵轴振幅  
   B. 它不能表示时间信息  
   C. 它展示不同时间点的频率能量分布  
   D. 它就是 speaker embedding 的可视化

3. 为什么很多 TTS 系统先预测 `mel spectrogram`？  
   A. 因为它是最终可播放音频  
   B. 因为它比 waveform 更结构化、更易建模  
   C. 因为它不含频率信息  
   D. 因为它等价于文本 token

4. `Tacotron` 最合适的定位是：  
   A. 文本到 `mel spectrogram` 的 TTS 框架  
   B. 直接生成最终 waveform 的 vocoder  
   C. 只做说话人识别  
   D. 只做语音量化

5. `voice cloning` 中 `speaker embedding` 的主要作用是：  
   A. 表示句子文本内容  
   B. 表示说话人特征/声音风格  
   C. 直接输出 waveform  
   D. 替代 spectrogram

6. 下列哪项最符合 `vocoder` 的职责？  
   A. 把文本编码成字符序列  
   B. 把 speaker embedding 聚类  
   C. 把 spectrogram 恢复成 waveform  
   D. 把 waveform 变成 token

7. 为什么直接生成 waveform 较困难？  
   A. 因为 waveform 没有时间结构  
   B. 因为音频采样分辨率高，逐点生成代价大  
   C. 因为 waveform 不能被神经网络处理  
   D. 因为 waveform 已经是离散码本表示

8. `speech tokenizer` 的核心目标是：  
   A. 把连续语音表示变成适合序列模型的离散 token  
   B. 只保留说话人身份  
   C. 直接把文本翻译成语音  
   D. 替代所有 vocoder

9. `vector quantization` 的核心作用是：  
   A. 把连续表示映射到有限码本向量  
   B. 直接把 spectrogram 变成 waveform  
   C. 计算 cosine similarity  
   D. 估计 F0

10. 关于 `VQGAN`，哪项正确？  
    A. 它就是普通 GAN，与 VQ 无关  
    B. 它可以理解为 `VQ-VAE + adversarial loss`  
    C. 它只用于 speaker embedding 学习  
    D. 它证明 waveform 一定优于 spectrogram

11. 关于 `waveform` 与 `spectrogram` 的关系，哪项最准确？  
    A. 二者完全等价，只是画法不同  
    B. waveform 是时域表示，spectrogram 是时频表示  
    C. spectrogram 是离散 token，waveform 是连续 token  
    D. waveform 由 spectrogram 直接逐字映射得到

12. 关于 `voice cloning`，哪项错误？  
    A. 它关注“怎么说”，不只是“说了什么”  
    B. speaker embedding 来自参考语音  
    C. 它的核心是复制文本内容而不是声音风格  
    D. 它通常可与 synthesizer + vocoder 流程结合

## 模拟题答案与解析

- 你的答案：`1B 2C 3B 4A 5B 6C 7B 8A 9A 10B 11B 12C`
- 判分：`12 / 12`

1. `B` 正确。`waveform` 是语音在时域上的原始振幅信号。
2. `C` 正确。`spectrogram` 反映的是时间上的频率能量分布。
3. `B` 正确。`mel spectrogram` 更结构化，通常比直接建模 `waveform` 更容易。
4. `A` 正确。`Tacotron` 的考试定位是 `text -> mel spectrogram`。
5. `B` 正确。`speaker embedding` 表示说话人风格或身份特征。
6. `C` 正确。`vocoder` 负责 `spectrogram -> waveform`。
7. `B` 正确。原始音频时间分辨率高，逐点生成成本大。
8. `A` 正确。`speech tokenizer` 把连续语音变成离散 token。
9. `A` 正确。`vector quantization` 是映射到有限码本。
10. `B` 正确。`VQGAN` 可理解为 `VQ-VAE + adversarial loss`。
11. `B` 正确。`waveform` 是时域，`spectrogram` 是时频域。
12. `C` 正确。题目问错误项，错误在于把 `voice cloning` 说成复制文本内容。

## 今天最值得继续盯防的点

- 你今天题目全对，但最容易在正式考试里失分的仍然是边界混淆：
  - `speaker embedding` vs `semantic content`
  - `spectrogram` vs `discrete tokens`
  - `Tacotron` vs `vocoder`
  - 表示变换 `waveform -> spectrogram` vs 离散化 `quantization`
- 如果明天开始前做 3 分钟回忆，优先背这 4 组边界。
