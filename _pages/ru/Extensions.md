---
title: Расширения
layout: post
category: Guides
permalink: /extensions/
handles: /extensions/
machine_translated: true
lang: ru
---
# Главная информация

Расширения представляют собой более удобную форму пользовательских скриптов.

Все расширения существуют в своих собственных подкаталогах внутри каталога `extensions`. Вы можете использовать git для установки расширения следующим образом:

```
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients extensions/aesthetic-gradients
```

Это устанавливает расширение из `https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients` в каталог `extensions/aesthetic-gradients`.

В качестве альтернативы вы можете просто скопировать и вставить каталог в «extensions».

Для разработки расширений см. [Разработка расширений](Developing-extensions).

# Безопасность

Поскольку расширения позволяют пользователю устанавливать и запускать произвольный код, это может быть использовано злонамеренно и отключено по умолчанию при работе с параметрами, позволяющими удаленным пользователям подключаться к серверу (`--share` или `--listen`). у вас все еще будет пользовательский интерфейс, но попытка установить что-либо приведет к ошибке. Если вы хотите использовать эти параметры и по-прежнему иметь возможность устанавливать расширения, используйте флаг командной строки `--enable-insecure-extension-access`.

# Расширения

## Эстетические градиенты
https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-градиенты

Создайте вложение из одного или нескольких изображений и используйте его, чтобы применить их стиль к сгенерированным изображениям.

