---
title: установить на Apple
layout: post
category: development
permalink: /install-on-apple/
machine_translated: true
lang: ru
---
Пользователи Mac: отправьте отзыв о том, работают ли эти инструкции для вас или нет, и если что-то неясно или у вас все еще есть проблемы с установкой, которые в настоящее время не [упомянуты здесь](https://github.com /AUTOMATIC1111/stable-diffusion-webui/discussions/5461).

Важные заметки
------
Currently most functionality in the web UI works correctly on macOS, with the most notable exceptions being CLIP interrogator and training. Although training does seem to work, it is incredibly slow and consumes an excessive amount of memory. CLIP interrogator can be used but it doesn't work correctly with the GPU acceleration macOS uses so the default configuration will run it entirely via CPU (which is slow).

Most samplers are known to work with the only exception being the PLMS sampler when using the Stable Diffusion 2.0 model. Generated images with GPU acceleration on macOS should usually match or almost match generated images on CPU with the same settings and seed.

Automatic installation
------

### Новая установка:
1. Если Homebrew не установлен, следуйте инструкциям на странице https://brew.sh, чтобы установить его. Держите окно терминала открытым и следуйте инструкциям в разделе «Следующие шаги», чтобы добавить Homebrew в PATH.
2. Откройте новое окно терминала и запустите `brew install cmake protobuf rust python@3.10 git wget`
3. Клонируйте репозиторий веб-интерфейса, запустив git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.
4. Поместите модели/контрольные точки Stable Diffusion, которые вы хотите использовать, в `stable-diffusion-webui/models/Stable-diffusion`. Если у вас их нет, см. [Загрузка моделей стабильной диффузии](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon#downloading-stable-diffusion-models) ниже.
5. `cd stable-diffusion-webui`, а затем `./webui.sh`, чтобы запустить веб-интерфейс. Виртуальная среда Python будет создана и активирована с помощью venv, а все оставшиеся недостающие зависимости будут автоматически загружены и установлены.
6. Чтобы перезапустить процесс веб-интерфейса позже, снова запустите `./webui.sh`. Обратите внимание, что веб-интерфейс не обновляется автоматически; для обновления запустите `git pull` перед запуском `./webui.sh`.

### Существующая установка:
Если у вас уже есть установка веб-интерфейса, созданная с помощью `setup_mac.sh`, удалите файл `run_webui_mac.sh` и папку `repositories` из папки `stable-diffusion-webui`. Затем запустите `git pull`, чтобы обновить веб-интерфейс, а затем `./webui.sh`, чтобы запустить его.

Загрузка моделей стабильной диффузии
------

If you don't have any models to use, Stable Diffusion models can be downloaded from [Hugging Face](https://huggingface.co/models?pipeline_tag=text-to-image&sort=downloads). To download, click on a model and then click on the `Files and versions` header. Look for files listed with the ".ckpt" or ".safetensors" extensions, and then click the down arrow to the right of the file size to download them.

Some popular official Stable Diffusion models are:
* [Stable DIffusion 1.4](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original) ([sd-v1-4.ckpt](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4.ckpt))
* [Stable Diffusion 1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) ([v1-5-pruned-emaonly.ckpt](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt))
* [Stable Diffusion 1.5 Inpainting](https://huggingface.co/runwayml/stable-diffusion-inpainting) ([sd-v1-5-inpainting.ckpt](https://huggingface.co/runwayml/stable-diffusion-inpainting/resolve/main/sd-v1-5-inpainting.ckpt))

Stable Diffusion 2.0 and 2.1 require both a model and a configuration file, and image width & height will need to be set to 768 or higher when generating images:
* [Stable Diffusion 2.0](https://huggingface.co/stabilityai/stable-diffusion-2) ([768-v-ema.ckpt](https://huggingface.co/stabilityai/stable-diffusion-2/resolve/main/768-v-ema.ckpt))
* [Stable Diffusion 2.1](https://huggingface.co/stabilityai/stable-diffusion-2-1) ([v2-1_768-ema-pruned.ckpt](https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.ckpt))

For the configuration file, hold down the option key on the keyboard and click [here](https://github.com/Stability-AI/stablediffusion/raw/main/configs/stable-diffusion/v2-inference-v.yaml) to download `v2-inference-v.yaml` (it may download as `v2-inference-v.yaml.yml`). In Finder select that file then go to the menu and select `File` > `Get Info`. In the window that appears select the filename and change it to the filename of the model, except with the file extension `.yaml` instead of `.ckpt`, press return on the keyboard (confirm changing the file extension if prompted), and place it in the same folder as the model (e.g. if you downloaded the `768-v-ema.ckpt` model, rename it to `768-v-ema.yaml` and put it in `stable-diffusion-webui/models/Stable-diffusion` along with the model).

Also available is a [Stable Diffusion 2.0 depth model](https://huggingface.co/stabilityai/stable-diffusion-2-depth) ([512-depth-ema.ckpt](https://huggingface.co/stabilityai/stable-diffusion-2-depth/resolve/main/512-depth-ema.ckpt)). Download the `v2-midas-inference.yaml` configuration file by holding down option on the keyboard and clicking [here](https://github.com/Stability-AI/stablediffusion/raw/main/configs/stable-diffusion/v2-midas-inference.yaml), then rename it with the `.yaml` extension in the same way as mentioned above and put it in `stable-diffusion-webui/models/Stable-diffusion` along with the model. Note that this model works at image dimensions of 512 width/height or higher instead of 768.

Troubleshooting
------

### Веб-интерфейс не запускается:
Если вы столкнулись с ошибками при попытке запустить веб-интерфейс с помощью `./webui.sh`, попробуйте удалить папки `repositories` и `venv` из папки `stable-diffusion-webui`, а затем обновите веб-интерфейс с помощью `git pull ` перед повторным запуском `./webui.sh`.

### Плохая работа:
В настоящее время ускорение GPU в macOS использует _lot_ памяти. Если производительность низкая (если для создания изображения 512x512 с 20 шагами с любым сэмплером требуется больше минуты), сначала попробуйте начать с параметра командной строки `--opt-split-attention-v1` (например, `./webui. sh --opt-split-attention-v1`) и посмотрите, поможет ли это. Если это не имеет большого значения, откройте приложение «Мониторинг активности», расположенное в /Applications/Utilities, и проверьте график нехватки памяти на вкладке «Память». Если нехватка памяти отображается красным цветом при создании изображения, закройте процесс веб-интерфейса, а затем добавьте параметр командной строки `--medvram` (например, `./webui.sh --opt-split-attention-v1 -- медврам`). Если производительность по-прежнему низкая, а нехватка памяти с этой опцией по-прежнему красная, то вместо этого попробуйте `--lowvram` (т.е. `./webui.sh --opt-split-attention-v1 --lowvram`). Если для создания изображения 512x512 с 20 шагами с любым сэмплером по-прежнему требуется больше нескольких минут, возможно, вам нужно отключить ускорение графического процессора. Откройте `webui-user.sh` в Xcode и измените `#export COMMANDLINE_ARGS=""` на `export COMMANDLINE_ARGS="--skip-torch-cuda-test --no-half --use-cpu all"`.

------

Discussions/Feedback here: https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/5461
