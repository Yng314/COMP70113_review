# 2026-03-07 Q1 3D + Video Review Summary

## 范围 Double Check 结论

- 今日范围：`Q1-3D + Q1-Video`
- 考试形式：单选题
- 3D 主考点：
  - `SDF`
  - `NeRF`
  - `3D Gaussian Splatting (3DGS)`
  - `SDS`
- Video 主考点：
  - `optical flow`
  - `temporal consistency`
  - `latent space operations`
- 不要求：
  - 论文级复杂推导
  - 工程实现细节
  - 具体网络层数、通道数、模块 trivia

## 今日合并 PDF

- 路径：`/Users/young/Coding/MRes/Courses/generativeai/genai_review/2026-03-07_Q1-3D_Video_slides_merged.pdf`
- 说明：
  - 已按今日复习顺序合并
  - 重复页已放在最后并标记为重复

## 今日要点

### 3D Generation

- `SDF`
  - 输出点到表面的带符号距离
  - `f(x)=0` 定义表面
  - 本课程口径：`outside > 0`，`inside < 0`
- `NeRF`
  - 输入：位置 `x` + 方向 `d`
  - 输出：密度 `sigma` + 颜色 `c`
  - 用 `volumetric rendering` 沿 ray 累积得到像素颜色
- `3DGS`
  - 用离散 `3D Gaussian primitives` 表示场景
  - 按可见性和贡献混合，类似 alpha blending
  - 相比 `NeRF`，更偏实时、高效
- `SDS`
  - 不是 3D 表示本身
  - 是用预训练 `2D diffusion model` 的 guidance/loss 来优化可微 3D 表示的方法
  - 常见被优化对象可以是 `NeRF`

### Video Generation

- `optical flow`
  - 相邻帧之间像素级位移场
  - 描述“像素怎么动”
- `temporal consistency`
  - 视频前后帧是否连贯稳定
  - 典型反例：闪烁、身份漂移、纹理忽隐忽现
  - `optical flow` 能帮助建模，但不等于 `temporal consistency`
- `latent space operations`
  - 在压缩后的 latent 表示中做生成/关键帧建模/插值
  - 再 decode 回像素空间，并做 upsampling
  - 典型流程：
    - latent key frames
    - latent frame interpolation
    - decode to pixel space
    - video upsampling

## 高频易错点

- `SDF` vs `SDS`
  - `SDF`：3D 表示，输出 signed distance
  - `SDS`：优化/引导方法
- `NeRF` vs `3DGS`
  - `NeRF`：continuous MLP query
  - `3DGS`：discrete Gaussian blending
- `optical flow` vs `temporal consistency`
  - `optical flow`：位移
  - `temporal consistency`：连贯稳定
- `latent space operations`
  - 不是直接在最终高清像素空间逐帧硬做
  - 是先在 latent 空间中生成和插值，再解码
- `point cloud` vs `mesh`
  - `point cloud`：一组点，顺序不重要，无拓扑信息
  - `mesh`：`V/E/F`，有连接结构，顺序重要

## 关键概念卡

### Card 1: 3D 表示

- `Point cloud`: a set of 3D points, permutation invariant, no topology
- `Mesh`: vertices, edges, faces; order matters
- `Voxel`: regular 3D occupancy grid; intuitive but expensive
- `Implicit function`: surface defined by `f(x)=0`

### Card 2: 3D 主考四件套

- `SDF`: signed distance, `f(x)=0`
- `NeRF`: `x, d -> sigma, c`
- `3DGS`: Gaussian primitives + blending
- `SDS`: 2D diffusion guidance for 3D optimization

### Card 3: Video 主考三件套

- `Optical flow`: pixel displacement between frames
- `Temporal consistency`: coherent frames over time
- `Latent ops`: key frames/interpolation in latent, then decode

## 对应考试形式的模拟题

### 模拟题 A（标准版）

1. 关于 `Signed Distance Function (SDF)`，哪项最准确？
   - A. 它输出每个点的颜色和密度
   - B. 它输出点到表面的带符号距离，表面通常由 `f(x)=0` 定义
   - C. 它由顶点、边、面直接定义表面
   - D. 它本质上是规则 voxel occupancy grid

2. 关于 `NeRF`，哪项最准确？
   - A. 它主要预测点到表面的 signed distance
   - B. 它只输入 3D 位置，不需要视角方向
   - C. 它输入位置和视角方向，输出密度和颜色
   - D. 它的核心是把场景表示成离散 Gaussian 集合

