---
title: 安装
priority: 0
category: Getting started
layout: post
permalink: /install/
machine_translated: true
lang: cn
---
如果您使用的是较旧且功能较弱的计算机，请考虑使用其中一种在线服务（例如 Colab）。虽然可以在内存小于 4Gb 的 GPU 甚至 TPU 上运行生成模型并进行一些[优化](../optimizations)，但依赖云服务通常更快、更实用。

- [在线服务](../在线服务)

如果您决定在本地安装，请确保满足所需的 [dependencies](../dependencies)。

### 在 Windows 上自动安装

这是针对基于 NVidia 的 GPU 的说明。对于 AMD，请参阅 [此处](https://rentry.org/ayymd-stable-diffustion-v1_4-guide)。

1. 安装[Python 3.10.6](https://www.python.org/downloads/windows/)，勾选“Add Python to PATH”
2. 安装 [git](https://git-scm.com/download/win)。
3. 下载 stable-diffusion-webui 存储库，例如通过运行 `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`。
4. 将 `model.ckpt` 放在 `models` 目录中（参见 [dependencies](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies) 获取它的位置）。
5. _*（可选）*_ 将 `GFPGANv1.4.pth` 与 `webui.py` 放在基本目录中（参见 [dependencies](https://github.com/AUTOMATIC1111/stable-diffusion-webui/ wiki/Dependencies）获取它的位置）。
6. 以普通非管理员用户身份从 Windows 资源管理器运行 `webui-user.bat`。

### 在 Linux 上自动安装

这是针对基于 NVidia 的 GPU 的说明。对于 AMD，请参阅 [AMD](../install-on-amd/)

1.安装依赖：
```bash
# Debian-based:
sudo apt install wget git python3 python3-venv
# Red Hat-based:
sudo dnf install wget git python3
# Arch-based:
sudo pacman -S wget git python3
```
2. 要安装在`/home/$(whoami)/stable-diffusion-webui/`，运行：
```bash
bash <(wget -qO- https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh)
```

### 在 Apple Silicon 上安装

在 [此处](../install-on-apple/) 找到说明。
