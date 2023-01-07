---
title: 优化
layout: post
category: Guides
permalink: /optimizations/
machine_translated: true
lang: cn
---
[命令行参数](Run-with-Custom-Parameters) 可以启用一些优化：

| commandline argument           | explanation                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| `--xformers` |使用 [xformers](https://github.com/facebookresearch/xformers) 库。显着改善内存消耗和速度。 Windows 版本安装由 [C43H66N12O12S2](https://github.com/C43H66N12O12S2/stable-diffusion-webui/releases) 维护的二进制文件。只会在一小部分配置上启用，因为这就是我们拥有二进制文件的目的。 [文档](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Xformers) |
| `--force-enable-xformers` |无论程序是否认为您可以运行它，都启用上面的 xformers。不要报告你运行这个的错误。 |
| `--opt-split-attention` |交叉注意层优化显着减少了内存使用，几乎没有成本（一些报告提高了性能）。黑魔法。 <br/>默认情况下为 `torch.cuda` 打开，其中包括 NVidia 和 AMD 卡。 |
| `--disable-opt-split-attention` | Disables the optimization above.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--opt-split-attention-v1` |使用上面优化的旧版本，它不会占用大量内存（它会使用更少的 VRAM，但会更多地限制您可以制作的图片的最大尺寸）。 |
| `--medvram` |通过将 Stable Diffusion 模型分成三部分 - cond（用于将文本转换为数字表示）、first_stage（用于将图片转换为潜在空间并返回）和 unet（用于潜在空间的实际去噪）并制作这样一来，始终只有一个在 VRAM 中，而将其他的发送到 CPU RAM。会降低性能，但只会降低一点——除非启用了实时预览。 |
| `--lowvram` |对上面更彻底的优化，将unet拆分成很多模块，VRAM中只保留一个模块。对性能具有破坏性。 |
| `*不要批处理条件未处理` |防止在采样期间对正负提示进行批处理，这实际上可以让您以 0.5 的批处理大小运行，从而节省大量内存。降低性能。不是命令行选项，而是使用“--medvram”或​​“--lowvram”隐式启用的优化。 |
| `--always-batch-cond-uncond` |禁用上面的优化。只有与 `--medvram` 或 `--lowvram` 一起使用才有意义 |
| `--opt-channelslast`           | Changes torch memory type for stable diffusion to channels last. Effects not closely studied.                                                                                                                                                                                                                                                                                                                                        |


额外提示（Windows）：
- https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/3889 禁用硬件 GPU 调度。
- 禁用浏览器硬件加速
- 进入 nvidia 控制面板，3d 参数，并将电源配置文件更改为“最大性能”
