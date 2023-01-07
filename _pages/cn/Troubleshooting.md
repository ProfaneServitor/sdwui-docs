---
title: 故障排除
layout: post
category: Guides
permalink: /troubleshooting/
machine_translated: true
lang: cn
---
- **该程序经测试可在 Python 3.10.6 上运行。除非你想找麻烦，否则不要使用其他版本。**
- 安装程序创建一个 python 虚拟环境，因此安装的模块都不会影响现有的 python 系统安装。
- 要使用系统的 python 而不是创建虚拟环境，请使用自定义参数替换“set VENV_DIR=-”。
- 要从头开始重新安装，请删除目录：`venv`、`repositories`。
- 第一次启动程序时，会显示 python 解释器的路径。如果这不是您安装的 python，您可以在 webui-user 脚本中指定完整路径；请参阅 [使用自定义参数运行](Run-with-Custom-Parameters)。
- 如果所需的 Python 版本不在 PATH 中，请使用 python 可执行文件的完整路径修改 `webui-user.bat` 中的 `set PYTHON=python` 行。
- 示例：`set PYTHON=B:\soft\Python310\python.exe`
- 来自“requirements_versions.txt”的安装程序要求，其中列出了专门与 Python 3.10.6 兼容的模块的版本。如果这不适用于其他版本的 Python，设置自定义参数“set REQS_FILE=requirements.txt”可能会有所帮助。

# 低 VRAM 视频卡
在具有少量 VRAM (<=4GB) 的视频卡上运行时，可能会出现内存不足错误。
可以通过命令行参数启用各种优化，牺牲一些/很多速度以支持使用更少的 VRAM：
- 如果您有 4GB VRAM 并想制作 512x512（或最多 640x640）图像，请使用 `--medvram`。
- 如果您有 4GB VRAM 并想制作 512x512 图像，但使用 `--medvram` 时出现内存不足错误，请改用 `--medvram --opt-split-attention`。
- 如果您有 4GB VRAM 并想制作 512x512 图像，但仍然出现内存不足错误，请改用 `--lowvram --always-batch-cond-uncond --opt-split-attention`。
- 如果您有 4GB VRAM 并且想要使图像比使用 `--medvram` 时更大，请使用 `--lowvram --opt-split-attention`。
- 如果你有更多的 VRAM 并且想要制作比你通常可以制作的更大的图像（例如 1024x1024 而不是 512x512），请使用 `--medvram --opt-split-attention`。您也可以使用 `--lowvram` 但效果可能几乎不明显。
- 否则，不要使用其中任何一个。

# 绿屏或黑屏
显卡
在不支持半精度浮点数的视频卡上运行时（16xx 卡的一个已知问题），可能会出现绿色或黑色屏幕，而不是生成的图片。
这可以通过在 VRAM 使用量显着增加时使用命令行参数 `--precision full --no-half` 来解决，这可能需要 `--medvram`。

# 启用 xformers 后出现“CUDA 错误：没有可在设备上执行的内核映像”
您安装的 xformers 与您的 GPU 不兼容。如果您使用 Python 3.10，拥有 Pascal 或更高版本的卡并在 Windows 上运行，请将 `--reinstall-xformers --xformers` 添加到您的 `COMMANDLINE_ARGS` 以升级到工作版本。升级后删除 `--reinstall-xformers`。

# NameError: 名称 'xformers' 未定义
如果你使用 Windows，这意味着你的 Python 太旧了。使用 3.10

如果是 Linux，则必须自己构建 xformers 或避免使用 xformers。