3. 关于 `3D Gaussian Splatting (3DGS)`，哪项最准确？
   - A. 它把场景表示成离散的 3D Gaussian primitives，并沿射线做混合
   - B. 它沿射线反复查询连续 MLP，得到颜色和密度
   - C. 它只能表示几何，不能表示颜色或透明度
   - D. 它必须先转成 mesh 才能渲染

4. 关于 `Score Distillation Sampling (SDS)`，哪项最准确？
   - A. 它是一种输出 signed distance 的 3D 表示
   - B. 它是一种把场景离散成 Gaussian 的方法
   - C. 它是一种 3D voxelization 算法
   - D. 它利用预训练 2D diffusion model 的 guidance/loss 去优化可微 3D 表示

5. 下面哪一项不是一种 3D 表示本身？
   - A. `SDF`
   - B. `NeRF`
   - C. `3DGS`
   - D. `SDS`

6. 关于 `optical flow`，哪项最准确？
   - A. 它描述相邻帧之间像素级位移
   - B. 它描述视频中每个物体的类别标签
   - C. 它等同于 temporal consistency
   - D. 它只用于音频生成

7. 一个生成视频里同一个物体在相邻帧中颜色、纹理、身份频繁闪烁，但大致运动方向还算合理。这个问题最直接对应：
   - A. optical flow 太大
   - B. tokenization 错误
   - C. temporal consistency 不足
   - D. latent space 太小

8. 关于 `optical flow` 和 `temporal consistency` 的关系，哪项最准确？
   - A. 二者完全同义
   - B. temporal consistency 只关心单帧清晰度
   - C. optical flow 是最终目标，temporal consistency 只是实现手段
   - D. optical flow 描述像素如何移动，temporal consistency 描述前后帧是否连贯稳定

9. 关于 `latent space operations`，哪项最准确？
   - A. 指直接在最终高清像素空间上逐帧编辑
   - B. 指在压缩后的 latent 表示中做生成、关键帧建模或插值，再解码回像素空间
   - C. 指把视频先转成 optical flow 再做分类
   - D. 指只在文本 embedding 上做操作，不涉及视频表示

10. 下面哪个流程最符合 slides 里的 latent video generation 思路？
    - A. 先上采样到高清像素，再做 latent interpolation，最后编码回 latent
    - B. 先做 optical flow，再直接输出最终视频，不需要解码
    - C. 先生成 latent key frames，再做 latent frame interpolation，然后 decode 到 pixel space，最后做 video upsampling
    - D. 先把视频转成 mesh，再做 diffusion transformer

### 模拟题 B（难点版）

1. 关于 `SDF`，下面哪一项最准确？
   - A. `SDF` 的输出只告诉我们点是否在物体内部，因此本质上等同于 occupancy
   - B. `SDF` 既编码“在内还是在外”，也编码“离表面有多远”
   - C. `SDF` 必须同时输出颜色和法向量，否则无法定义表面
   - D. `SDF` 的核心优势是天然支持 view-dependent effects

2. 某方法输入空间位置 `x` 和视角方向 `d`，输出 `sigma` 和 `c`，然后沿 ray 累积得到像素颜色。下面哪项判断最准确？
   - A. 这是 `SDF`，因为它需要知道方向
   - B. 这是 `NeRF`，因为它建模体密度和视角相关颜色
   - C. 这是 `3DGS`，因为它用离散 Gaussian 做 alpha blending
   - D. 这是 `SDS`，因为它用 diffusion guidance 更新 3D 表示

3. 关于 `NeRF` 与 `3DGS` 的对比，哪项最准确？
   - A. 两者都本质上依赖连续 MLP，只是训练损失不同
   - B. `NeRF` 更像离散高斯混合，`3DGS` 更像连续场查询
   - C. `NeRF` 查询连续场，`3DGS` 混合离散 Gaussian；两者都涉及可见性/遮挡权重
   - D. `3DGS` 不需要颜色信息，只需要几何中心和方差

4. 关于 `SDS`，哪项最准确？
   - A. `SDS` 的本质是把 3D 场景转成 voxel 再做 denoising
   - B. `SDS` 直接定义 3D 表面，因此和 `SDF` 同类
   - C. `SDS` 使用 2D diffusion 模型提供 guidance，并通过可微渲染更新 3D 参数
   - D. `SDS` 只能优化 `NeRF`，不能用于其他可微 3D 表示

5. 下面哪组对应关系是正确的？
   - A. `SDF -> density`，`NeRF -> signed distance`，`3DGS -> loss function`，`SDS -> representation`
   - B. `SDF -> signed distance`，`NeRF -> density/color field`，`3DGS -> Gaussian primitives`，`SDS -> optimization guidance`
   - C. `SDF -> voxel grid`，`NeRF -> mesh faces`，`3DGS -> prompt encoder`，`SDS -> rendering equation`
   - D. `SDF -> view-dependent reflection`，`NeRF -> topological constraints`，`3DGS -> tokenization`，`SDS -> audio spectrogram`

