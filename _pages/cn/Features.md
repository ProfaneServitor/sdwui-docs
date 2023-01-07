---
title: 特征
layout: post
category: Guides
permalink: /features/
machine_translated: true
lang: cn
---
这是 [Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 的功能展示页面。

除非另有说明，否则所有示例都是非精选的。

# 稳定扩散 2.0
## 基本模型
支持的模型：768-v-ema.ckpt（[模型]（https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/768-v-ema.ckpt），[配置]（https ://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference-v.yaml)) 和 512-base-ema.ckpt ([模型](https://huggingface .co/stabilityai/stable-diffusion-2-base/blob/main/512-base-ema.ckpt), [配置](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/稳定扩散/v2-inference.yaml））。 2.1 检查站也应该工作。

- 下载检查点（从这里：https://huggingface.co/stabilityai/stable-diffusion-2）
- 将其放入 models/Stable-Diffusion 目录
- 从 SD2.0 存储库中获取配置并将其放入与检查点相同的位置，将其重命名为具有相同的文件名（即，如果您的检查点名为“768-v-ema.ckpt”，则配置应命名为“768- v-ema.yaml`)
- 从 UI 中选择新的检查点

对于 2.0 模型，训练选项卡很可能会被破坏。

如果 2.0 或 2.1 正在生成黑色图像，请使用 `--no-half` 启用全精度或尝试使用 `--xformers` 优化。

_**注意：**_ SD 2.0 和 2.1 对 FP16 数值不稳定性更敏感（正如他们自己所指出的[此处](https://github.com/Stability-AI/stablediffusion/commit/c12d960d1ee4f9134c2516862ef991ec52d3f59e)）由于它们新的交叉注意力模块。

在 fp16 上：[comment](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/5503#issuecomment-1341495770) 在 webui-user.bat 中启用：

@回声关闭

设置蟒蛇=
设置 GIT=
设置 VENV_DIR=
设置 COMMANDLINE_ARGS=你的命令行选项
set STABLE_DIFFUSION_COMMIT_HASH="c12d960d1ee4f9134c2516862ef991ec52d3f59e"
设置 ATTN_PRECISION=fp16

调用webui.bat

##深度引导模型
[更多信息](https://github.com/Stability-AI/stablediffusion#depth-conditional-stable-diffusion)。 [PR](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/5542)。
指示：
- 下载 [512-depth-ema.ckpt](https://huggingface.co/stabilityai/stable-diffusion-2-depth) 检查点
- 将其放置在模型/稳定扩散中
- 获取 [config](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-midas-inference.yaml) 并将其放在与检查点相同的文件夹中
- 将配置重命名为“512-depth-ema.yaml”
- 从 UI 中选择新的检查点

深度引导模型仅适用于 img2img 选项卡。

# 涂装

Outpainting 扩展了原始图像并修复了创建的空白区域。

例子：

|原创 |外涂 |再次超越 |
|------------------------------|------------------------------|------------------------------|

| ![](图片/outpainting-1.png) | ![](图像/outpainting-2.png) | ![](图片/outpainting-3.png) |

来自 4chan 的匿名用户的原始图像。谢谢匿名用户。

您可以在底部的 img2img 选项卡中找到该功能，位于脚本 -> 穷人的涂装下。

Outpainting 与普通图像生成不同，它似乎从大步数中获益良多。一个好的涂装的秘诀
是一个很好的提示，与图片相匹配，用于去噪的滑块和 CFG 比例设置为最大，步数为 50 到 100
Euler 祖先或 DPM2 祖先采样器。

| 81 步，欧拉 A | 30 步，欧拉 A | 10 步，欧拉 A | 80 步，欧拉 A |
|-------------------------------------|---------------------------------------|--------------------------------------|-------------------------------------|

| ![](图像/inpainting-81-euler-a.png) | ![](图像/inpainting-30-euler-a.png) | ![](图像/修复-10-euler-a.png) | ![](图像/inpainting-80-dpm2-a.png) |

# 修复
在 img2img 选项卡中，在图像的一部分上绘制遮罩，该部分将被补漆。

![](图像/修复.png)

修复选项：
- 在网络编辑器中自己绘制一个面具
- 在外部编辑器中删除部分图片并上传透明图片。任何稍微透明的区域都将成为蒙版的一部分。请注意 [某些编辑器](https://docs.krita.org/en/reference_manual/layers_and_masks/split_alpha.html#how-to-save-a-png-texture-and-keep-color-values-in-全透明区域）默认将完全透明区域保存为黑色。
- 将模式（图片右下角）更改为“上传蒙版”并为蒙版选择单独的黑白图像（白色=修复）。

##修复模型
RunwayML 已经训练了一个专门为修复而设计的附加模型。这个模型接受额外的输入——没有噪声的初始图像加上蒙版——并且似乎在工作上要好得多。

该模型的下载和额外信息在这里：https://github.com/runwayml/stable-diffusion#inpainting-with-stable-diffusion

要使用该模型，您必须重命名检查点，使其文件名以“inpainting.ckpt”结尾，例如“1.5-inpainting.ckpt”。

之后只需选择检查点，因为您通常会选择任何检查点，您就可以开始了。

## 屏蔽内容
屏蔽的内容字段决定了在修复之前将内容放入屏蔽区域。

| mask                                            | fill                                            | original                                            | latent noise                                            | latent nothing                                            |
|-------------------------------------------------|-------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------|

| ![](图像/修复初始内容掩码.png) | ![](图像/修复初始内容填充.png) | ![](图像/修复初始内容-original.png) | ![](图像/修复初始内容-潜在噪声.png) | ![](图像/修复初始内容-潜在-nothing.png) |

## 以全分辨率修复
通常，修复会将图像调整为 UI 中指定的目标分辨率。全分辨率 Inpaint
启用后，仅调整遮罩区域的大小，并在处理后粘贴回原始图片。
这允许您处理大图片，并允许您以更大的分辨率渲染修复的对象。


|输入 |修复正常 |全分辨率修复 |
|-------------------------------------|----------------------------------|-----------------------------------|

| ![](图像/inpaint-whole-mask.png) | ![](图像/inpaint-whole-no.png) | ![](图像/inpaint-whole-yes.png) |


## 屏蔽模式
屏蔽模式有两个选项：
- Inpaint masked - 遮罩下的区域被修复
- Inpaint not masked - 面具下没有变化，其他一切都被修复

## 阿尔法蒙版

|输入 |输出 |
|------------------------------|-------------------------------|

| ![](图像/修复-mask.png) | ![](图像/inpaint-mask2.png) |


# 提示矩阵
使用 `|` 字符分隔多个提示，系统将为它们的每个组合生成一个图像。
例如，如果您使用“现代城市中繁忙的城市街道|插图|电影灯光”提示，则有四种可能的组合（提示的第一部分始终保留）：

- `现代城市中繁忙的城市街道`
- `现代城市中繁忙的城市街道，插图`
- `现代城市中繁忙的城市街道，电影般的灯光`
-`现代城市中繁忙的城市街道，插图，电影灯光`

将按此顺序生成四个图像，所有图像都具有相同的种子，每个图像都有相应的提示：
![](图片/提示矩阵.png)

另一个例子，这次有 5 个提示和 16 个变体：
![](图片/prompt_matrix.jpg)

您可以在底部的脚本 -> 提示矩阵下找到该功能。

# 彩色素描

img2img 的基本着色工具。要在 img2img 中使用此功能，请在命令行参数中使用“--gradio-img2img-tool color-sketch”启用。要在修复模式下使用此功能，请启用“--gradio-inpaint-tool color-sketch”。基于 Chromium 的浏览器支持滴管工具。 （见图）

![滴管](https://user-images.githubusercontent.com/98228077/196140222-54bc71ad-2746-4c38-8075-5c53fbcde2a9.png)


#稳定扩散高档
使用 RealESRGAN/ESRGAN 的高档图像，然后遍历结果的图块，使用 img2img 改进它们。
它还有一个选项，让您可以在外部程序中自己完成放大部分，只需使用 img2img 遍历图块。

原创想法：https://github.com/jquesnelle/txt2imghd。这是一个独立的实现。

要使用此功能，请从脚本下拉选择中选择“SD upscale”（img2img 选项卡）。

![chrome_dl8hcMPYcx](https://user-images.githubusercontent.com/39339941/193300082-be3b8864-3c28-44b7-bb75-f893f92269b6.png)

输入图像将放大到原始图像的两倍
宽度和高度，以及 UI 的宽度和高度滑块指定各个图块的大小。因为重叠，
拼贴的大小可能非常重要：512x512 图像需要九个 512x512 拼贴（因为重叠），但仅
四个 640x640 的图块。

升级的推荐参数：
- 采样方法：欧拉a
- 降噪强度：0.2，如果你喜欢冒险，可以提高到 0.4

|原创 |真ESRGAN |黄玉十亿像素 |标清高档|
|-------------------------------------------|---------------------------------------------|---------------------------------------------------------|---------------------------------------------|

| ![](图片/sd-upscale-robot-original.png) | ![](图片/sd-upscale-robot-realrgan.png) | ![](图像/sd-upscale-robot-esrgan-topaz-gigapixel.png) | ![](图片/sd-upscale-robot-sd-upscale.png) |
| ![](图片/sd-upscale-castle-original.png) | ![](图片/sd-upscale-castle-realesrgan.png) | ![](图片/sd-upscale-castle-esrgan-topaz-gigapixel.png) | ![](图片/sd-upscale-castle-sd-upscale.png) |
| ![](图片/sd-upscale-city-original.png) | ![](图片/sd-upscale-city-realesrgan.png) | ![](图片/sd-upscale-city-esrgan-topaz-gigapixel.png) | ![](图片/sd-upscale-city-sd-upscale.png) |

# 注意/强调
在提示中使用 `()` 会增加模型对封闭词的注意力，而 `[]` 会减少它。您可以组合多个修饰符：

![](图片/attention-3.jpg)

备忘单：

- `a (word)` - 将对 `word` 的关注度提高 1.1 倍
- `a ((word))` - 将对 `word` 的关注度提高 1.21 (= 1.1 * 1.1)
- `a [word]` - 将对 `word` 的关注度降低 1.1 倍
- `a (word:1.5)` - 将对 `word` 的关注度提高 1.5 倍
- `a (word:0.25)` - 将对 `word` 的关注度降低 4 倍（= 1 / 0.25）
- `a \(word\)` - 在提示中使用文字 `()` 字符

使用 `()`，可以像这样指定权重：`(text:1.4)`。如果未指定权重，则假定为 1.1。指定权重仅适用于 `()` 而不适用于 `[]`。

如果你想在提示中使用任何文字 `()[]` 字符，请使用反斜杠将它们转义：`anime_\(character\)`。

在 2022-09-29，添加了支持转义字符和数字权重的新实现。新实现的一个缺点是旧实现并不完美，有时会吃掉字符：例如，“a (((farm))), daytime”，如果没有逗号，将变成“a farm daytime”。正确保留所有文本的新实现不共享此行为，这意味着您保存的种子可能会产生不同的图片。目前，设置中有一个选项可以使用旧的实现。

NAI 使用我在 2022 年 9 月 29 日之前的实现，除了他们使用 1.05 作为乘数并使用“{}”而不是“()”。所以转换适用：

- 他们的 `{word}` = 我们的 `(word:1.05)`
- 他们的 `{{word}}` = 我们的 `(word:1.1025)`
- 他们的 `[word]` = 我们的 `(word:0.952)` (0.952 = 1/1.05)
- 他们的 `[[word]]` = 我们的 `(word:0.907)` (0.907 = 1/1.05/1.05)


# 环回
在 img2img 中选择环回脚本允许您自动将输出图像作为下一批的输入。相当于
保存输出图像，并用它替换输入图像。批次计数设置控制多少次迭代
这是你得到的。

通常，在执行此操作时，您会自己从众多图像中选择一个用于下一次迭代，因此有用性
这个功能可能有问题，但我已经设法用它获得了一些我无法获得的非常好的输出
否则。

示例：（精选结果）

![](图片/loopback.jpg)

来自 4chan 的匿名用户的原始图像。谢谢匿名用户。

# X/Y 图
创建具有不同参数的图像网格。选择哪些参数应由行和列使用共享
X 类型和Y 类型字段，并将以逗号分隔的那些参数输入到X 值/Y 值字段中。对于整数，
和浮点数，并支持范围。例子：

- 简单范围：
- `1-5` = 1、2、3、4、5
- 括号内增量的范围：
- `1-5 (+2)` = 1, 3, 5
- `10-5 (-3)` = 10, 7
- `1-3 (+0.5)` = 1, 1.5, 2, 2.5, 3
- 方括号中包含计数的范围：
- `1-10 [5]` = 1, 3, 5, 7, 10
- `0.0-1.0 [6]` = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0

![](图片/xy_grid-medusa.png)

以下是创建上图的设置：

![](图片/xy_grid-medusa-ui.png)

### 提示S/R
Prompt S/R 是 X/Y Plot 较难理解的操作模式之一。 S/R 代表搜索/替换，这就是它的作用 - 您输入一个单词或短语列表，它从列表中获取第一个并将其视为关键字，然后用列表中的其他条目替换该关键字的所有实例.

例如，使用提示 `a man holding an apple, 8k clean` 和 Prompt S/R `an apple, a watermelon, a gun` 你会得到三个提示：

-`一个拿着苹果的男人，8k 干净`
-`一个拿着西瓜的人，8k 干净`
-`一个拿着枪的男人，8k 干净`

该列表使用与 CSV 文件中的一行相同的语法，因此如果您想在条目中包含逗号，您必须将文本放在引号中并确保引号和分隔逗号之间没有空格：

- `darkness, light, green, heat` - 4 items - `darkness`, `light`, `green`, `heat`
- `darkness, "light, green", heat` - 错误 - 4 items - `darkness`, `"light`, `green"`, `heat`
- `darkness,"light, green", heat` - RIGHT - 3 items - `darkness`, `light, green`, `heat`

# 文本反转
简短说明：将您的嵌入放入 embeddings 目录，并在提示中使用文件名。

详细解释：[Textual Inversion](Textual-Inversion)

![grid-0037](https://user-images.githubusercontent.com/20920490/193285770-9454c5e1-e594-463c-8be8-1488ddf2877b.png)

# 调整大小
在 img2img 模式下调整输入图像的大小有三个选项：

- 调整大小 - 简单地将源图像调整为目标分辨率，导致宽高比不正确
- 裁剪和调整大小 - 调整源图像的大小以保持纵横比，使其占据整个目标分辨率，并裁剪突出的部分
- 调整大小和填充 - 调整源图像的大小，保留宽高比，使其完全适合目标分辨率，并按源图像的行/列填充空白空间

例子：
![](图片/resizing.jpg)

# 采样方式选择
为txt2img挑出多种采样方式：

![](图片/采样.jpg)

# 种子调整大小
此功能允许您从不同分辨率的已知种子生成图像。通常，当您更改分辨率时，
即使保留所有其他参数（包括种子），图像也会完全改变。通过调整种子大小，您可以指定分辨率
的原始图像，并且模型很可能会产生看起来非常相似的东西，即使分辨率不同。
在下面的示例中，最左边的图片是 512x512，其他图片使用完全相同的参数生成，但垂直方向更大
解析度。

|资讯 |图片 |
|---------------------------|-------------------------------|

|未启用种子调整大小 | ![](图片/seed-noresize.png) |
|种子从 512x512 调整大小 | ![](图片/seed-resize.png) |

祖先采样器在这方面比其他采样器差一点。

您可以通过单击种子附近的“额外”复选框找到此功能。

＃ 变化
变化强度滑块和变化种子字段允许您指定现有图片应更改多少以使其看起来
像一个不同的。在最大强度下，您将获得带有变异种子的图片，至少 - 带有原始种子的图片（除了
用于使用祖先采样器时）。

![](图片/种子变体.jpg)

您可以通过单击种子附近的“额外”复选框找到此功能。

# 样式
按“将提示另存为样式”按钮将当前提示写入 styles.csv，这是一个包含样式集合的文件。一个保管箱
提示的右侧将允许您从以前保存的样式中选择任何样式，并自动将其附加到您的输入中。
要删除样式，请从 styles.csv 中手动删除它并重新启动程序。

如果您在样式中使用特殊字符串“{prompt}”，它会将提示中当前的任何内容替换到该位置，而不是将样式附加到您的提示中。

# 否定提示

允许您使用另一个提示，提示模型在生成图片时应避免的事情。这通过使用
采样过程中无条件条件的否定提示，而不是空字符串。

进阶解释：【否定提示】（Negative-prompt）

|原创 |负：紫色 |负面：触角 |
|-------------------------------|---------------------------------|------------------------------------|

| ![](图片/negative-base.png) | ![](图片/negative-purple.png) | ![](图片/negative-tentacles.png) |

#CLIP 询问器

最初来自：https://github.com/pharmapsychotic/clip-interrogator

CLIP 询问器允许您从图像中检索提示。提示不允许您重现此内容
精确的图像（有时它甚至不会很接近），但这可能是一个好的开始。

![](图片/CLIP-interrogate.png)

第一次运行 CLIP interrogator 时，它会下载几千兆字节的模型。

CLIP 询问器有两个部分：一个是 BLIP 模型，它根据图片创建文本描述。
另一个是 CLIP 模型，它会从列表中挑选出与图片相关的几行。默认情况下，有
只是一个列表 - 艺术家列表（来自 `artists.csv`）。您可以通过执行以下操作添加更多列表：

- 在与 webui 相同的位置创建 `interrogate` 目录
- 将文本文件放入其中，每行都有相关描述

有关要使用的文本文件的示例，请参阅 https://github.com/pharmapsychotic/clip-interrogator/tree/main/data。
事实上，您可以从那里获取文件并使用它们 - 只需跳过 artists.txt 因为您已经有了一个列表
`artists.csv` 中的艺术家（或者也使用它，谁会阻止你）。每个文件在最终描述中添加一行文本。
如果您添加“.top3”。到文件名，例如 `flavors.top3.txt`，该文件中最相关的三行将是
添加到提示中（其他号码也可以）。

有与此功能相关的设置：
- `Interrogate: keep models in VRAM` - 请勿在使用后从内存中卸载 Interrogate 模型。对于具有大量 VRAM 的用户。
- `Interrogate: use artists from artists.csv` - 在询问时添加来自 `artists.csv` 的艺术家。当你在 interrogate 目录中有你的艺术家列表时，禁用它可能很有用
- `Interrogate: num_beams for BLIP` - 影响 BLIP 模型详细描述的参数（生成提示的第一部分）
- `Interrogate: minimum description length` - BLIP 模型文本的最小长度
- `Interrogate: maximum descripton length` - BLIP 模型文本的最大长度
- `Interrogate: text file 中的最大行数` - interrogator 将只考虑文件中这么多的第一行。设置为 0，默认为 1500，大约是 4GB 视频卡可以处理的量。

# 快速编辑

![xy_grid-0022-646033397](https://user-images.githubusercontent.com/20920490/190426933-9748708b-6db0-4cb0-8cb9-3285053916b8.jpg)

即时编辑允许您开始对一张图片进行采样，但在中间切换到其他图片。其基本语法是：

```
[from:to:when]
```

其中“from”和“to”是任意文本，“when”是一个数字，它定义了应该在采样周期的多晚进行切换。越晚，模型绘制“to”文本代替“from”文本的能力就越小。如果“when”是一个介于 0 和 1 之间的数字，则它是进行切换之前的步数的一小部分。如果它是一个大于零的整数，它就是进行切换之前的步骤。

将一个提示编辑嵌套在另一个提示编辑中确实有效。

此外：
- `[to:when]` - 在固定数量的步骤后将 `to` 添加到提示中（`when`）
- `[from::when]` - 在固定步数（`when`）后从提示中删除 `from`

例子：
`[幻想：赛博朋克：16]风景`

- 开始时，模型将绘制“幻想风景”。
- 在第 16 步之后，它将切换到绘制“赛博朋克风景”，从它停止的地方继续幻想。

这是一个包含多个编辑的更复杂的示例：
`带有 [mountain:lake:0.25] 和 [an oak:a christmas tree:0.75][ 前景 ::0.6][ 背景 0.25] [shoddy:masterful:0.5] 的奇幻风景`（采样器有 100 个步骤）

- 开始时，“前景中有一座山和一棵橡树的奇幻风景”
- 在第 25 步之后，“前景中有一个湖泊和一棵橡树的奇幻风景，背景很差”
- 在第 50 步之后，“前景中有一个湖泊和一棵橡树的奇幻风景非常棒”
- 在第 60 步之后，“以湖泊和橡树为背景的奇幻景观精湛”
- 在第 75 步之后，“背景中有湖泊和一棵圣诞树的奇幻景观精湛”

顶部的图片是根据提示制作的：

`微笑的第二次世界大战将军的官方肖像，[男：女：0.99]，开朗，快乐，详细的脸，20 世纪，高度详细，电影照明，Greg Rutkowski 的数字艺术绘画

数字 0.99 将替换为您在图像的列标签中看到的任何内容。

图片最后一列是[male:female:0.0]，这本质上是让模型从头开始画女性，而不是从男性将军开始，这就是为什么它看起来与其他人如此不同。

## 交替词

每隔一步交换的方便语法。

[牛|马]在田野里

在第 1 步中，提示是“田间的奶牛”。第 2 步是“田野里的马”。第 3 步是“田野里的奶牛”，依此类推。

![交替词](https://user-images.githubusercontent.com/39339941/197556926-49ceb72b-daf3-4208-86f3-c2e7e9cd775a.gif)




请参阅下面的更高级示例。在第 8 步，链条从“人”循环回到“牛”。

[牛|牛|马|人|东北虎|牛|人]在田野里

提示编辑首先由 Doggettx 在 [this myspace.com post](https://www.reddit.com/r/StableDiffusion/comments/xas2os/simple_prompt2prompt_implementation_with_prompt/) 中实现。

＃ 高分辨率。使固定
一个方便的选项，可以以较低的分辨率部分渲染您的图像，放大它，然后以高分辨率添加细节。默认情况下，txt2img 以非常高的分辨率制作可怕的图像，这使得避免使用小图片的构图成为可能。通过选中 txt2img 页面上的“Highres.fix”复选框启用。

|没有|与|
|-------------------------------|---------------------------------|

| ![00262-836728130](https://user-images.githubusercontent.com/20920490/191177752-ad983e62-8e1c-4197-8f3b-3165a6a6c31d.png) | ![00261-836728130](https://user-images.githubusercontent.com/20920490/191177785-395a951e-0d2e-4db7-9645-4c5af9321772.png) |
| ![00345-950170121](https://user-images.githubusercontent.com/20920490/191178018-25dcd98d-6c45-4c31-ab7a-3de6c51c52e3.png) | ![00341-950170121](https://user-images.githubusercontent.com/20920490/191178048-3eba3db4-e5be-4617-9bfe-2cb36cebaafc.png) |

# 可组合扩散

允许组合多个提示的方法。
使用大写字母 AND 组合提示

一只猫和一只狗

支持提示权重：`a cat :1.2 AND a dog AND a penguin :2.2`
默认权重值为 1。
将多个嵌入组合到结果中可能非常有用：`creature_embedding in the woods:0.7 AND arcane_embedding:0.5 AND glitch_embedding:0.2`

使用低于 0.1 的值几乎没有效果。 `a cat AND a dog:0.03` 将产生与 `a cat` 基本相同的输出

通过继续将更多提示附加到您的总数，这对于生成微调的递归变体可能很方便。 `log 上的 creature_embedding AND frog:0.13 AND yellow eyes:0.08`


＃ 打断

按中断按钮停止当前处理。

# 4GB 显卡支持
针对具有低 VRAM 的 GPU 的优化。这应该可以在具有 4GB 内存的视频卡上生成 512x512 图像。

`--lowvram` 是 [basujindal](https://github.com/basujindal/stable-diffusion) 优化思想的重新实现。
模型被分成模块，GPU内存中只保留一个模块；当另一个模块需要运行时，前一个
从 GPU 内存中删除。这种优化的本质使处理运行得更慢——大约慢 10 倍
与我的 RTX 3090 上的正常操作相比。

`--medvram` 是另一个优化，应该通过不处理条件和显着减少 VRAM 使用
同一批次无条件去噪。

这种优化的实现不需要对原始的稳定扩散代码进行任何修改。

# 人脸修复
让您使用 GFPGAN 或 CodeFormer 改善图片中的人脸。每个选项卡中都有一个复选框来使用面部修复，
还有一个单独的选项卡，只允许您在任何图片上使用面部修复，并带有一个滑块来控制可见度
效果是。您可以在设置中选择这两种方法。

|原创 | GFPGAN |代码形成者 |
|-------------------------|--------------------------------|------------------------------------|

| ![](图片/facefix.png) | ![](图片/facefix-gfpgan.png) | ![](图片/facefix-codeformer.png) |


# 保存
单击输出部分下的保存按钮，生成的图像将保存到设置中指定的目录中；
生成参数将附加到同一目录中的 csv 文件。

# 加载中
Gradio 的加载图形对神经网络的处理速度有非常不利的影响。
当带渐变的选项卡未处于活动状态时，我的 RTX 3090 使图像速度提高约 10%。默认情况下，用户界面
现在隐藏加载进度动画并将其替换为静态“正在加载...”文本，从而实现
同样的效果。使用 `--no-progressbar-hiding` 命令行选项来恢复它并显示加载动画。

# 提示验证
Stable Diffusion 对输入文本长度有限制。如果你的提示太长，你会得到一个
文本输出字段中的警告，显示文本的哪些部分被模型截断和忽略。

# PNG 信息
将有关生成参数的信息作为文本块添加到 PNG。你
以后可以使用任何支持查看的软件查看此信息
PNG 块信息，例如：https://www.nayuki.io/page/png-file-chunk-inspector

# 设置
带有设置的选项卡，允许您使用 UI 编辑以前无法编辑的一半以上的参数
是命令行。设置保存到 config.js 文件。保留为命令行的设置
选项是启动时需要的选项。

# 文件名格式
“设置”选项卡中的“图像文件名模式”字段允许自定义生成的 txt2img 和 img2img 图像文件名。此模式定义了要包含在文件名中的生成参数及其顺序。支持的标签是：

`[steps], [cfg], [prompt], [prompt_no_styles], [prompt_spaces], [width], [height], [styles], [sampler], [seed], [model_hash], [prompt_words], [日期], [日期时间], [job_timestamp].`

这个列表会随着新的添加而发展。您可以通过将鼠标悬停在 UI 中的“图像文件名模式”标签上来获取最新的支持标签列表。

模式示例：`[seed]-[steps]-[cfg]-[sampler]-[prompt_spaces]`

关于“提示”标签的注意事项：`[prompt]` 将在提示词之间添加下划线，而 `[prompt_spaces]` 将保持提示完整（更容易再次复制/粘贴到 UI 中）。 `[prompt_words]` 是您的提示的简化和清理版本，已用于生成子目录名称，仅包含您的提示文字（无标点符号）。

如果将此字段留空，将应用默认模式 (`[seed]-[prompt_spaces]`)。

请注意，标签实际上在模式内部被替换了。这意味着您还可以向此模式添加非标签词，以使文件名更加明确。例如：`s=[seed],p=[prompt_spaces]`

# 用户脚本
如果程序使用 `--allow-code` 选项启动，脚本代码的额外文本输入字段
位于页面底部的脚本 -> 自定义代码下。它允许你输入python
将处理图像的代码。

在代码中，使用“p”变量从 Web UI 访问参数，并为 Web UI 提供输出
使用 `display(images, seed, info)` 函数。脚本中的所有全局变量也可以访问。

一个简单的脚本，只处理图像并正常输出：

```python
import modules.processing

processed = modules.processing.process_images(p)

print("Seed was: " + str(processed.seed))

display(processed.images, processed.seed, processed.info)
```

# 界面配置
您可以更改 UI 元素的参数：
- 无线电组：默认选择
- 滑块：默认值、最小值、最大值、步长
- 复选框：选中状态
- 文本和数字输入：默认值

该文件是 webui 目录下的 ui-config.json ，如果程序启动时没有，它会自动创建。

通常会展开隐藏部分的复选框在设置为 UI 配置条目时最初不会这样做。

某些设置会中断处理，例如宽度和高度不能被 64 整除的步长，以及某些设置，例如更改默认设置
img2img 选项卡上的功能，可能会破坏 UI。我没有计划在不久的将来解决这些问题。

#ESRGAN
可以在 Extras 选项卡以及 SD 高档中使用 ESRGAN 模型。

要使用 ESRGAN 模型，请将它们放入与 webui.py 相同位置的 ESRGAN 目录中。
如果文件具有 .pth 扩展名，则该文件将作为模型加载。从 [模型数据库](https://upscale.wiki/wiki/Model_Database) 中获取模型。

并非数据库中的所有模型都受支持。很可能不支持所有 2x 模型。

# img2img 替代测试
使用 Euler 扩散器的反向解构输入图像，以创建用于构建输入提示的噪声模式。

例如，您可以使用此图像。从 *scripts* 部分选择 img2img 替代测试。

![alt_src](https://user-images.githubusercontent.com/1633844/191771623-6293ec7b-c1c0-425c-9fe9-9d03313761fb.png)

调整重建过程的设置：
- 使用场景的简短描述：“一个棕色头发的微笑女人。”描述您要更改的功能会有所帮助。将其设置为您的启动提示，并在脚本设置中设置“原始输入提示”。
- 你*必须*使用欧拉采样方法，因为这个脚本是建立在它之上的。
- 采样步数：50-60。这与脚本中的解码步骤值非常匹配，否则您会遇到麻烦。在此演示中使用 50。
- CFG 等级：2 或更低。对于此演示，请使用 1.8。 （提示，您可以编辑 ui-config.json 将“img2img/CFG Scale/step”更改为 .1 而不是 .5。
- 去噪强度 - 这*确实*重要，与旧文档所说的相反。将其设置为 1。
- 宽度/高度 - 使用输入图像的宽度/高度。
- 种子......你可以忽略这个。反向欧拉现在正在为图像生成噪声。
- 解码 cfg 比例 - 低于 1 的地方是最佳点。对于演示，使用 1。
- 解码步骤 - 如上所述，这应该与您的采样步骤相匹配。 50 用于演示，考虑增加到 60 以获得更详细的图像。

拨入以上所有内容后，您应该能够点击“生成”并返回一个*非常*接近原始结果的结果。

在验证脚本以良好的准确度重新生成源照片后，您可以尝试更改提示的详细信息。原始图像的较大变化可能会导致图像的构图与源图像完全不同。

使用上述设置和下面提示的示例输出（图中未显示红头发/小马）

![演示](https://user-images.githubusercontent.com/1633844/191776138-c77bf232-1981-47c9-a4d3-ae155631f5c8.png)

“一个微笑的蓝头发女人。”作品。
“一个皱着眉头的棕色头发的女人。”作品。
“一个皱着眉头的红头发女人。”作品。
“一个皱着眉头的红发女子骑着马。”似乎完全取代了女人，现在我们有了一匹姜黄色的小马。

# 用户.css
在 `webui.py` 附近创建一个名为 `user.css` 的文件，并将自定义 CSS 代码放入其中。例如，这会使画廊更高：

```css
#txt2img_gallery, #img2img_gallery{
    min-height: 768px;
}
```
一个有用的提示是您可以将 `/?__theme=dark` 附加到您的 webui url 以启用内置的 *dark 主题*
<br>例如(`http://127.0.0.1:7860/?__theme=dark`)

或者，您可以将 `--theme=dark` 添加到 `webui-user.bat` 中的 `set COMMANDLINE_ARGS=`<br>
例如`set COMMANDLINE_ARGS=--theme=dark`


![chrome_O1kvfKs1es](https://user-images.githubusercontent.com/39339941/197560013-51e535d6-7cef-4946-ab6b-747e1c76b007.png)

# 通知.mp3
如果名为 notification.mp3 的音频文件存在于 webui 的根文件夹中，它将在生成过程完成时播放。

作为灵感来源：
* https://pixabay.com/sound-effects/search/ding/?duration=0-30
* https://pixabay.com/sound-effects/search/notification/?duration=0-30

# 调整

## 忽略 CLIP 模型的最后一层
这是设置中的一个滑块，它控制 CLIP 网络处理提示的时间应该多早停止。

更详细的解释：

CLIP 是一种非常先进的神经网络，可将您的提示文本转换为数字表示。神经网络可以很好地处理这种数字表示，这就是为什么 SD 的开发者选择 CLIP 作为稳定扩散图像生成方法中涉及的 3 个模型之一的原因。由于 CLIP 是一个神经网络，这意味着它有很多层。您的提示以简单的方式数字化，然后通过层馈送。您在第一层之后获得提示的数字表示，将其提供给第二层，将其结果提供给第三层，依此类推，直到到达最后一层，这就是稳定版中使用的 CLIP 的输出扩散。这是 1 的滑块值。但是您可以提前停止，并使用倒数第二层的输出 - 这是 2 的滑块值。您停止得越早，处理提示的神经网络层数就越少。

一些模型是通过这种调整进行训练的，因此设置此值有助于在这些模型上产生更好的结果。
