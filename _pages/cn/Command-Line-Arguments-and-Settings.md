---
title: 命令行参数和设置
layout: post
category: Guides
permalink: /cli/
machine_translated: true
lang: cn
---
## webui-用户

自定义程序运行方式的推荐方法是编辑 `webui-user.bat` (Windows) 和 `webui-user.sh` (Linux)：
- `set PYTHON` 允许设置自定义 Python 路径
- 示例：`set PYTHON=b:/soft/Python310/Python.exe`
- `set VENV_DIR` 允许您选择虚拟环境的目录。默认为“venv”。特殊值 `-` 运行脚本而不创建虚拟环境。
- 示例：`set VENV_DIR=C:\run\var\run` 将在 `C:\run\var\run` 目录中创建 venv。
- 示例：`set VENV_DIR=-` 使用系统的 python 运行程序
- `set COMMANDLINE_ARGS` 设置命令行参数 `webui.py` 运行
- 示例：`set COMMANDLINE_ARGS=--ckpt a.ckpt` 使用模型 `a.ckpt` 而不是 `model.ckpt`

## 命令行参数
### 在线运行
使用 `--share` 选项在线运行。你会得到一个 xxx.app.gradio 链接。这是在协作中使用该程序的预期方式。您可以使用标志 `--gradio-auth username:password` 为所述 gradio 共享实例设置身份验证，可选择提供多组用户名和密码，以逗号分隔。

使用 `--listen` 让服务器监听网络连接。这将允许本地网络上的计算机访问 UI，如果您配置端口转发，互联网上的计算机也可以访问。

使用 `--port xxxx` 让服务器侦听特定端口，xxxx 是需要的端口。请记住，所有低于 1024 的端口都需要 root/admin 权限，因此建议使用高于 1024 的端口。如果可用，默认为端口 7860。

# 所有命令行参数

|参数命令 |价值 |默认 |说明 |
| ---------------- | ----- | ------- | ----------- |

