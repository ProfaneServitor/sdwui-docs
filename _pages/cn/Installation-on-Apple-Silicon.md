---
title: 在苹果上安装
layout: post
category: development
permalink: /install-on-apple/
machine_translated: true
lang: cn
---
Mac 用户：请提供反馈，说明这些说明是否适合您，如果有任何不清楚的地方，或者您仍然遇到当前未[在此处提及](https://github.com) 的安装问题/AUTOMATIC1111/stable-diffusion-webui/discussions/5461)。

重要笔记
------

当前，Web UI 中的大多数功能都可以在 macOS 上正常运行，最明显的例外是 CLIP 询问器和培训。尽管训练似乎确实有效，但它非常慢并且消耗过多的内存。可以使用 CLIP 询问器，但它不能与 macOS 使用的 GPU 加速一起正常工作，因此默认配置将完全通过 CPU 运行它（这很慢）。

众所周知，大多数采样器都可以工作，唯一的例外是使用稳定扩散 2.0 模型时的 PLMS 采样器。在 macOS 上使用 GPU 加速生成的图像通常应该匹配或几乎匹配在具有相同设置和种子的 CPU 上生成的图像。

自动安装
------


### 新安装：
1. 如果未安装 Homebrew，请按照 https://brew.sh 上的说明进行安装。保持终端窗口打开并按照“后续步骤”下的说明将 Homebrew 添加到您的 PATH。
2. 打开一个新的终端窗口并运行`brew install cmake protobuf rust python@3.10 git wget`
3. 通过运行 `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui` 克隆 Web UI 存储库
4. 将要使用的 Stable Diffusion 模型/检查点放入 `stable-diffusion-webui/models/Stable-diffusion`。如果没有，请参阅 [下载稳定的扩散模型](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon#downloading-stable-diffusion-models)以下。
5. `cd stable-diffusion-webui` 然后 `./webui.sh` 运行 web UI。将使用 venv 创建并激活 Python 虚拟环境，并且将自动下载并安装任何剩余的缺失依赖项。
6. 要稍后重新启动 Web UI 进程，请再次运行 `./webui.sh`。请注意，它不会自动更新网络用户界面；要更新，请在运行 ./webui.sh 之前运行 git pull。

### 现有安装：
如果您已经安装了使用“setup_mac.sh”创建的 Web UI，请从“stable-diffusion-webui”文件夹中删除“run_webui_mac.sh”文件和“repositories”文件夹。然后运行 ​​`git pull` 来更新 web UI，然后运行 ​​`./webui.sh` 来运行它。

下载稳定的扩散模型
------


如果您没有任何模型可以使用，可以从 [Hugging Face](https://huggingface.co/models?pipeline_tag=text-to-image&sort=downloads) 下载 Stable Diffusion 模型。要下载，请单击模型，然后单击“文件和版本”标题。查找以“.ckpt”或“.safetensors”扩展名列出的文件，然后单击文件大小右侧的向下箭头以下载它们。

一些流行的官方稳定扩散模型是：
* [稳定扩散 1.4](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original) ([sd-v1-4.ckpt](https://huggingface.co/CompVis/稳定扩散-v-1-4-原始/解决/主要/sd-v1-4.ckpt))
* [稳定扩散 1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) ([v1-5-pruned-emaonly.ckpt](https://huggingface.co/runwayml/stable- diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt））
* [稳定扩散 1.5 修复](https://huggingface.co/runwayml/stable-diffusion-inpainting) ([sd-v1-5-inpainting.ckpt](https://huggingface.co/runwayml/stable-diffusion -修复/解决/主要/sd-v1-5-inpainting.ckpt))

Stable Diffusion 2.0 和 2.1 需要模型和配置文件，生成图像时图像宽度和高度需要设置为 768 或更高：
* [稳定扩散 2.0](https://huggingface.co/stabilityai/stable-diffusion-2) ([768-v-ema.ckpt](https://huggingface.co/stabilityai/stable-diffusion-2/解决/主要/768-v-ema.ckpt))
* [稳定扩散 2.1](https://huggingface.co/stabilityai/stable-diffusion-2-1) ([v2-1_768-ema-pruned.ckpt](https://huggingface.co/stabilityai/stable- diffusion-2-1/resolve/main/v2-1_768-ema-pruned.ckpt))

配置文件，按住键盘上的option键，点击[这里](https://github.com/Stability-AI/stablediffusion/raw/main/configs/stable-diffusion/v2-inference-v.yaml ) 下载 `v2-inference-v.yaml`（它可能会下载为 `v2-inference-v.yaml.yml`）。在 Finder 中选择该文件，然后转到菜单并选择“文件”>“获取信息”。在出现的窗口中选择文件名并将其更改为模型的文件名，除了文件扩展名为“.yaml”而不是“.ckpt”，按键盘上的回车键（如果出现提示，请确认更改文件扩展名），然后将它放在与模型相同的文件夹中（例如，如果您下载了 `768-v-ema.ckpt` 模型，请将其重命名为 `768-v-ema.yaml` 并将其放入 `stable-diffusion-webui/models /Stable-diffusion` 以及模型）。

还提供了 [Stable Diffusion 2.0 深度模型](https://huggingface.co/stabilityai/stable-diffusion-2-depth) ([512-depth-ema.ckpt](https://huggingface.co/stabilityai /stable-diffusion-2-depth/resolve/main/512-depth-ema.ckpt))。通过按住键盘上的选项并单击 [此处](https://github.com/Stability-AI/stablediffusion/raw/main/configs/stable-diffusion/ v2-midas-inference.yaml)，然后按照上面提到的方式用`.yaml`扩展名重命名，和模型一起放在`stable-diffusion-webui/models/Stable-diffusion`中。请注意，此模型适用于 512 宽度/高度或更高而不是 768 的图像尺寸。

故障排除
------


### Web UI 无法启动：
如果您在尝试使用 ./webui.sh 启动 Web UI 时遇到错误，请尝试从 stable-diffusion-webui 文件夹中删除 repositories 和 venv 文件夹，然后使用 git pull 更新 Web UI ` 在再次运行 `./webui.sh` 之前。

＃＃＃ 表现不佳：
目前 macOS 上的 GPU 加速使用了_lot_内存。如果性能不佳（如果使用任何采样器生成 20 个步骤的 512x512 图像需要超过一分钟）首先尝试从 `--opt-split-attention-v1` 命令行选项（即 `./webui. sh --opt-split-attention-v1`) 看看是否有帮助。如果这没有太大区别，则打开位于 /Applications/Utilities 中的 Activity Monitor 应用程序并检查 Memory 选项卡下的内存压力图。如果生成图像时内存压力显示为红色，请关闭 web UI 进程，然后添加 `--medvram` 命令行选项（即 `./webui.sh --opt-split-attention-v1 -- medvram`）。如果该选项的性能仍然很差并且内存压力仍然是红色，那么请尝试使用 `--lowvram`（即 `./webui.sh --opt-split-attention-v1 --lowvram`）。如果使用任何采样器生成 20 个步骤的 512x512 图像仍然需要几分钟以上，那么您可能需要关闭 GPU 加速。在 Xcode 中打开 `webui-user.sh` 并将 `#export COMMANDLINE_ARGS=""` 更改为 `export COMMANDLINE_ARGS="--skip-torch-cuda-test --no-half --use-cpu all"`。

------


此处的讨论/反馈：https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/5461
