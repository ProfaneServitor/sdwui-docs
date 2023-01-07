---
title: 变形金刚
layout: post
category: Guides
permalink: /xformers/
machine_translated: true
lang: cn
---
Xformers 库是加速图像生成的可选方法。

除了一种特定配置外，没有适用于 Windows 的二进制文件，但您可以自己构建它。

来自一位匿名用户的指南，尽管我认为它适用于在 Linux 上构建：

关于如何构建 XFORMERS 的指南
还包括如何摆脱 sm86 对 voldy 新提交的限制

1.进入webui目录
2.`来源./venv/bin/activate`
3.`cd 存储库`
3.`git 克隆 https://github.com/facebookresearch/xformers.git`
4.`cd xformers`
5. `git 子模块更新 --init --recursive`
6.`pip install -r requirements.txt`
7.`pip 安装-e.`

## [@duckness](https://github.com/duckness) 在 Windows 上构建 xFormers

***



### 如果您在 Python 3.10 中使用 Pascal、Turing、Ampere、Lovelace 或 Hopper 卡，则无需再手动构建。卸载现有的 xformers 并使用 `--xformers` 启动 repo。将安装兼容的车轮。




***


1.【安装VS Build Tools 2022】(https://visualstudio.microsoft.com/downloads/?q=build+tools#build-tools-for-visual-studio-2022)，你只需要`Desktop development with C++ `

![setup_COFbK0AJAZ](https://user-images.githubusercontent.com/6380270/194767872-232136a1-9204-4b16-ae21-3e01f6f526ea.png)

2. [Install CUDA 11.3](https://developer.nvidia.com/cuda-11.3.0-download-archive)（后面的版本没测试），选择custom，你只需要下面的（VS integration估计不需要） ):

![setup_QwCdsQ28FM](https://user-images.githubusercontent.com/6380270/194767963-6df7ce14-e6eb-4718-8e93-a11abf172f14.png)

3.克隆[xFormers repo](https://github.com/facebookresearch/xformers)，创建一个`venv`并激活它

```sh
git clone https://github.com/facebookresearch/xformers.git
cd xformers
git submodule update --init --recursive
python -m venv venv
./venv/scripts/activate
```

4. 为了避免获取 CPU 版本的问题，[单独安装 pyTorch](https://pytorch.org/get-started/locally/)：

```sh
pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu113
```

5.然后安装其余的依赖项：

```sh
pip install -r requirements.txt
pip install wheel
```

6. 由于 CUDA 11.3 相当旧，您需要强制启用它以在 MS Build Tools 2022 上构建。如果在 `powershell` 上执行 `$env:NVCC_FLAGS = "-allow-unsupported-compiler"`，或 `set NVCC_FLAGS =-allow-unsupported-compiler` 如果在 `cmd`


7. 您终于可以构建 xFormers，请注意构建将花费很长时间（可能 10-20 分钟），它最初可能会抱怨一些错误，但它应该仍然可以正确编译。

> 可选提示：要进一步加快多核 CPU Windows 系统的速度，请安装 ninja https://github.com/ninja-build/ninja。
> 安装步骤：
> 1. 从 https://github.com/ninja-build/ninja/releases 下载 ninja-win.zip 并解压
> 2. 将 ninja.exe 放在 C:\Windows 下或将提取的 ninja.exe 的完整路径添加到系统 PATH 中
> 3. 在 cmd 中运行 ninja -h 并验证是否看到打印的帮助消息
> 4. 运行以下命令开始构建。它应该自动使用 Ninja，不需要额外的配置。您应该会看到明显更高的 CPU 使用率 (40%+)。
>```
> python setup.py 构建
> python setup.py bdist_wheel
>```
> 这将配备 AMD 5800X CPU 的 Windows PC 的构建时间从 1.5 小时减少到 10 分钟。
> Linux 和 MacOS 也支持 Ninja，但我没有这些操作系统可以测试，因此无法提供分步教程。



8. 运行以下命令：
```嘘
python setup.py 构建
蟒蛇 setup.py bdist_wheel
```

9. In `xformers` directory, navigate to the `dist` folder and copy the `.whl` file to the base directory of `stable-diffusion-webui`

10. In `stable-diffusion-webui` directory, install the `.whl`, change the name of the file in the command below if the name is different:

```sh
./venv/脚本/激活
pip 安装 xformers-0.0.14.dev0-cp310-cp310-win_amd64.whl
```

11. Ensure that `xformers` is activated by launching `stable-diffusion-webui` with `--force-enable-xformers`

## Non-deterministic / unstable / inconsistent results:

Known issue. See [this](https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/2705#discussioncomment-4024378 ) list on the discussion page.