6. 一段生成视频中，人物轮廓在相邻帧之间轻微闪烁、衣服纹理时有时无，但整体运动方向基本合理。最直接的问题是：
   - A. optical flow 不存在
   - B. temporal consistency 不足
   - C. latent space 太大
   - D. 因果注意力一定失效

7. 关于 `optical flow` 与 `temporal consistency`，哪项最准确？
   - A. 有了正确 optical flow，就必然有完美 temporal consistency
   - B. temporal consistency 只和单帧清晰度有关，与跨帧无关
   - C. optical flow 描述像素位移；它有助于时序一致，但不等于时序一致
   - D. 两者都是在 latent space 里做关键帧插值的操作名

8. 关于 `latent space operations`，哪项最准确？
   - A. 指直接在像素空间上逐帧编辑，再把结果压缩到 latent
   - B. 指在压缩表示中进行生成、关键帧建模或插值，然后再 decode 到像素空间
   - C. 指只在文本 embedding 上做操作，不涉及视频表示
   - D. 指把 optical flow 作为 latent code 存起来即可完成视频生成

9. 如果一个视频模型的流程是“先生成 latent key frames，再做 latent frame interpolation，最后 decode 到 pixel space 并 upsample”，下面哪项理解最准确？
   - A. 这是典型的 latent video generation 思路，核心是先在压缩空间建模再回到像素空间
   - B. 这说明模型根本不需要时间维
   - C. 这等价于在原始高清像素空间直接做逐帧 diffusion
   - D. 这本质上是在做 `SDF` 的零水平集重建

10. 关于 `Causal Video Diffusion Models`，哪项最准确？
    - A. 因果注意力的核心结论是提升 temporal consistency，但和 latency 无关
    - B. 双向注意力在长视频里初始等待更重；因果注意力更适合降低初始等待时间
    - C. 因果注意力要求当前帧同时访问所有未来帧
    - D. 因果视频扩散的重点是把视频变成 mesh 再生成

## 模拟题答案与解析

### 模拟题 A 答案

- 1. B
- 2. C
- 3. A
- 4. D
- 5. D
- 6. A
- 7. C
- 8. D
- 9. B
- 10. C

### 模拟题 A 解析

- 1. `SDF` 的关键词是 `signed distance`
- 2. `NeRF` 的关键词是 `x + d -> density + color`
- 3. `3DGS` 的关键词是 `Gaussian primitives`
- 4. `SDS` 是 guidance/loss，不是表示
- 5. `SDS` 不是 3D 表示本身
- 6. `optical flow` 是像素位移场
- 7. 闪烁/身份漂移优先对应 `temporal consistency`
- 8. `optical flow` 讲位移，`temporal consistency` 讲连贯稳定
- 9. `latent ops` 在 latent 空间中做生成/插值
- 10. latent video 典型流程就是 `key frames -> interpolation -> decode -> upsample`

### 模拟题 B 答案

- 1. B
- 2. B
- 3. C
- 4. C
- 5. B
- 6. B
- 7. C
- 8. B
- 9. A
- 10. B

### 模拟题 B 解析

- 1. `SDF` 不只区分 inside/outside，还给出距离
- 2. 位置和方向输入、密度和颜色输出，对应 `NeRF`
- 3. `NeRF` 与 `3DGS` 的关键是 `continuous query` vs `discrete blending`
- 4. `SDS` 通过 2D diffusion guidance 和可微渲染更新 3D 参数
- 5. 这组定义映射是本节最需要背清楚的边界
- 6. 运动大体合理但外观闪烁，是时序一致性不足
- 7. `optical flow` 有助于 `temporal consistency`，但不等于它
- 8. `latent space operations` 的本质是在压缩空间做时空建模
- 9. 这是 slides 中明确展示的 latent video pipeline
- 10. 因果视频扩散的高频考点是 `latency` 优势

## 本次模拟结果

- 模拟题 A：`10/10`
- 模拟题 B：`10/10`

## 最后压缩背诵版

- `SDF`: signed distance, `f(x)=0`
- `NeRF`: `x, d -> sigma, c`
- `3DGS`: Gaussian primitives + blending
- `SDS`: 2D diffusion guidance for 3D optimization
- `Optical flow`: pixel displacement
- `Temporal consistency`: no flicker, coherent over time
- `Latent ops`: latent key frames + interpolation + decode + upsample
