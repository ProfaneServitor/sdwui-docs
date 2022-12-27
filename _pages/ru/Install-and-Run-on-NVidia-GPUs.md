---
title: установить на нвидиа
layout: post
category: Getting started
permalink: /install-on-nvidia/
machine_translated: true
lang: ru
---
Перед попыткой установки убедитесь, что все необходимые [зависимости] (зависимости) соблюдены.

# Автоматическая установка
## Окна
Запустите `webui-user.bat` из проводника Windows как обычно, ***не администратор***, пользователь.

См. раздел [Устранение неполадок](Устранение неполадок), чтобы узнать, что делать, если что-то пойдет не так.

## Линукс
Чтобы установить в каталог по умолчанию `/home/$(whoami)/stable-diffusion-webui/`, запустите:
```bash
bash <(wget -qO- https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh)
```

Чтобы настроить установку, клонируйте репозиторий в нужное место, измените необходимые переменные в `webui-user.sh` и запустите:
```bash
bash webui.sh
```

# Почти автоматическая установка и запуск
Чтобы установить необходимые пакеты через pip без создания виртуальной среды, запустите:
```bash
python launch.py
```

Аргументы командной строки могут быть переданы напрямую, например:
```bash
python launch.py --opt-split-attention --ckpt ../secret/anime9999.ckpt
```

# Ручная установка
Ручная установка очень устарела и, вероятно, не будет работать. проверьте colab в файле readme репо для получения инструкций.

Следующий процесс устанавливает все вручную как в Windows, так и в Linux (последний требует замены `dir` на `ls`):
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

Установка завершена, чтобы запустить веб-интерфейс, выполните:
```bash
python webui.py
```

# Инструкции по WSL2 для Windows 11
Чтобы установить в дистрибутиве Linux в Windows 11 WSL2:
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

На этом этапе можно применить инструкции по установке вручную, начиная с шага «# клонировать репозитории для Stable Diffusion и (необязательно) CodeFormer».


# Альтернативная установка в Windows с помощью Conda
- Предпосылки _*(Только если у вас их нет)*_. Предполагается, что [Chocolatey](https://chocolatey.org/install) установлен.
``` ударить
# установить гит
шоколад установить git
# установить конду
шоколад установить anaconda3
    ```

Необязательные параметры: [git](https://community.chocolatey.org/packages/git), [conda](https://community.chocolatey.org/packages/anaconda3)
- Установить (предупреждение: размер некоторых файлов превышает несколько гигабайт, сначала убедитесь, что у вас есть место)
1. Загрузите как .zip и распакуйте или используйте git для клонирования.
``` ударить
клон git https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
        ```

2. Запустите приглашение Anaconda. Следует отметить, что вы можете использовать более старые версии Python, но вам может потребоваться вручную удалить такие функции, как оптимизация кеша, что снизит вашу производительность.
``` ударить
# Перейдите в каталог git
cd "GIT\StableDiffusion"
# Создать среду
conda create -n StableDiffusion python=3.10.6
# Активировать среду
conda активирует StableDiffusion
# Подтвердить выбранную среду
список конвертов conda
# Запускаем локальный веб-сервер
webui-user.bat
# Дождитесь "Запуск по локальному URL-адресу: http://127.0.0.1:7860" и откройте этот URI.
        ```

3. _*(Необязательно)*_ Перейдите на [CompVis](https://huggingface.co/CompVis) и загрузите последнюю модель, например [1.4](https://huggingface.co/CompVis/stable-diffusion- v1-4) и распакуйте его в пример:
``` ударить
GIT\StableDiffusion\models\Stable-диффузия
        ```

после этого перезапустите сервер, перезапустив приглашение Anaconda и
``` ударить
webui-user.bat
        ```

- Альтернативные значения по умолчанию, которые стоит попробовать:
1. Попробуйте **euler a** (Ancestral Euler) с более высокими **шагами выборки**, например: 40 или другие со 100.
2. Установите для параметра «Настройки» > «Пользовательский интерфейс» > «Показывать ход создания образа через каждые N шагов выборки» значение 1 и выберите детерминированное значение **Исходное число**. Можно визуально увидеть, как происходит разделение изображений, и записать .gif с помощью [ScreenToGif] (https://github.com/NickeManarin/ScreenToGif).
3. Используйте **Восстановить лица**. Как правило, лучшие результаты, но это качество достигается за счет скорости.
