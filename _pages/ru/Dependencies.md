---
title: зависимости
layout: post
category: Getting started
permalink: /dependencies/
machine_translated: true
lang: ru
---
1. Python 3.10.6 и Git:
- Windows: загрузите и запустите установщики для Python 3.10.6 ([веб-страница](https://www.python.org/downloads/release/python-3106/), [exe](https://www.python.org /ftp/python/3.10.6/python-3.10.6-amd64.exe) или [версия win7](https://github.com/adang1345/PythonWin7/raw/master/3.10.6/python-3.10. 6-amd64-full.exe)) и git ([веб-страница](https://git-scm.com/download/win))
- Linux (на базе Debian): `sudo apt install wget git python3 python3-venv`
- Linux (на базе Red Hat): `sudo dnf install wget git python3`
- Linux (на базе Arch): `sudo pacman -S wget git python3`
2. Код из этого репозитория:
- предпочтительный способ: использование git: `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`.
- Этот способ упоминается, потому что он позволяет вам обновиться, просто запустив `git pull`.
- Эти команды можно использовать из окна командной строки, которое открывается после того, как вы щелкните правой кнопкой мыши в проводнике и выберите «Git Bash здесь».
- альтернативный способ: используйте опцию «Код» (зеленая кнопка) -> «Скачать ZIP» на главной странице репозитория.
- Вам все равно нужно установить git, даже если вы выберете это.
- Для обновления придется заново скачивать zip и заменять файлы.
3. Контрольную точку модели Stable Diffusion, файл с расширением `.ckpt`, необходимо загрузить и поместить в каталог `models/Stable-diffusion`.
- [Официальная загрузка] (https://huggingface.co/CompVis/stable-diffusion-v-1-4-original)
- [Файловое хранилище](https://drive.yerf.org/wl/?id=EBfTrmcCCUAGaQBXVIj5lJmEhjoP1tgl)
- Torrent (magnet:?xt=urn:btih:3a4a612d75ed088ea542acac52f9f45987488d1c&dn=sd-v1-4.ckpt&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org% 3а1337)

# Необязательные зависимости

## ESRGAN (Увеличение масштаба)
Модели ESRGAN, такие как модели из [базы данных моделей] (https://upscale.wiki/wiki/Model_Database), могут быть помещены в каталог ESRGAN.
Файл будет загружен как модель, если он имеет расширение `.pth`, и он будет отображаться под своим именем в пользовательском интерфейсе.

> Примечание. Модели RealESRGAN не являются моделями ESRGAN, они несовместимы. Не скачивайте модели RealESRGAN. Не помещайте RealESRGAN в каталог с моделями ESRGAN.

## Файлы .yaml для моделей SD 2.x

- 768-v-ema.ckpt [config](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference-v.yaml))

- 512-base-ema.ckpt [config](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference.yaml)

- 512-depth-ema.ckpt [config](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-midas-inference.yaml)

Загрузите файл конфигурации .yaml и сохраните его в той же папке, что и .ckpt с тем же именем.
