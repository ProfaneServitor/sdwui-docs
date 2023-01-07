---
title: 在英伟达上安装
layout: post
category: development
permalink: /install-on-nvidia/
machine_translated: true
lang: cn
---
在尝试安装之前，请确保满足所有必需的 [dependencies](Dependencies)。

# 自动安装
## 窗口
从 Windows Explorer 正常运行 `webui-user.bat`，***非管理员***，用户。

请参阅 [故障排除](Troubleshooting) 部分了解如果出现问题该怎么办。

## Linux
要在默认目录`/home/$(whoami)/stable-diffusion-webui/` 中安装，请运行：
```bash
bash <(wget -qO- https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh)
```

为了自定义安装，将存储库克隆到所需位置，更改 webui-user.sh 中所需的变量并运行：
```bash
bash webui.sh
```

# 几乎自动安装和启动
要在不创建虚拟环境的情况下通过 pip 安装所需的包，请运行：
```bash
python launch.py
```

命令行参数可以直接传递，例如：
```bash
python launch.py --opt-split-attention --ckpt ../secret/anime9999.ckpt
```

# 手动安装
手动安装非常过时，可能无法正常工作。查看存储库自述文件中的 colab 以获取说明。

以下过程在 Windows 或 Linux 上手动安装所有内容（后者需要将 `dir` 替换为 `ls`）：
```bash
# install torch with CUDA support. See https://pytorch.org/get-started/locally/ for more instructions if this fails.
pip install torch --extra-index-url https://download.pytorch.org/whl/cu113

# check if torch supports GPU; this must output "True". You need CUDA 11. installed for this. You might be able to use
# a different version, but this is what I tested.
python -c "import torch; print(torch.cuda.is_available())"

# clone web ui and go into its directory
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui

# clone repositories for Stable Diffusion and (optionally) CodeFormer
mkdir repositories
git clone https://github.com/CompVis/stable-diffusion.git repositories/stable-diffusion
git clone https://github.com/CompVis/taming-transformers.git repositories/taming-transformers
git clone https://github.com/sczhou/CodeFormer.git repositories/CodeFormer
git clone https://github.com/salesforce/BLIP.git repositories/BLIP

# install requirements of Stable Diffusion
pip install transformers==4.19.2 diffusers invisible-watermark --prefer-binary

# install k-diffusion
pip install git+https://github.com/crowsonkb/k-diffusion.git --prefer-binary

# (optional) install GFPGAN (face restoration)
pip install git+https://github.com/TencentARC/GFPGAN.git --prefer-binary

# (optional) install requirements for CodeFormer (face restoration)
pip install -r repositories/CodeFormer/requirements.txt --prefer-binary

# install requirements of web ui
pip install -r requirements.txt  --prefer-binary

# update numpy to latest version
pip install -U numpy  --prefer-binary

# (outside of command line) put stable diffusion model into web ui directory
# the command below must output something like: 1 File(s) 4,265,380,512 bytes
dir model.ckpt

```

安装完成，启动web ui，运行：
```bash
python webui.py
```

# Windows 11 WSL2 说明
要在 Windows 11 的 WSL2 中的 Linux 发行版下安装：
```bash
# install conda (if not already done)
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
chmod +x Anaconda3-2022.05-Linux-x86_64.sh
./Anaconda3-2022.05-Linux-x86_64.sh

# Clone webui repo
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui

# Create and activate conda env
conda env create -f environment-wsl2.yaml
conda activate automatic

```

此时，可以应用手动安装的说明，从步骤“# clone repositories for Stable Diffusion and (optional) CodeFormer”开始。


# 在 Windows 上使用 Conda 进行替代安装
- 先决条件 _*（仅当您没有时才需要）*_。假设安装了 [Chocolatey](https://chocolatey.org/install)。
```狂欢
# 安装 git
choco 安装 git
# 安装畅达
choco 安装 anaconda3
    ```

可选参数：[git](https://community.chocolatey.org/packages/git), [conda](https://community.chocolatey.org/packages/anaconda3)
- 安装（警告：某些文件超过数 GB，请先确保您有空间）
1. 下载为 .zip 并解压或使用 git 克隆。
```狂欢
git 克隆 https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
        ```

2. 启动 Anaconda 提示符。应该注意的是，您可以使用较旧的 Python 版本，但您可能被迫手动删除缓存优化等功能，这会降低您的性能。
```狂欢
# 导航到git目录
cd "GIT\StableDiffusion"
# 创建环境
conda create -n StableDiffusion python=3.10.6
# 激活环境
conda 激活 StableDiffusion
# 验证环境是否被选中
conda 环境列表
# 启动本地网络服务器
webui用户.bat
# 等待“在本地 URL 上运行：http://127.0.0.1:7860”并打开该 URI。
        ```

3. _*（可选）*_ 转到 [CompVis](https://huggingface.co/CompVis) 并下载最新模型，例如 [1.4](https://huggingface.co/CompVis/stable-diffusion- v1-4) 并将其解压为 ex:
```狂欢
GIT\StableDiffusion\模型\稳定扩散
        ```

之后通过重新启动 Anaconda 提示符和
```狂欢
webui用户.bat
        ```

- 值得尝试的替代默认设置：
1. 尝试 **euler a** (Ancestral Euler) 和更高的 **Sampling Steps** 例如：40 或其他 100。
2. 将“设置 > 用户界面 > 每 N 个采样步骤显示图像创建进度”设置为 1，然后选择一个确定性的 **种子** 值。可以直观地看到图像解散是如何发生的，并使用 [ScreenToGif](https://github.com/NickeManarin/ScreenToGif) 录制一个 .gif。
3.使用**恢复人脸**。通常，结果会更好，但质量是以速度为代价的。
