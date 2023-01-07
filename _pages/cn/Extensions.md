---
title: 扩展
layout: post
category: Guides
permalink: /extensions/
handle: /extensions/
machine_translated: true
lang: cn
---
＃ 基本信息

扩展是一种更方便的用户脚本形式。

扩展都存在于 extensions 目录中它们自己的子目录中。你可以像这样使用 git 安装扩展：

```
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients extensions/aesthetic-gradients
```

这会将来自 https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients 的扩展安装到 extensions/aesthetic-gradients 目录中。

或者，您可以将目录复制粘贴到“extensions”中。

关于开发扩展，参见[开发扩展](Developing-extensions)。

＃ 安全

由于扩展允许用户安装和运行任意代码，这可能会被恶意使用，并且在使用允许远程用户连接到服务器的选项（`--share` 或 `--listen`）运行时默认禁用 -您仍然拥有用户界面，但尝试安装任何东西都会导致错误。如果您想使用这些选项并且仍然能够安装扩展，请使用 `--enable-insecure-extension-access` 命令行标志。

# 扩展

## 审美渐变

<https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients>

从一张或几张图片创建嵌入，并使用它将其样式应用于生成的图像。

![firefox_FgKg9dx9eF](https://user-images.githubusercontent.com/20920490/197466300-6b042bcf-5cba-4600-97d7-ad2652875706.png)

## 通配符
<https://github.com/AUTOMATIC1111/stable-diffusion-webui-wildcards>

允许您在提示中使用 __name__ 语法从通配符目录中名为 name.txt 的文件中获取随机行。

## 动态提示

<https://github.com/adieyal/sd-dynamic-prompts>

[AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 的自定义扩展，实现了用于随机或组合提示生成的表达模板语言以及支持深度通配符目录的功能结构。

[自述文件](https://github.com/adieyal/sd-dynamic-prompts) 中显示了更多功能和新增功能。

![图像](https://github.com/adieyal/sd-dynamic-prompts/raw/main/images/extension.png)

使用这个扩展，提示：

{2$$artist1|artist2|artist3} 的{夏季|冬季|秋季|春季}的{房子|公寓|旅馆|小屋}`

会出现以下任一提示：

- 艺术家 1、艺术家 2 的夏季房屋
- 艺术家 3、艺术家 1 的秋天小屋
- 艺术家 2、艺术家 3 的冬季小屋
- ...


如果您正在寻找艺术家和风格的有趣组合，这将特别有用。

您还可以从文件中选择一个随机字符串。假设您在 WILDCARD_DIR 中有文件 seasons.txt（见下文），那么：

`__seasons__ 来了`

可能会生成以下内容：

- 冬天来了
- 春天来了
- ...


您也可以两次使用相同的通配符

`我爱__seasons__胜过__seasons__`

- 比起夏天我更喜欢冬天
- 我爱春天胜过春天

## 梦想亭
<https://github.com/d8ahazard/sd_dreambooth_extension>

用户界面中的 Dreambooth。有关调整和配置要求，请参阅项目自述文件。包括 [LoRA](https://github.com/cloneofsimo/lora)（低阶适应）

基于 ShivamShiaro 的回购协议。

![图片](https://user-images.githubusercontent.com/1633844/201434706-2c2744ba-082e-427e-9f8d-af03de204583.png)


## 智能流程
<https://github.com/d8ahazard/sd_smartprocess>

智能裁剪、字幕和图像增强。

![图片](https://user-images.githubusercontent.com/1633844/201435094-433d765c-56e8-4573-82d9-71af2b112159.png)


## 图像浏览器
<https://github.com/yfszzx/stable-diffusion-webui-images-browser>

提供在网络浏览器中浏览创建的图像的界面。

![68747470733a2f2f73362e6a70672e636d2f323032322f31302f32342f504a6a755a742e706e67](https://user-images.githubusercontent.com/20920490/197518762-a23f3e34-f174-4275-8283-eb8d2ff65ef2.png)

＃＃ 灵感
<https://github.com/yfszzx/stable-diffusion-webui-inspiration>

随机显示艺术家或艺术流派典型风格的图片，选择后显示更多该艺术家或流派的图片。所以你在创作时不必担心选择合适的艺术风格有多难。

![68747470733a2f2f73362e6a70672e636d2f323032322f31302f32322f504a596f4e4c2e706e67](https://user-images.githubusercontent.com/20920490/197518700-3f753132-8799-4ad0-8cdf-bcdcbf7798aa.png)

＃＃ 以下
<https://github.com/deforum-art/deforum-for-automatic1111-webui>


Deforum 的官方端口，一个用于 2D 和 3D 动画的扩展脚本，支持关键帧序列、动态数学参数（甚至在提示内）、动态遮罩、深度估计和变形。

![ui](https://user-images.githubusercontent.com/20920490/197619558-c088a329-3672-4f0a-8685-cf539996ad1e.png)

## 艺术家学习
<https://github.com/camenduru/stable-diffusion-webui-artists-to-study>

<https://artiststostudy.pages.dev/> 适用于 [web ui] 的扩展（https://github.com/AUTOMATIC1111/stable-diffusion-webui）。

要安装它，请将 repo 克隆到 `extensions` 目录并重新启动 web ui：

`git clone https://github.com/camenduru/stable-diffusion-webui-artists-to-study`

您可以通过单击将艺术家姓名添加到剪贴板。 （感谢 @gmaciocci 的想法）

![图片](https://user-images.githubusercontent.com/54370274/197829512-e7d30d44-2697-4ecd-b9a7-3665217918c7.jpg)

## 审美形象得分手

<https://github.com/tsngo/stable-diffusion-webui-aesthetic-image-scorer>

https://github.com/AUTOMATIC1111/stable-diffusion-webui 的扩展

基于 [Chad Scorer](https://github.com/grexzen/SD) 使用 [CLIP+MLP 美学分数预测器](https://github.com/christophschuhmann/improved-aesthetic-predictor) 计算生成图像的美学分数-乍得/blob/main/chad_scorer.py)

参见[讨论](https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/1831)

将分数保存到 windows 标签，并计划其他选项

![图片](https://github.com/tsngo/stable-diffusion-webui-aesthetic-image-scorer/blob/main/tag_group_by.png)

## 数据集标签编辑器
<https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor>

[日语自述文件](https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor/blob/main/README-JP.md)

这是 [Stable Diffusion web UI by AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 训练数据集中编辑字幕的扩展。

它适用于逗号分隔样式的文本标题（例如 DeepBooru 审讯器生成的标签）。

可以加载图片文件名中的字幕，但编辑后的字幕只能以文本文件的形式保存。

![图片](https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor/blob/main/ss01.png)

## 自动 sd-paint-ext

<https://github.com/Interpause/auto-sd-paint-ext>

以前称为“auto-sd-krita”。

>使用 Krita 插件扩展 AUTOMATIC1111 的 webUI（其他绘图工作室即将推出？）

过时的演示 |新用户界面（全部：演示图像）
--- | ---
![demo image](https://user-images.githubusercontent.com/42513874/194701722-e7a3f7eb-be4a-4f43-93a5-480835c9260f.jpg) | ![demo image 2](https://user-images.githubusercontent.com/42513874/199507299-66729f9b-3581-43a3-b5f4-57eb90b8f981.png)

**Differences**

- UI no longer freezes during image update
- Inpainting layer no longer has to be manually hidden, nor use white specifically
- UI has been improved & squeezed further
- Scripts API is now possible

## training-picker
<https://github.com/Maurdekye/training-picker>

Adds a tab to the webui that allows the user to automatically extract keyframes from video, and manually extract 512x512 crops of those frames for use in model training.

![image](https://user-images.githubusercontent.com/2313721/199614791-1f573573-a2e2-4358-836d-5655825077e1.png)

**Installation**

- Install [AUTOMATIC1111's Stable Diffusion Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- Install [ffmpeg](https://ffmpeg.org/) for your operating system
- Clone this repository into the extensions folder inside the webui
- Drop videos you want to extract cropped frames from into the training-picker/videos folder

## Unprompted

<https://github.com/ThereforeGames/unprompted>

Supercharge your prompt workflow with this powerful scripting language!

![unprompted_header](https://user-images.githubusercontent.com/95403634/199041569-7c6c5748-e7dc-4068-943f-c2d92745dbb5.png)

**Unprompted** is a highly modular extension for [AUTOMATIC1111's Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) that allows you to include various shortcodes in your prompts. You can pull text from files, set up your own variables, process text through conditional functions, and so much more - it's like wildcards on steroids.

While the intended usecase is Stable Diffusion, **this engine is also flexible enough to serve as an all-purpose text generator.**

## Booru tag autocompletion
<https://github.com/DominikDoom/a1111-sd-webui-tagcomplete>

Displays autocompletion hints for tags from "image booru" boards such as Danbooru. Uses local tag CSV files and includes a config for customization.

![image](https://user-images.githubusercontent.com/20920490/200016417-9451efdb-5d0d-4131-bd9e-39a687be8dd7.png)

## novelai-2-local-prompt
<https://github.com/animerl/novelai-2-local-prompt>

Add a button to convert the prompts used in NovelAI for use in the WebUI. In addition, add a button that allows you to recall a previously used prompt.

![pic](https://user-images.githubusercontent.com/113022648/197382468-65f4a96d-48af-4890-8fcf-0ec7c3b9ec3a.png)

## Tokenizer
<https://github.com/AUTOMATIC1111/stable-diffusion-webui-tokenizer>

Adds a tab that lets you preview how CLIP model would tokenize your text.

![about](https://user-images.githubusercontent.com/20920490/200113798-50b55f5a-45db-4b6f-93c0-ae6be75e5788.png)

## Push to 🤗 Hugging Face

<https://github.com/camenduru/stable-diffusion-webui-huggingface>

![Push Folder to Hugging Face](https://user-images.githubusercontent.com/54370274/206897701-9e86ce7c-af06-4d95-b9ea-385276c99d3a.jpg)

To install it, clone the repo into the `extensions` directory and restart the web ui:

`git clone https://github.com/camenduru/stable-diffusion-webui-huggingface`

`pip install huggingface-hub`

## StylePile
<https://github.com/some9000/StylePile>

An easy way to mix and match elements to prompts that affect the style of the result.

![image](https://user-images.githubusercontent.com/98228077/208331056-2956d050-a7a4-4b6f-b064-72f6a7d7ee0d.png)

## Latent Mirroring
<https://github.com/dfaker/SD-latent-mirroring>

Applies mirroring and flips to the latent images to produce anything from subtle balanced compositions to perfect reflections

![image](https://user-images.githubusercontent.com/98228077/208331098-3b7fefce-6d38-486d-9543-258f5b2b0fd6.png)

## Embeddings editor
<https://github.com/CodeExplode/stable-diffusion-webui-embedding-editor>

Allows you to manually edit textual inversion embeddings using sliders.

![image](https://user-images.githubusercontent.com/98228077/208331138-cdfe8f43-78f7-499e-b746-c42355ee8d6d.png)

## seed travel
<https://github.com/yownas/seed_travel>

Small script for AUTOMATIC1111/stable-diffusion-webui to create images that exists between seeds.

<img src="https://github.com/ClashSAN/bloated-gifs/blob/main/seedtravel.gif" width="512" height="512" />


## shift-attention
<https://github.com/yownas/shift-attention>

Generate a sequence of images shifting attention in the prompt. This script enables you to give a range to the weight of tokens in a prompt and then generate a sequence of images stepping from the first one to the second.

<https://user-images.githubusercontent.com/13150150/193368939-c0a57440-1955-417c-898a-ccd102e207a5.mp4

## prompt travel
<https://github.com/Kahsolt/stable-diffusion-webui-prompt-travel>

Extension script for AUTOMATIC1111/stable-diffusion-webui to travel between prompts in latent space.

<img src="https://github.com/ClashSAN/bloated-gifs/blob/main/prompt_travel.gif" width="512" height="512" />


## Sonar
<https://github.com/Kahsolt/stable-diffusion-webui-sonar>

Improve the generated image quality, searches for similar (yet even better!) images in the neighborhood of some known image, focuses on single prompt optimization rather than traveling between multiple prompts.

![image](https://user-images.githubusercontent.com/98228077/209545702-c796a3f8-4d8c-4e2b-9b2e-920008ec2f32.png)![image](https://user-images.githubusercontent.com/98228077/209545756-31c94fec-d783-447f-8aac-4a5bba43ea15.png)

## Detection Detailer
<https://github.com/dustysys/ddetailer>

An object detection and auto-mask extension for Stable Diffusion web UI.

<img src="https://github.com/dustysys/ddetailer/raw/master/misc/ddetailer_example_3.gif"/>


## conditioning-highres-fix
<https://github.com/klimaleksus/stable-diffusion-webui-conditioning-highres-fix>

This is Extension for rewriting Inpainting conditioning mask strength value relative to Denoising strength at runtime. This is useful for Inpainting models such as sd-v1-5-inpainting.ckpt

![image](https://user-images.githubusercontent.com/98228077/208331374-5a271cf3-cfac-449b-9e09-c63ddc9ca03a.png)

## Randomize
<https://github.com/stysmmaker/stable-diffusion-webui-randomize>

Allows for random parameters during txt2img generation. This script is processed for all generations, regardless of the script selected, meaning this script will function with others as well, such as AUTOMATIC1111/stable-diffusion-webui-wildcards.

## Auto TLS-HTTPS
<https://github.com/papuSpartan/stable-diffusion-webui-auto-tls-https>

Allows you to easily, or even completely automatically start using HTTPS.

## DreamArtist
<https://github.com/7eu7d7/DreamArtist-sd-webui-extension>

Towards Controllable One-Shot Text-to-Image Generation via Contrastive Prompt-Tuning.

![image](https://user-images.githubusercontent.com/98228077/208331536-069783ae-32f7-4897-8c1b-94e0ae14f9cd.png)

## WD 1.4 Tagger
<https://github.com/toriato/stable-diffusion-webui-wd14-tagger>

Uses a trained model file, produces WD 1.4 Tags. Model link - https://mega.nz/file/ptA2jSSB#G4INKHQG2x2pGAVQBn-yd_U5dMgevGF8YYM9CR_R1SY

![image](https://user-images.githubusercontent.com/98228077/208331569-2cf82c5c-f4c3-4181-84bd-2bdced0c2cff.png)

## booru2prompt
<https://github.com/Malisius/booru2prompt>

This SD extension allows you to turn posts from various image boorus into stable diffusion prompts. It does so by pulling a list of tags down from their API. You can copy-paste in a link to the post you want yourself, or use the built-in search feature to do it all without leaving SD.

![image](https://user-images.githubusercontent.com/98228077/208331612-dad61ef7-33dd-4008-9cc7-06b0b0a7cb6d.png)

also see:\
<https://github.com/stysmmaker/stable-diffusion-webui-booru-prompt>

## gelbooru-prompt
<https://github.com/antis0007/sd-webui-gelbooru-prompt>

Fetch tags with image hash. Updates planned.

## Merge Board
<https://github.com/bbc-mc/sdweb-merge-board>

Multiple lane merge support(up to 10). Save and Load your merging combination as Recipes, which is simple text.

![image](https://user-images.githubusercontent.com/98228077/208331651-09a0d70e-1906-4f80-8bc1-faf3c0ca8fad.png)

also see:\
<https://github.com/Maurdekye/model-kitchen>

## Depth Maps
<https://github.com/thygate/stable-diffusion-webui-depthmap-script>

Creates depthmaps from the generated images. The result can be viewed on 3D or holographic devices like VR headsets or lookingglass display, used in Render or Game- Engines on a plane with a displacement modifier, and maybe even 3D printed.

![image](https://user-images.githubusercontent.com/98228077/208331747-9acba3f0-3039-485e-96ab-f0cf5619ec3b.png)

## multi-subject-render
<https://github.com/Extraltodeus/multi-subject-render>

It is a depth aware extension that can help to create multiple complex subjects on a single image. It generates a background, then multiple foreground subjects, cuts their backgrounds after a depth analysis, paste them onto the background and finally does an img2img for a clean finish.

![image](https://user-images.githubusercontent.com/98228077/208331952-019dfd64-182d-4695-bdb0-4367c81e4c43.png)

## depthmap2mask
<https://github.com/Extraltodeus/depthmap2mask>

Create masks for img2img based on a depth estimation made by MiDaS.

![image](https://user-images.githubusercontent.com/15731540/204050868-eca8db02-2193-4115-a5b8-e8f5c796e035.png)![image](https://user-images.githubusercontent.com/15731540/204050888-41b00335-50b4-4328-8cfd-8fc5e9cec78b.png)![image](https://user-images.githubusercontent.com/15731540/204050899-8757b774-f2da-4c15-bfa7-90d8270e8287.png)

## ABG_extension
<https://github.com/KutsuyaYuki/ABG_extension>

Automatically remove backgrounds. Uses an onnx model fine-tuned for anime images. Runs on GPU.

| ![test](https://user-images.githubusercontent.com/98228077/209423352-e8ea64e7-8522-4c2c-9350-c7cd50c35c7c.png) |  ![00035-4190733039-cow](https://user-images.githubusercontent.com/98228077/209423400-720ddde9-258a-4e68-8a93-73b67dad714e.png) | ![00021-1317075604-samdoesarts portrait](https://user-images.githubusercontent.com/98228077/209423428-da7c68db-e7d1-45a1-b931-817de9233a67.png) | ![00025-2023077221-](https://user-images.githubusercontent.com/98228077/209423446-79e676ae-460e-4282-a591-b8b986bfd869.png) |
| :---: | :---: | :---: | :---: |
| ![img_-0002-3313071906-bust shot of person](https://user-images.githubusercontent.com/98228077/209423467-789c17ad-d7ed-41a9-a039-802cfcae324a.png) | ![img_-0022-4190733039-cow](https://user-images.githubusercontent.com/98228077/209423493-dcee7860-a09e-41e0-9397-715f52bdcaab.png) | ![img_-0008-1317075604-samdoesarts portrait](https://user-images.githubusercontent.com/98228077/209423521-736f33ca-aafb-4f8b-b067-14916ec6955f.png) | ![img_-0012-2023077221-](https://user-images.githubusercontent.com/98228077/209423546-31b2305a-3159-443f-8a98-4da22c29c415.png) |

## Visualize Cross-Attention
<https://github.com/benkyoujouzu/stable-diffusion-webui-visualize-cross-attention-extension

![image](https://user-images.githubusercontent.com/98228077/208332131-6acdae9a-2b25-4e71-8ab0-6e375c7c0419.png)

Generates highlighted sectors of a submitted input image, based on input prompts. Use with tokenizer extension. See the readme for more info.

## DAAM
<https://github.com/kousw/stable-diffusion-webui-daam

DAAM stands for Diffusion Attentive Attribution Maps. Enter the attention text (must be a string contained in the prompt) and run. An overlapping image with a heatmap for each attention will be generated along with the original image.

![image](https://user-images.githubusercontent.com/98228077/208332173-ffb92131-bd02-4a07-9531-136822d06c86.png)

## Prompt Gallery
<https://github.com/dr413677671/PromptGallery-stable-diffusion-webui

Build a yaml file filled with prompts of your character, hit generate, and quickly preview them by their word attributes and modifiers.

![image](https://user-images.githubusercontent.com/98228077/208332199-7652146c-2428-4f44-9011-66e81bc87426.png)

## embedding-inspector
<https://github.com/tkalayci71/embedding-inspector

Inspect any token(a word) or Textual-Inversion embeddings and find out which embeddings are similar. You can mix, modify, or create the embeddings in seconds. Much more intriguing options have since been released, see [here.](https://github.com/tkalayci71/embedding-inspector#whats-new)

![image](https://user-images.githubusercontent.com/98228077/209546038-3f4206bf-2c43-4d58-bf83-6318ade393f4.png)

## Infinity Grid Generator
<https://github.com/mcmonkeyprojects/sd-infinity-grid-generator-script

Build a yaml file with your chosen parameters, and generate infinite-dimensional grids. Built-in ability to add description text to fields. See readme for usage details.

![image](https://user-images.githubusercontent.com/98228077/208332269-88983668-ea7e-45a8-a6d5-cd7a9cb64b3a.png)

## NSFW checker
<https://github.com/AUTOMATIC1111/stable-diffusion-webui-nsfw-censor

Replaces NSFW images with black.

## Diffusion Defender
<https://github.com/WildBanjos/DiffusionDefender

Prompt blacklist, find and replace, for semi-private and public instances.

## Config-Presets
<https://github.com/Zyin055/Config-Presets

Adds a configurable dropdown to allow you to change UI preset settings in the txt2img and img2img tabs.

![image](https://user-images.githubusercontent.com/98228077/208332322-24339554-0274-4add-88a7-d33bba1e3823.png)

## Preset Utilities
<https://github.com/Gerschel/sd_web_ui_preset_utils

Preset tool for UI. Planned support for some other custom scripts.

![image](https://user-images.githubusercontent.com/98228077/209540881-2a870282-edb6-4c94-869b-5493cdced01f.png)

## DH Patch
<https://github.com/d8ahazard/sd_auto_fix

Random patches by D8ahazard. Auto-load config YAML files for v2, 2.1 models; patch latent-diffusion to fix attention on 2.1 models (black boxes without no-half), whatever else I come up with.

## Riffusion
<https://github.com/enlyth/sd-webui-riffusion

Use Riffusion model to produce music in gradio. To replicate [original](https://www.riffusion.com/about) interpolation technique, input the [prompt travel extension](https://github.com/Kahsolt/stable-diffusion-webui-prompt-travel) output frames into the riffusion tab.

![image](https://user-images.githubusercontent.com/98228077/209539460-f5c23891-b5e6-46c7-b1a5-b7440a3f031b.png)![image](https://user-images.githubusercontent.com/98228077/209539472-031e623e-f7a2-4da9-9711-8bf73d0cfe6e.png)

## Save Intermediate Images
<https://github.com/AlUlkesh/sd_save_intermediate_images

Implements saving intermediate images, with more advanced features.

![image](https://user-images.githubusercontent.com/98228077/209453267-cb65adce-4e1c-45c7-93da-e0bd1020670c.png)

## openOutpaint extension
<https://github.com/zero01101/openOutpaint-webUI-extension

A tab with the full openOutpaint UI. Run with the --api flag.

![image](https://user-images.githubusercontent.com/98228077/209453250-8bd2d766-56b5-4887-97bc-cb0e22f98dde.png)

## Enhanced-img2img
<https://github.com/OedoSoldier/enhanced-img2img

An extension with support for batched and better inpainting.