![firefox_FgKg9dx9eF](https://user-images.githubusercontent.com/20920490/197466300-6b042bcf-5cba-4600-97d7-ad2652875706.png)

## Подстановочные знаки
https://github.com/AUTOMATIC1111/stable-diffusion-webui-wildcards

Позволяет вам использовать синтаксис `__name__` в приглашении для получения случайной строки из файла с именем `name.txt` в каталоге подстановочных знаков.

## Динамические подсказки
https://github.com/adieyal/sd-динамические-подсказки

Пользовательское расширение для [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), которое реализует выразительный язык шаблонов для генерации случайных или комбинаторных подсказок, а также функции для поддержки глубокого каталога подстановочных знаков. структуры.

Дополнительные функции и дополнения показаны в [readme](https://github.com/adieyal/sd-dynamic-prompts).

![изображение](https://github.com/adieyal/sd-dynamic-prompts/raw/main/images/extension.png)

Используя это расширение, подсказка:

`{дом|квартира|домик|коттедж} {летом|зимой|осенью|весной} от {2$$artist1|artist2|artist3}`

Будут ли какие-либо из следующих подсказок:

- Летний домик художника1, художника2
- Домик осенью от artist3, artist1
- Коттедж зимой художник2, художник3
- ...


Это особенно полезно, если вы ищете интересные сочетания исполнителей и стилей.

Вы также можете выбрать случайную строку из файла. Предполагая, что у вас есть файл Seasons.txt в WILDCARD_DIR (см. ниже), тогда:

`__seasons__ приближается`

Может генерировать следующее:

- Зима близко
- Весна идет
- ...


Вы также можете использовать один и тот же подстановочный знак дважды.

`Я люблю __seasons__ больше, чем __seasons__`

- Я люблю зиму больше, чем лето
- Я люблю весну больше, чем весну

## Будка мечты
https://github.com/d8ahazard/sd_dreambooth_extension

Dreambooth в пользовательском интерфейсе. Требования к настройке и конфигурации см. в файле readme проекта. Включает [LoRA] (https://github.com/cloneofsimo/lora) (адаптация низкого ранга)

На основе репозитория ShivamShiaro.

![изображение](https://user-images.githubusercontent.com/1633844/201434706-2c2744ba-082e-427e-9f8d-af03de204583.png)


## Умный процесс
https://github.com/d8ahazard/sd_smartprocess

Интеллектуальная обрезка, добавление подписей и улучшение изображений.

![изображение](https://user-images.githubusercontent.com/1633844/201435094-433d765c-56e8-4573-82d9-71af2b112159.png)


## Браузер изображений
https://github.com/yfszzx/stable-diffusion-webui-images-browser

Предоставляет интерфейс для просмотра созданных изображений в веб-браузере.

![68747470733a2f2f73362e6a70672e636d2f323032322f31302f32342f504a6a755a742e706e67](https://user-images.githubusercontent.com/20920490/197518762-a23f3e34-f174-4275-8283-eb8d2ff65ef2.png)

## Вдохновение
https://github.com/yfszzx/stable-diffusion-webui-inspiration

Произвольное отображение изображений типичного стиля художника или художественного жанра, после выбора отображается больше изображений этого художника или жанра. Так что вам не нужно беспокоиться о том, как сложно выбрать правильный стиль искусства при создании.

![68747470733a2f2f73362e6a70672e636d2f323032322f31302f32322f504a596f4e4c2e706e67](https://user-images.githubusercontent.com/20920490/197518700-3f753132-8799-4ad0-8cdf-bcdcbf7798aa.png)

## Ниже
https://github.com/deforum-art/deforum-for-automatic1111-webui


Официальный порт Deforum, обширный скрипт для 2D- и 3D-анимации, поддерживающий последовательности ключевых кадров, динамические математические параметры (даже внутри подсказок), динамическое маскирование, оценку глубины и деформацию.

![ui](https://user-images.githubusercontent.com/20920490/197619558-c088a329-3672-4f0a-8685-cf539996ad1e.png)

## Художники для изучения
https://github.com/camenduru/stable-diffusion-webui-artists-to-study

https://artiststostudy.pages.dev/ адаптировано под расширение для [веб-интерфейса](https://github.com/AUTOMATIC1111/stable-diffusion-webui).

Чтобы установить его, клонируйте репозиторий в каталог «extensions» и перезапустите веб-интерфейс:

`git clone https://github.com/camenduru/stable-diffusion-webui-artists-to-study`

Вы можете добавить имя исполнителя в буфер обмена, нажав на него. (спасибо за идею @gmaciocci)

![изображение](https://user-images.githubusercontent.com/54370274/197829512-e7d30d44-2697-4ecd-b9a7-3665217918c7.jpg)

## Оценщик эстетических изображений
https://github.com/tsngo/stable-diffusion-webui-aesthetic-image-scorer

Расширение для https://github.com/AUTOMATIC1111/stable-diffusion-webui

Вычисляет эстетическую оценку для сгенерированных изображений с помощью [предиктора эстетической оценки CLIP+MLP] (https://github.com/christophschuhmann/improved-aesthetic-predictor) на основе [оценщика Чада] (https://github.com/grexzen/SD). -Чад/blob/main/chad_scorer.py)

См. [Обсуждения] (https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/1831).

Сохраняет счет в тегах Windows с другими запланированными параметрами

![изображение](https://github.com/tsngo/stable-diffusion-webui-aesthetic-image-scorer/blob/main/tag_group_by.png)

## Редактор тегов набора данных
https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor

[Японский файл Readme] (https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor/blob/main/README-JP.md)

Это расширение для редактирования подписей в обучающем наборе данных для [веб-интерфейса Stable Diffusion от AUTOMATIC1111] (https://github.com/AUTOMATIC1111/stable-diffusion-webui).

Он хорошо работает с текстовыми подписями в стиле, разделенном запятыми (например, теги, сгенерированные запросчиком DeepBooru).

Подписи в именах файлов изображений могут быть загружены, но отредактированные подписи могут быть сохранены только в виде текстовых файлов.

![изображение](https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor/blob/main/ss01.png)

## auto-sd-paint-ext

https://github.com/Interpause/auto-sd-paint-ext

Ранее известный как «auto-sd-krita».

> Расширение веб-интерфейса AUTOMATIC1111 с плагином Krita (скоро появятся другие студии рисования?)

Устаревшая демо | Новый пользовательский интерфейс (ВСЕ: демонстрационное изображение)
--- | ---
![demo image](https://user-images.githubusercontent.com/42513874/194701722-e7a3f7eb-be4a-4f43-93a5-480835c9260f.jpg) | ![demo image 2](https://user-images.githubusercontent.com/42513874/199507299-66729f9b-3581-43a3-b5f4-57eb90b8f981.png)

**Differences**

- UI no longer freezes during image update
- Inpainting layer no longer has to be manually hidden, nor use white specifically
- UI has been improved & squeezed further
- Scripts API is now possible

## training-picker
https://github.com/Maurdekye/training-picker

Adds a tab to the webui that allows the user to automatically extract keyframes from video, and manually extract 512x512 crops of those frames for use in model training.

![image](https://user-images.githubusercontent.com/2313721/199614791-1f573573-a2e2-4358-836d-5655825077e1.png)

**Installation**

- Install [AUTOMATIC1111's Stable Diffusion Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- Install [ffmpeg](https://ffmpeg.org/) for your operating system
- Clone this repository into the extensions folder inside the webui
- Drop videos you want to extract cropped frames from into the training-picker/videos folder

## Unprompted
https://github.com/ThereforeGames/unprompted

Supercharge your prompt workflow with this powerful scripting language!

![unprompted_header](https://user-images.githubusercontent.com/95403634/199041569-7c6c5748-e7dc-4068-943f-c2d92745dbb5.png)

**Unprompted** is a highly modular extension for [AUTOMATIC1111's Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) that allows you to include various shortcodes in your prompts. You can pull text from files, set up your own variables, process text through conditional functions, and so much more - it's like wildcards on steroids.

While the intended usecase is Stable Diffusion, **this engine is also flexible enough to serve as an all-purpose text generator.**

## Booru tag autocompletion
https://github.com/DominikDoom/a1111-sd-webui-tagcomplete

Displays autocompletion hints for tags from "image booru" boards such as Danbooru. Uses local tag CSV files and includes a config for customization.

![image](https://user-images.githubusercontent.com/20920490/200016417-9451efdb-5d0d-4131-bd9e-39a687be8dd7.png)

## novelai-2-local-prompt
https://github.com/animerl/novelai-2-local-prompt

Add a button to convert the prompts used in NovelAI for use in the WebUI. In addition, add a button that allows you to recall a previously used prompt.

![pic](https://user-images.githubusercontent.com/113022648/197382468-65f4a96d-48af-4890-8fcf-0ec7c3b9ec3a.png)

## Tokenizer
https://github.com/AUTOMATIC1111/stable-diffusion-webui-tokenizer

Adds a tab that lets you preview how CLIP model would tokenize your text.

![about](https://user-images.githubusercontent.com/20920490/200113798-50b55f5a-45db-4b6f-93c0-ae6be75e5788.png)

## Push to 🤗 Hugging Face

https://github.com/camenduru/stable-diffusion-webui-huggingface

![Push Folder to Hugging Face](https://user-images.githubusercontent.com/54370274/206897701-9e86ce7c-af06-4d95-b9ea-385276c99d3a.jpg)

To install it, clone the repo into the `extensions` directory and restart the web ui:

`git clone https://github.com/camenduru/stable-diffusion-webui-huggingface`

`pip install huggingface-hub`

## StylePile
https://github.com/some9000/StylePile

An easy way to mix and match elements to prompts that affect the style of the result.

![image](https://user-images.githubusercontent.com/98228077/208331056-2956d050-a7a4-4b6f-b064-72f6a7d7ee0d.png)

## Latent Mirroring
https://github.com/dfaker/SD-latent-mirroring

Applies mirroring and flips to the latent images to produce anything from subtle balanced compositions to perfect reflections

![image](https://user-images.githubusercontent.com/98228077/208331098-3b7fefce-6d38-486d-9543-258f5b2b0fd6.png)

## Embeddings editor
https://github.com/CodeExplode/stable-diffusion-webui-embedding-editor

Allows you to manually edit textual inversion embeddings using sliders.

![image](https://user-images.githubusercontent.com/98228077/208331138-cdfe8f43-78f7-499e-b746-c42355ee8d6d.png)

## seed travel
https://github.com/yownas/seed_travel

Small script for AUTOMATIC1111/stable-diffusion-webui to create images that exists between seeds.

<img src="https://github.com/ClashSAN/bloated-gifs/blob/main/seedtravel.gif" width="512" height="512" />

## shift-attention
https://github.com/yownas/shift-attention

Generate a sequence of images shifting attention in the prompt. This script enables you to give a range to the weight of tokens in a prompt and then generate a sequence of images stepping from the first one to the second.

https://user-images.githubusercontent.com/13150150/193368939-c0a57440-1955-417c-898a-ccd102e207a5.mp4

## prompt travel
https://github.com/Kahsolt/stable-diffusion-webui-prompt-travel

Extension script for AUTOMATIC1111/stable-diffusion-webui to travel between prompts in latent space.

<img src="https://github.com/ClashSAN/bloated-gifs/blob/main/prompt_travel.gif" width="512" height="512" />

## Sonar
https://github.com/Kahsolt/stable-diffusion-webui-sonar

Improve the generated image quality, searches for similar (yet even better!) images in the neighborhood of some known image, focuses on single prompt optimization rather than traveling between multiple prompts.

![image](https://user-images.githubusercontent.com/98228077/209545702-c796a3f8-4d8c-4e2b-9b2e-920008ec2f32.png)![image](https://user-images.githubusercontent.com/98228077/209545756-31c94fec-d783-447f-8aac-4a5bba43ea15.png)

## Detection Detailer
https://github.com/dustysys/ddetailer

An object detection and auto-mask extension for Stable Diffusion web UI.

<img src="https://github.com/dustysys/ddetailer/raw/master/misc/ddetailer_example_3.gif"/>

## conditioning-highres-fix
https://github.com/klimaleksus/stable-diffusion-webui-conditioning-highres-fix

This is Extension for rewriting Inpainting conditioning mask strength value relative to Denoising strength at runtime. This is useful for Inpainting models such as sd-v1-5-inpainting.ckpt

![image](https://user-images.githubusercontent.com/98228077/208331374-5a271cf3-cfac-449b-9e09-c63ddc9ca03a.png)

## Randomize
https://github.com/stysmmaker/stable-diffusion-webui-randomize

Allows for random parameters during txt2img generation. This script is processed for all generations, regardless of the script selected, meaning this script will function with others as well, such as AUTOMATIC1111/stable-diffusion-webui-wildcards.

## Auto TLS-HTTPS
https://github.com/papuSpartan/stable-diffusion-webui-auto-tls-https

Allows you to easily, or even completely automatically start using HTTPS.

## DreamArtist
https://github.com/7eu7d7/DreamArtist-sd-webui-extension

Towards Controllable One-Shot Text-to-Image Generation via Contrastive Prompt-Tuning.

![image](https://user-images.githubusercontent.com/98228077/208331536-069783ae-32f7-4897-8c1b-94e0ae14f9cd.png)

## WD 1.4 Tagger
https://github.com/toriato/stable-diffusion-webui-wd14-tagger

Uses a trained model file, produces WD 1.4 Tags. Model link - https://mega.nz/file/ptA2jSSB#G4INKHQG2x2pGAVQBn-yd_U5dMgevGF8YYM9CR_R1SY

![image](https://user-images.githubusercontent.com/98228077/208331569-2cf82c5c-f4c3-4181-84bd-2bdced0c2cff.png)

## booru2prompt
https://github.com/Malisius/booru2prompt

This SD extension allows you to turn posts from various image boorus into stable diffusion prompts. It does so by pulling a list of tags down from their API. You can copy-paste in a link to the post you want yourself, or use the built-in search feature to do it all without leaving SD.

![image](https://user-images.githubusercontent.com/98228077/208331612-dad61ef7-33dd-4008-9cc7-06b0b0a7cb6d.png)

also see:\
https://github.com/stysmmaker/stable-diffusion-webui-booru-prompt

## gelbooru-prompt
https://github.com/antis0007/sd-webui-gelbooru-prompt

Fetch tags with image hash. Updates planned.

## Merge Board
https://github.com/bbc-mc/sdweb-merge-board

Multiple lane merge support(up to 10). Save and Load your merging combination as Recipes, which is simple text.

![image](https://user-images.githubusercontent.com/98228077/208331651-09a0d70e-1906-4f80-8bc1-faf3c0ca8fad.png)

also see:\
https://github.com/Maurdekye/model-kitchen

## Depth Maps
https://github.com/thygate/stable-diffusion-webui-depthmap-script

Creates depthmaps from the generated images. The result can be viewed on 3D or holographic devices like VR headsets or lookingglass display, used in Render or Game- Engines on a plane with a displacement modifier, and maybe even 3D printed.

![image](https://user-images.githubusercontent.com/98228077/208331747-9acba3f0-3039-485e-96ab-f0cf5619ec3b.png)

## multi-subject-render
https://github.com/Extraltodeus/multi-subject-render

It is a depth aware extension that can help to create multiple complex subjects on a single image. It generates a background, then multiple foreground subjects, cuts their backgrounds after a depth analysis, paste them onto the background and finally does an img2img for a clean finish.

![image](https://user-images.githubusercontent.com/98228077/208331952-019dfd64-182d-4695-bdb0-4367c81e4c43.png)

## depthmap2mask
https://github.com/Extraltodeus/depthmap2mask

Create masks for img2img based on a depth estimation made by MiDaS.

![image](https://user-images.githubusercontent.com/15731540/204050868-eca8db02-2193-4115-a5b8-e8f5c796e035.png)![image](https://user-images.githubusercontent.com/15731540/204050888-41b00335-50b4-4328-8cfd-8fc5e9cec78b.png)![image](https://user-images.githubusercontent.com/15731540/204050899-8757b774-f2da-4c15-bfa7-90d8270e8287.png)

## ABG_extension
https://github.com/KutsuyaYuki/ABG_extension

Automatically remove backgrounds. Uses an onnx model fine-tuned for anime images. Runs on GPU.

| ![test](https://user-images.githubusercontent.com/98228077/209423352-e8ea64e7-8522-4c2c-9350-c7cd50c35c7c.png) |  ![00035-4190733039-cow](https://user-images.githubusercontent.com/98228077/209423400-720ddde9-258a-4e68-8a93-73b67dad714e.png) | ![00021-1317075604-samdoesarts portrait](https://user-images.githubusercontent.com/98228077/209423428-da7c68db-e7d1-45a1-b931-817de9233a67.png) | ![00025-2023077221-](https://user-images.githubusercontent.com/98228077/209423446-79e676ae-460e-4282-a591-b8b986bfd869.png) |
| :---: | :---: | :---: | :---: |
| ![img_-0002-3313071906-bust shot of person](https://user-images.githubusercontent.com/98228077/209423467-789c17ad-d7ed-41a9-a039-802cfcae324a.png) | ![img_-0022-4190733039-cow](https://user-images.githubusercontent.com/98228077/209423493-dcee7860-a09e-41e0-9397-715f52bdcaab.png) | ![img_-0008-1317075604-samdoesarts portrait](https://user-images.githubusercontent.com/98228077/209423521-736f33ca-aafb-4f8b-b067-14916ec6955f.png) | ![img_-0012-2023077221-](https://user-images.githubusercontent.com/98228077/209423546-31b2305a-3159-443f-8a98-4da22c29c415.png) |

## Visualize Cross-Attention
https://github.com/benkyoujouzu/stable-diffusion-webui-visualize-cross-attention-extension

![image](https://user-images.githubusercontent.com/98228077/208332131-6acdae9a-2b25-4e71-8ab0-6e375c7c0419.png)

Generates highlighted sectors of a submitted input image, based on input prompts. Use with tokenizer extension. See the readme for more info.

## DAAM
https://github.com/kousw/stable-diffusion-webui-daam

DAAM stands for Diffusion Attentive Attribution Maps. Enter the attention text (must be a string contained in the prompt) and run. An overlapping image with a heatmap for each attention will be generated along with the original image.

![image](https://user-images.githubusercontent.com/98228077/208332173-ffb92131-bd02-4a07-9531-136822d06c86.png)

## Prompt Gallery
https://github.com/dr413677671/PromptGallery-stable-diffusion-webui

Build a yaml file filled with prompts of your character, hit generate, and quickly preview them by their word attributes and modifiers.

![image](https://user-images.githubusercontent.com/98228077/208332199-7652146c-2428-4f44-9011-66e81bc87426.png)

## embedding-inspector
https://github.com/tkalayci71/embedding-inspector

Inspect any token(a word) or Textual-Inversion embeddings and find out which embeddings are similar. You can mix, modify, or create the embeddings in seconds. Much more intriguing options have since been released, see [here.](https://github.com/tkalayci71/embedding-inspector#whats-new)

![image](https://user-images.githubusercontent.com/98228077/209546038-3f4206bf-2c43-4d58-bf83-6318ade393f4.png)

## Infinity Grid Generator
https://github.com/mcmonkeyprojects/sd-infinity-grid-generator-script

Build a yaml file with your chosen parameters, and generate infinite-dimensional grids. Built-in ability to add description text to fields. See readme for usage details.

![image](https://user-images.githubusercontent.com/98228077/208332269-88983668-ea7e-45a8-a6d5-cd7a9cb64b3a.png)

## NSFW checker
https://github.com/AUTOMATIC1111/stable-diffusion-webui-nsfw-censor

Replaces NSFW images with black.

## Diffusion Defender
https://github.com/WildBanjos/DiffusionDefender

Prompt blacklist, find and replace, for semi-private and public instances.

## Config-Presets
https://github.com/Zyin055/Config-Presets

Adds a configurable dropdown to allow you to change UI preset settings in the txt2img and img2img tabs.

![image](https://user-images.githubusercontent.com/98228077/208332322-24339554-0274-4add-88a7-d33bba1e3823.png)

## Preset Utilities
https://github.com/Gerschel/sd_web_ui_preset_utils

Preset tool for UI. Planned support for some other custom scripts.

![image](https://user-images.githubusercontent.com/98228077/209540881-2a870282-edb6-4c94-869b-5493cdced01f.png)

## DH Patch
https://github.com/d8ahazard/sd_auto_fix

Random patches by D8ahazard. Auto-load config YAML files for v2, 2.1 models; patch latent-diffusion to fix attention on 2.1 models (black boxes without no-half), whatever else I come up with.

## Riffusion
https://github.com/enlyth/sd-webui-riffusion

Use Riffusion model to produce music in gradio. To replicate [original](https://www.riffusion.com/about) interpolation technique, input the [prompt travel extension](https://github.com/Kahsolt/stable-diffusion-webui-prompt-travel) output frames into the riffusion tab.

![image](https://user-images.githubusercontent.com/98228077/209539460-f5c23891-b5e6-46c7-b1a5-b7440a3f031b.png)![image](https://user-images.githubusercontent.com/98228077/209539472-031e623e-f7a2-4da9-9711-8bf73d0cfe6e.png)

## Save Intermediate Images
https://github.com/AlUlkesh/sd_save_intermediate_images

Implements saving intermediate images, with more advanced features.

![image](https://user-images.githubusercontent.com/98228077/209453267-cb65adce-4e1c-45c7-93da-e0bd1020670c.png)

## openOutpaint extension
https://github.com/zero01101/openOutpaint-webUI-extension

A tab with the full openOutpaint UI. Run with the --api flag.

![image](https://user-images.githubusercontent.com/98228077/209453250-8bd2d766-56b5-4887-97bc-cb0e22f98dde.png)

## Enhanced-img2img
https://github.com/OedoSoldier/enhanced-img2img

An extension with support for batched and better inpainting.
