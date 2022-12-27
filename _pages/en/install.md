---
title: Install
priority: 0
category: Getting started
layout: post
permalink: /install/
lang: en
---
If you are using an older weaker computer, consider using one of online services (like Colab). While it is possible to run generative models on GPUs with less than 4Gb memory or even TPU with some [optimizations](../optimizations), it's usually faster and more practical to rely on cloud services.

- [Online Services](../Online-services)

If you decide to install locally, make sure the required [dependencies](../dependencies) are met.

### Automatic Installation on Windows

This is instructions for NVidia-based GPUs. For AMD, see [here](https://rentry.org/ayymd-stable-diffustion-v1_4-guide).

1. Install [Python 3.10.6](https://www.python.org/downloads/windows/), checking "Add Python to PATH"
2. Install [git](https://git-scm.com/download/win).
3. Download the stable-diffusion-webui repository, for example by running `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`.
4. Place `model.ckpt` in the `models` directory (see [dependencies](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies) for where to get it).
5. _*(Optional)*_ Place `GFPGANv1.4.pth` in the base directory, alongside `webui.py` (see [dependencies](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies) for where to get it).
6. Run `webui-user.bat` from Windows Explorer as normal, non-administrator, user.

### Automatic Installation on Linux

This is instructions for NVidia-based GPUs. For AMD, see  [AMD](../install-on-amd/)

1. Install the dependencies:
```bash
# Debian-based:
sudo apt install wget git python3 python3-venv
# Red Hat-based:
sudo dnf install wget git python3
# Arch-based:
sudo pacman -S wget git python3
```
2. To install in `/home/$(whoami)/stable-diffusion-webui/`, run:
```bash
bash <(wget -qO- https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh)
```

### Installation on Apple Silicon

Find the instructions [here](../install-on-apple/).
