---
title: 依赖关系
layout: post
category: Getting started
permalink: /dependencies/
machine_translated: true
lang: cn
---
1. Python 3.10.6 和 Git：
- Windows：下载并运行 Python 3.10.6 的安装程序（[网页](https://www.python.org/downloads/release/python-3106/)、[exe](https://www.python.org /ftp/python/3.10.6/python-3.10.6-amd64.exe)，或[win7版本](https://github.com/adang1345/PythonWin7/raw/master/3.10.6/python-3.10. 6-amd64-full.exe)) 和 git ([网页](https://git-scm.com/download/win))
- Linux（基于 Debian）：`sudo apt install wget git python3 python3-venv`
- Linux（基于 Red Hat）：`sudo dnf install wget git python3`
- Linux（基于 Arch）：`sudo pacman -S wget git python3`
2. 来自这个存储库的代码：
- 首选方式：使用 git：`git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`。
- 之所以提到这种方式，是因为它让您只需运行 `git pull` 即可更新。
- 这些命令可以在您右键单击资源管理器并选择“Git Bash here”后打开的命令行窗口中使用。
- 替代方法：使用回购主页上的“代码”（绿色按钮）->“下载 ZIP”选项。
- 即使你选择了这个，你仍然需要安装 git。
- 要更新，您必须再次下载 zip 并替换文件。
3. Stable Diffusion模型检查点，一个扩展名为.ckpt的文件，需要下载并放在models/Stable-diffusion目录下。
- [官方下载](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original)
- [文件存储](https://drive.yerf.org/wl/?id=EBfTrmcCCUAGaQBXVIj5lJmEhjoP1tgl)
- 洪流 (磁铁:?xt=urn:btih:3a4a612d75ed088ea542acac52f9f45987488d1c&dn=sd-v1-4.ckpt&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org% 3a1337)

# 可选依赖

## ESRGAN（升级）
ESRGAN 模型，例如来自 [模型数据库](https://upscale.wiki/wiki/Model_Database) 的模型，可以放置在 ESRGAN 目录中。
如果文件具有 .pth 扩展名，它将作为模型加载，并且会在 UI 中显示其名称。

> 注意：RealESRGAN 模型不是 ESRGAN 模型，它们不兼容。不要下载 RealESRGAN 模型。不要将 RealESRGAN 放入包含 ESRGAN 模型的目录中。

## sd 2.x 模型的 .yaml 文件

- 768-v-ema.ckpt [配置](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference-v.yaml))

- 512-base-ema.ckpt [配置](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference.yaml)

- 512-depth-ema.ckpt [配置](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-midas-inference.yaml)

下载配置 .yaml 文件并将其存储在与 .ckpt 同名的同一文件夹中。
