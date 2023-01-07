---
title: 自定义脚本
layout: post
category: Guides
permalink: /custom-scripts/
machine_translated: true
lang: cn
toc: true
---
# 安装和使用自定义脚本

要安装自定义脚本，请将它们放入 `scripts` 目录，然后单击设置选项卡底部的 `Reload custom script` 按钮。安装后，自定义脚本将出现在 txt2img 和 img2img 选项卡左下角的下拉菜单中。以下是 Web UI 用户创建的一些著名的自定义脚本：

# 来自用户的自定义脚本

## 改进的提示矩阵

<https://github.com/ArrowM/auto1111-improved-prompt-matrix>

此脚本是 [advanced-prompt-matrix](https://github.com/GRMrGecko/stable-diffusion-webui-automatic/blob/advanced_matrix/scripts/advanced_prompt_matrix.py) 修改后支持“批次计数”。不创建网格。

**用法：**

使用 `<` `>` 创建一组替代文本。使用“|”分隔文本选项。可以使用多个组和多个选项。例如：

`a <corgi|cat> wearing <goggles|a hat>` 的输入
会输出4个提示：`a corgi wearing goggles`, `a corgi wearing a hat`, `a cat wearing goggles`, `a cat wearing a hat`

当使用 `batch count` > 1 时，将为每个种子生成每个提示变体。 `batch size` 被忽略。

## txt2img2img

<https://github.com/ThereforeGames/txt2img2img>

极大地提高任何角色/主题的可编辑性，同时保留他们的相似性。该脚本的主要动机是提高通过 [Textual Inversion](https://textual-inversion.github.io/) 创建的嵌入的可编辑性。

（小心克隆，因为它签入了一些 venv）

<img src="https://user-images.githubusercontent.com/98228077/200106431-21a22657-db24-4e9c-b7fa-e3a8e9096b89.png" width="302" />


## txt2掩码

<https://github.com/ThereforeGames/txt2mask>

允许您指定带有文本的修复蒙版，而不是画笔。

<img src="https://user-images.githubusercontent.com/95403634/190878562-d020887c-ccb0-411c-ab37-38e2115552eb.png" width="302" />


## 蒙版绘图界面
<https://github.com/dfaker/stable-diffusion-webui-cv2-external-masking-script>

提供由 CV2 提供支持的本地弹出窗口，允许在处理之前添加掩码。

<img src="https://user-images.githubusercontent.com/98228077/200109495-3d6741f1-0e25-4ae5-9f84-d93f886f302a.png" width="302" height="312" />


## Img2img 视频
<https://github.com/memes-forever/Stable-diffusion-webui-video>

使用img2img，生成一张张图片。

<video width="320" height="240" 控件>
<source src="https://user-images.githubusercontent.com/107195976/191963848-6eb8e169-dee3-46d7-8310-db45046353fd.mp4" type="video/mp4">
</视频>

## 种子旅行

<https://github.com/yownas/seed_travel>

选择两个（或更多）种子并生成一系列在它们之间插值的图像。或者，让它创建结果的视频。

你可以用它做什么的例子：

https://www.youtube.com/watch?v=4c71iUclY4U

<video width="320" height="240" 控件>
<source src="https://user-images.githubusercontent.com/98228077/192487018-06e1b86a-8763-4e8c-906b-273754f161cd.mp4" type="video/mp4">
</视频>

## 高级种子混合

<https://github.com/amotile/stable-diffusion-backend/tree/master/src/process/implementations/automatic1111_scripts>

此脚本允许您将初始噪声基于多个加权种子。

前任。 `seed1:2, seed2:1, seed3:1`

权重被归一化，所以你可以像上面那样使用更大的一次，或者你可以做浮点数：

前任。 `seed1:0.5, seed2:0.25, seed3:0.25`

## 快速混合

<https://github.com/amotile/stable-diffusion-backend/tree/master/src/process/implementations/automatic1111_scripts>

该脚本允许您在生成图像之前通过数学组合文本嵌入来将多个加权提示组合在一起。

前任。

`含有元素{火|冰}的水晶`

它支持嵌套定义，因此您也可以这样做：

`含有元素fire:5|ice|earth的水晶`

## 动画师

<https://github.com/Animator-Anon/Animator>

一个基本的 img2img 脚本，它将转储帧并构建视频文件。适合在扭曲电影中创建有趣的缩放，但此时其他不多。

## 参数序列器

<https://github.com/rewbs/sd-parseq>

通过对许多 Stable Diffusion 参数（例如种子、比例、提示权重、去噪强度...）以及输入处理参数（例如缩放、平移、3D 旋转...）进行严格控制和灵活插值来生成视频

## 备用噪声时间表

<https://gist.github.com/dfaker/f88aa62e3a14b559fe4e5f6b345db664>

为采样器的西格玛计划使用备用生成器。

允许从 crowsonkb/k-diffusion 访问 Karras、指数和方差保持计划及其参数。

## 视频对视频

<https://github.com/Filarius/stable-diffusion-webui/blob/master/scripts/vid2vid.py>

从真实视频中，img2img 帧并将它们拼接在一起。不将帧解压缩到硬盘驱动器。

## Txt2VectorGraphics

<https://github.com/GeorgLegato/Txt2Vectorgraphics>

根据您的提示创建自定义、可缩放的图标，如 SVG 或 PDF。


|提示 |PNG |SVG |
| :--------  | :-----------------: | :---------------------: |

| Happy Einstein | <img src="https://user-images.githubusercontent.com/7210708/193370360-506eb6b5-4fa7-4b2a-9fec-6430f6d027f5.png" width="40%" /> | <img src="https://user-images.githubusercontent.com/7210708/193370379-2680aa2a-f460-44e7-9c4e-592cf096de71.svg" width="30%"/> |

| Mountainbike Downhill | <img src="https://user-images.githubusercontent.com/7210708/193371353-f0f5ff6f-12f7-423b-a481-f9bd119631dd.png" width="40%"/> | <img src="https://user-images.githubusercontent.com/7210708/193371585-68dea4ca-6c1a-4d31-965d-c1b5f145bb6f.svg" width="30%"/> |

coffe mug in shape of a heart | <img src="https://user-images.githubusercontent.com/7210708/193374299-98379ca1-3106-4ceb-bcd3-fa129e30817a.png" width="40%"/> | <img src="https://user-images.githubusercontent.com/7210708/193374525-460395af-9588-476e-bcf6-6a8ad426be8e.svg" width="30%"/> |

| Headphones | <img src="https://user-images.githubusercontent.com/7210708/193376238-5c4d4a8f-1f06-4ba4-b780-d2fa2e794eda.png" width="40%"/> | <img src="https://user-images.githubusercontent.com/7210708/193376255-80e25271-6313-4bff-a98e-ba3ae48538ca.svg" width="30%"/> |



## 转移注意力

<https://github.com/yownas/shift-attention>

在提示中生成一系列图像来转移注意力。

此脚本使您能够在提示中为令牌的权重指定一个范围，然后生成从第一个到第二个的一系列图像。

## 环回和叠加
<https://github.com/DiceOwl/StableDiffusionStuff>

<https://github.com/DiceOwl/StableDiffusionStuff/blob/main/loopback_superimpose.py>

将 img2img 的输出与强度 alpha 的原始输入图像混合。结果再次输入 img2img（在 loop>=2），并重复此过程。倾向于锐化图像，提高一致性，减少创造力并减少精细细节。

## 插值
<https://github.com/DiceOwl/StableDiffusionStuff>

<https://github.com/DiceOwl/StableDiffusionStuff/blob/main/interpolate.py>

用于生成中间图像的 img2img 脚本。允许两个输入图像进行插值。 [自述文件](https://github.com/DiceOwl/StableDiffusionStuff) 中显示了更多功能。

## 运行n次

<https://gist.github.com/camenduru/9ec5f8141db9902e375967e93250860f>

使用随机种子运行 n 次。

## 高级环回

<https://github.com/Extraltodeus/advanced-loopback-for-sd-webui>

具有参数变化和快速切换等功能的动态缩放环回！

## 提示变形

<https://github.com/feffy380/prompt-morph>

使用 Stable Diffusion 生成变形序列。在两个或多个提示之间进行插值，并在每个步骤中创建一个图像。

使用新的 AND 关键字，并且可以选择将序列导出为视频。

##提示插值

<https://github.com/EugeoSynthesisThirtyTwo/prompt-interpolation-script-for-sd-webui>

使用此脚本，您可以在两个提示之间插入（使用“AND”关键字），生成任意数量的图像。
您还可以生成带有结果的 gif。适用于 txt2img 和 img2img。


![gif](https://user-images.githubusercontent.com/24735555/195470874-afc3dfdc-7b35-4b23-9c34-5888a4100ac1.gif)


## 不对称平铺

<https://github.com/tjm35/asymmetric-tiling-sd-webui/>

相互独立地控制水平/垂直无缝平铺。

<img src="https://user-images.githubusercontent.com/19196175/195132862-8c050327-92f3-44a4-9c02-0f11cce0b609.png" width="624" height="312" />


## 力对称
https://gist.github.com/1ort/2fe6214cf1abe4c07087aac8d91d0d8a

请参阅 https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/2441

每 n 步对图像应用对称并将结果进一步发送到 img2img。

<img src="https://user-images.githubusercontent.com/83316072/196016119-0a03664b-c3e4-49f0-81ac-a9e719b24bd1.png" width="624" height="312" />


## SD 潜在镜像

<https://github.com/dfaker/SD-latent-mirroring>

对潜像应用镜像和翻转以产生从微妙的平衡构图到完美反射的任何东西

<img src="https://user-images.githubusercontent.com/35278260/199627881-6f62a227-3a6c-4470-9c18-2ed8bc57194c.png" width="624" height="312" />


## txt2调色板

<https://github.com/1ort/txt2palette>

通过文本描述生成调色板。此脚本获取生成的图像并将它们转换为调色板。

<img src="https://user-images.githubusercontent.com/83316072/199360686-62f0f5ec-ed3d-4c0f-95b4-af9c67d1e248.png" width="352" height="312" />



## 样式箭头

<https://github.com/some9000/StylePile>

一种将元素混合和匹配到影响结果样式的提示的简单方法。
<img src="https://user-images.githubusercontent.com/17021558/199468444-99e78027-1889-4bec-b97b-25f801e33c0a.jpg" width="960" height="120" />


## XYZ 绘图脚本

<https://github.com/xrpgame/xyz_plot_script>

生成一个 .html 文件以交互方式浏览图像集。使用滚轮或箭头键在 Z 维度中移动。

<img src="https://raw.githubusercontent.com/xrpgame/xyz_plot_script/master/example1.png" width="522" height="312" />


## xyz-plot-grid

<https://github.com/Gerschel/xyz-plot-grid>

将 xyz_grid.py 与其他脚本一起放在脚本文件夹中。
像 x/y 图一样工作，就像您期望的那样，但现在有一个 z。就像您期望的那样工作，还有网格图例。

<img src="https://github.com/Gerschel/xyz-plot-grid/raw/main/000.png" width="574" height="390" />


## 扩展 XY 网格

<https://github.com/0xALIVEBEEF/Expanded-XY-grid>

AUTOMATIC1111 的 stable-diffusion-webui 的自定义脚本，它向标准 xy 网格添加了更多功能：

- 多工具：允许在一个轴上使用多个参数，理论上允许在一个 xy 网格中调整无限个参数

- 可定制的提示矩阵

- 目录中的组文件

- S/R 占位符 - 用所需值替换占位符值（参数列表中的第一个值）。

- 添加 PNGinfo 到网格图像


<img src="https://user-images.githubusercontent.com/80003301/202277871-a4a3341b-13f7-42f4-a3e6-ca8f8cd8250a.png" width="574" height="197" />


示例图像：提示：“达斯·维达骑自行车，修改器”； X：Multitool：“提示 S/R：自行车、摩托车 | CFG 比例：7.5、10 | 提示 S/R 占位符：修饰符、4k、artstation”； Y: Multitool: "Sampler: Euler, Euler a | Steps: 20, 50"




## Booru 标签自动补全

<https://github.com/DominikDoom/a1111-sd-webui-tagcomplete>

显示来自“image booru”板（例如 Danbooru）的标签的自动完成提示。使用本地标记 CSV 文件并包含用于自定义的配置。

还支持完成 [wildcards](https://github.com/adieyal/sd-dynamic-prompts#wildcard-files)

## 嵌入到 PNG

<https://github.com/dfaker/embedding-to-png-script>

将现有嵌入转换为可共享的图像版本。

<img src="https://user-images.githubusercontent.com/35278260/196052398-268a3a3e-0fad-46cd-b37d-9808480ceb18.png" width="263" height="256" />


## 阿尔法画布

<https://github.com/TKoestlerx/sdexperiments>

涂刷一个区域。 Infinite outpainting 概念，使用 AUTOMATIC1111 repo 中的两个现有 outpainting 脚本作为基础。

<img src="https://user-images.githubusercontent.com/86352149/199517938-3430170b-adca-487c-992b-eb89b3b63681.jpg" width="446" height="312" />


## 随机网格

<https://github.com/lilly1987/AI-WEBUI-scripts-Random>

随机输入 xy 网格值。

<img src="https://user-images.githubusercontent.com/20321215/197346726-f93b7e84-f808-4167-9969-dc42763eeff1.png" width="198" height="312" />


基本逻辑与x/y plot相同，只是在内部，x type固定为step，type y固定为cfg。
在 step1|2 值 (10-30) 范围内生成与步数 (10) 一样多的 x 值
在 cfg1|2 值 (6-15) 范围内生成与 cfg 计数 (10) 一样多的 x 值
即使您将 1|2 范围上限倒置，它也会自动更改。
在cfg值的情况下，将其视为int类型，不读取十进制值。

＃＃ 随机的

<https://github.com/lilly1987/AI-WEBUI-scripts-Random>

在没有网格的情况下重复简单的次数。

<img src="https://user-images.githubusercontent.com/20321215/197346617-0ed1cd09-0ddd-48ad-8161-bc1540d628ad.png" width="258" height="312" />


## 稳定扩散美学评分器

<https://github.com/grexzen/SD-Chad>

评价你的图像。

## img2tiles

<https://github.com/arcanite24/img2tiles>

从基本图像生成图块。基于 SD 高档脚本。

<img src="https://github.com/arcanite24/img2tiles/raw/master/examples/example5.png" width="312" height="312" />


## img2mosiac

<https://github.com/1ort/img2mosaic>

从图像生成马赛克。该脚本将图像切割成图块并分别处理每个图块。每个图块的大小是随机选择的。

<img src="https://user-images.githubusercontent.com/83316072/200170569-0e7131e4-1da8-4caf-9cd9-5b785c9d21b0.png" width="758" height="312" />


## 深度图

<https://github.com/thygate/stable-diffusion-webui-depthmap-script>

此脚本是 [AUTOMATIC1111 的稳定扩散 Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 的插件，可根据生成的图像创建“深度图”。结果可以在 3D 或全息设备（如 VR 耳机或 [lookingglass](https://lookingglassfactory.com/) 显示器）上查看，在带有位移修改器的平面上用于渲染或游戏引擎，甚至可以 3D 打印.

<img src="https://github.com/thygate/stable-diffusion-webui-depthmap-script/raw/main/examples.png" width="780" height="312" />


## 测试我的提示

<https://github.com/Extraltodeus/test_my_prompt>

您是否曾经使用过很长的提示词，但您不确定是否会对您的形象产生任何实际影响？您是否失去了尝试将它们一一移除以测试它们的效果是否值得您强大的 GPU 的勇气？

好吧，现在您不需要任何勇气，因为这个脚本已经为您量身定做！

它会生成与提示中的单词一样多的图像（当然，您可以选择分隔符）。


这里的提示很简单：“**banana, on fire, snow**”，正如您所看到的，它生成了每张图像，但其中没有任何描述。

<img src="https://user-images.githubusercontent.com/15731540/200349119-e45d3cfb-39f0-4999-a8f0-4671a6393824.png" width="512" height="512" />


您还可以测试您的否定提示。


## 像素艺术

<https://github.com/C10udburst/stable-diffusion-webui-scripts>

通过可变数量调整图像大小的简单脚本，还将图像转换为使用给定大小的调色板。


|已禁用 |已启用 x8，没有调整大小，没有调色板 |启用 x8，无调色板 |已启用 x8、16 调色板 |
| :---: | :---: | :---: | :---: |

|![预览](https://user-images.githubusercontent.com/18114966/201491785-e30cfa9d-c850-4853-98b8-11db8de78c8d.png) | ![预览](https://user-images.githubusercontent.com/18114966/201492204-f4303694-e98d-4ea3-8256-538a88ea26b6.png) | ![预览](https://user-images.githubusercontent.com/18114966/201491864-d0c0c9f1-e34f-4cb6-a68e-7043ec5ce74e.png) | ![预览](https://user-images.githubusercontent.com/18114966/201492175-c55fa260-a17d-47c9-a919-9116e1caa8fe.png) |

[使用的模型](https://publicprompts.art/all-in-one-pixel-art-dreambooth-model/)
```text
japanese pagoda with blossoming cherry trees, full body game asset, in pixelsprite style
Steps: 20, Sampler: DDIM, CFG scale: 7, Seed: 4288895889, Size: 512x512, Model hash: 916ea38c, Batch size: 4
```


## 多个超网络
<https://github.com/antis0007/sd-webui-multiple-hypernetworks>

添加一次应用多个超网络的能力。覆盖劫持、优化和 CrossAttention 前向函数，以便顺序应用具有不同权重的多个超网络。

## 超网络结构（.hns）/变量丢失/猴子补丁
<https://github.com/aria1th/Hypernetwork-MonkeyPatch-Extension>

添加应用超网络结构的能力，如在 .hns 文件中定义的那样。有关详细信息，请参阅[此处](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/4334)。

添加使用适当的可变丢失率的能力，例如 0.05。还修复了训练后立即使用超网络的问题。

添加创建 beta-hypernetwork（dropout）和 beta-training，它允许自动余弦退火和原始图像的无裁剪使用。

## 配置预设
<https://github.com/Zyin055/Config-Presets-Script-OLD>

使用可配置的预设值下拉列表快速更改 txt2img 和 img2img 选项卡中的设置。


<img src="https://camo.githubusercontent.com/fd878bf6e95b5b4d4bc95e1aef7d3253a5cd3832c65e97de942455572ee3e561/68747470733a2f2f692e696d6775722e636f6d2f4231654d5741772e6a7067" width="512" height="146" />




## 采样过程的保存步骤

该脚本会将采样过程的步骤保存到一个目录中。
```python
import os.path

import modules.scripts as scripts
import gradio as gr

from modules import sd_samplers, shared
from modules.processing import Processed, process_images


class Script(scripts.Script):
    def title(self):
        return "Save steps of the sampling process to files"

    def ui(self, is_img2img):
        path = gr.Textbox(label="Save images to path")
        return [path]

    def run(self, p, path):
        index = [0]

        def store_latent(x):
            image = shared.state.current_image = sd_samplers.sample_to_image(x)
            image.save(os.path.join(path, f"sample-{index[0]:05}.png"))
            index[0] += 1
            fun(x)

        fun = sd_samplers.store_latent
        sd_samplers.store_latent = store_latent

        try:
            proc = process_images(p)
        finally:
            sd_samplers.store_latent = fun

        return Processed(p, proc.images, p.seed, "")
```
