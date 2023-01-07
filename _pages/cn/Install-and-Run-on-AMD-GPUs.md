---
title: 在 AMD 上安装
layout: post
category: development
permalink: /install-on-amd/
machine_translated: true
lang: cn
---
以下说明仅适用于 Linux！可以在[此处](https://rentry.org/ayymd-stable-diffustion-v1_4-guide)（未经测试）找到适用于 Windows 用户的替代指南。

# 原生运行

执行以下操作：

```bash
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
cd stable-diffusion-webui
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip wheel

# It's possible that you don't need "--precision full", dropping "--no-half" however crashes my drivers
TORCH_COMMAND='pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/rocm5.1.1' python launch.py --precision full --no-half
```

在接下来的运行中，您只需要执行：
```bash
cd stable-diffusion-webui
# Optional: "git pull" to update the repository
source venv/bin/activate

# It's possible that you don't need "--precision full", dropping "--no-half" however crashes my drivers
TORCH_COMMAND='pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/rocm5.1.1' python launch.py --precision full --no-half
```

启动 WebUI 后的第一代可能需要很长时间，您可能会看到类似这样的消息：
> MIOpen(HIP)：警告 [SQLiteBase] 缺少系统数据库文件：gfx1030_40.kdb 性能可能会降低。请关注
> 安装说明：https://github.com/ROCmSoftwarePlatform/MIOpen#installing-miopen-kernels-package

下一代应该以正常的表现工作。你可以点击消息中的链接，如果你碰巧
要使用相同的操作系统，请按照此处的步骤解决此问题。如果没有明确的编译方式或
为您的操作系统安装 MIOpen 内核，请考虑遵循下面的“在 Docker 中运行”指南。



# 在 Docker 中运行
拉取最新的 `rocm/pytorch` Docker 镜像，启动镜像并附加到容器（取自 `rocm/pytorch`
文档）：`docker run -it --network=host --device=/dev/kfd --device=/dev/dri --group-add=video --ipc=host
--cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v $HOME/dockerx:/dockerx rocm/pytorch`

在容器内执行以下命令：
```bash
cd /dockerx
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
cd stable-diffusion-webui
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip wheel

# It's possible that you don't need "--precision full", dropping "--no-half" however crashes my drivers
TORCH_COMMAND='pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/rocm5.1.1' REQS_FILE='requirements.txt' python launch.py --precision full --no-half
```

以下运行只需要您重新启动容器，再次附加到它并在
容器：从这个列表中找到容器名称：`docker container ls --all`，选择与
`rocm/pytorch` 图像，重新启动它：`docker container restart <container-id>` 然后附加到它：`docker exec -it
<容器 ID> bash`。

```bash
cd /dockerx/stable-diffusion-webui
# Optional: "git pull" to update the repository
source venv/bin/activate

# It's possible that you don't need "--precision full", dropping "--no-half" however crashes my drivers
TORCH_COMMAND='pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/rocm5.1.1' REQS_FILE='requirements.txt' python launch.py --precision full --no-half
```

容器内的 `/dockerx` 文件夹应该可以在您的主目录中以相同的名称访问。

## 在 Docker 中更新 Python 版本
如果 Web UI 与 Docker 映像中预安装的 Python 3.7 版本不兼容，这里是
有关如何更新它的说明（假设您已成功遵循“在 Docker 中运行”）：

在容器内执行以下命令：
```bash
apt install python3.9-full # Confirm every prompt
update-alternatives --install /usr/local/bin/python python /usr/bin/python3.9 1
echo 'PATH=/usr/local/bin:$PATH' >> ~/.bashrc
```

然后重新启动容器并再次附加。如果您检查“python --version”，它现在应该显示“Python 3.9.5”或更新版本。

在容器内运行 rm -rf /dockerx/stable-diffusion-webui/venv ，然后按照“在内部运行”中的步骤操作
Docker”，跳过 `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui` 并使用修改后的
下面的启动命令：

```bash
TORCH_COMMAND='pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/rocm5.1.1' python launch.py --precision full --no-half
```
您可能不需要“--precision full”，删除“--no-half”，但它可能不适用于所有人。
某些显卡，如 Radeon RX 6000 系列和 RX 500 系列，无需选项 `--precision full --no-half` 即可正常运行，从而节省大量显存。 （注意 [此处](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/5468)。）

从现在开始始终使用这个新的启动命令，在后续运行中重新启动 Web UI 时也是如此。