| **配置** |
-h, --帮助 |无 |错误 |显示此帮助消息并退出 |
--配置 |配置 |配置/稳定扩散/v1-inference.yaml |构建模型的配置路径 |
--ckpt | CKPT|模型.ckpt |稳定扩散模型检查点的路径；如果指定，此检查点将添加到检查点列表并加载 |
--ckpt目录 | CKPT_DIR |无 |具有稳定扩散检查点的目录路径 |
--gfpgan-目录| GFPGAN_DIR | GFPGAN / | GFPAN 目录 |
--gfpgan模型| GFPGAN_模型 | GFPAN 模型文件名 |
--codeformer-模型路径 | CODEFORMER_MODELS_PATH |模型/Codeformer/ |带有 codeformer 模型文件的目录路径。 |
--gfpgan-模型路径 | GFPGAN_MODELS_PATH |模型/GFPGAN |包含 GFPGAN 模型文件的目录路径。 |
--esrgan-模型路径 | ESRGAN_MODELS_PATH |型号/ESRGAN | ESRGAN 模型文件的目录路径。 |
--bsrgan-模型路径 | BSRGAN_MODELS_PATH |模型/BSRGAN |包含 BSRGAN 模型文件的目录路径。 |
--realesrgan-models-path | REALESRGAN_MODELS_PATH |模型/RealESRGAN |包含 RealESRGAN 模型文件的目录路径。 |
--scunet 模型路径 | SCUNET_MODELS_PATH |模型/ScuNET | ScuNET 模型文件的目录路径。 |
--swinir 模型路径 | SWINIR_MODELS_PATH |模型/SwinIR |包含 SwinIR 和 SwinIR v2 模型文件的目录路径。 |
--ldsr-模型路径 | LDSR_MODELS_PATH |模型/LDSR |包含 LDSR 模型文件的目录路径。 |
--剪辑模型路径 |剪辑模型路径 |无 | CLIP 模型文件的目录路径。 |
--vae 路径 | VAE_路径 |无 |变分自动编码器模型的路径 |
--嵌入目录 |嵌入目录 |嵌入/ |用于文本反转的嵌入目录（默认值：嵌入）|
--超网络目录 |超网络目录 |模型/超网络/ |超网络目录 |
--本地化目录 |本地化目录 |本地化/ |本地化目录
--样式文件 |样式文件 |样式.csv |用于样式的文件名 |
--ui 配置文件 |用户界面配置文件 |用户界面配置.json |用于 ui 配置的文件名 |
--无进度条隐藏 |无 |错误 |不要在 gradio UI 中隐藏进度条（我们隐藏它是因为如果你在浏览器中有硬件加速，它会减慢 ML）|
--最大批次计数| MAX_BATCH_COUNT | 16 | UI 的最大批计数值 |
--ui-设置文件 |用户界面设置文件 |配置.json |用于 ui 设置的文件名 |
--允许代码 |无 |错误 |允许从 webui 执行自定义脚本 |
--分享 |无 |错误 |对 gradio 使用 share=True 并使 UI 可以通过他们的网站访问（对我不起作用，但你可能会更幸运）
--听|无 |错误 |以 0.0.0.0 作为服务器名称启动 gradio，允许响应网络请求 |
--端口 |港口 | 7860 |使用给定的服务器端口启动 gradio，您需要端口 < 1024 的根/管理员权限，如果可用，默认为 7860 |
--hide-ui-dir-config |无 |错误 |从 webui 隐藏目录配置 |
--冻结设置 |无 |错误 |禁用编辑设置 |
--enable-insecure-extension-access |无 |错误 |无论其他选项如何，都启用扩展选项卡 |
--gradio调试|无 |错误 |使用 --debug 选项启动 gradio |
--gradio-auth | GRADIO_AUTH |无 |将 gradio 身份验证设置为“用户名：密码”；或逗号分隔多个，如 "u1:p1,u2:p2,u3:p3" |
--gradio-img2img-工具 | {color-sketch,editor} |编辑| gradio image uploader tool：可以是ctopping的编辑器，也可以是绘图的color-sketch |
--disable-console-progressbars |无 |错误 |不要向控制台输出进度条 |
--启用控制台提示 |无 |错误 |使用 txt2img 和 img2img 生成时打印提示到控制台 |
--API |无 |错误 |使用 API 启动 webui |
--nowebui |无 |错误 |只启动 API，不启动 UI |
--ui-调试模式 |无 |错误 |不加载模型以快速启动 UI |
--设备ID |设备 ID |无 |选择要使用的默认 CUDA 设备（之前可能需要导出 CUDA_VISIBLE_DEVICES=0,1 等）|
--管理员 |无 |错误 |管理员权限 |
| **性能** |
--变形金刚|无 |错误 |为交叉注意力层启用 xformers |
--reinstall-xformers |无 |错误 |强制重新安装 xformers。对升级很有用 - 但在升级后将其删除，否则您将永久重新安装 xformers。 |
--force-enable-xformers |无 |错误 |为交叉注意力层启用 xformers，无论检查代码是否认为您可以运行它； ***如果这不起作用，请不要提交错误报告*** |
--opt-split-attention |无 |错误 |强制启用 Doggettx 的交叉注意力层优化。默认情况下，它在支持 cuda 的系统上打开。 |
--opt-split-attention-invokeai |无 |错误 |强制启用 InvokeAI 的交叉注意层优化。默认情况下，它在 cuda 不可用时打开。 |
--opt-split-attention-v1 |无 |错误 |启用旧版本的分离注意力优化，它不会消耗它能找到的所有 VRAM |
--opt-channelslast |无 |错误 |最后更改记忆类型以稳定扩散到通道 |
--disable-opt-split-attention |无 |错误 |强制禁用交叉注意层优化 |
--使用CPU | {all, sd, interrogate, gfpgan, bsrgan, esrgan, scunet, codeformer} |无 |指定模块使用CPU作为手电筒设备|
--没有一半 |无 |错误 |不要将模型切换为 16 位浮点数 |
--精度| {full,autocast} |自动铸造 |以此精度进行评估 |
--no-half-vae |无 |错误 |不要将 VAE 模型切换为 16 位浮点数 |
--medvram |无 |错误 |启用稳定的扩散模型优化，为低 VRM 使用牺牲一点速度 |
--lowvram |无 |错误 |启用稳定的扩散模型优化以牺牲大量速度以获得非常低的 VRM 使用率 |
--洛拉姆 |无 |错误 |将稳定的扩散检查点权重加载到 VRAM 而不是 RAM
--always-batch-cond-uncond |无 |错误 |禁用使用 --medvram 或 --lowvram 节省内存的 cond/uncond 批处理
| **特点** |
--自动启动 |无 |错误 |启动时在系统默认浏览器中打开 webui URL |
--主题|无 |未设置 |打开具有指定主题（“light”或“dark”）的 webui。如果未指定，则使用默认浏览器主题 |
--使用文本框种子 |无 |错误 |在 UI 中使用文本框作为种子（不能向上/向下，但可以输入长种子）|
--disable-safe-unpickle |无 |错误 |禁用检查 pytorch 模型中的恶意代码 |
--ngrok |恩格罗克 |未设置 | ngrok authtoken，gradio --share 的替代品
--ngrok 区域 | NGROK_区域 |未设置 | ngrok 应该启动的区域。
| **失效选项** |
--show-negative-prompt |无 |错误 |什么都不做 |
--deepdanbooru |无 |错误 |什么都不做 |
--卸载-gfpgan |无 |错误 |什么都不做。
