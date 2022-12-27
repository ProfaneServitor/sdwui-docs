---
title: Установить
priority: 0
category: Getting started
layout: post
permalink: /install/
machine_translated: true
lang: ru
---
Убедитесь, что необходимые [зависимости](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies) соблюдены, и следуйте инструкциям, доступным для обоих [NVidia](https://github.com/AUTOMATIC1111 /stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPU) (рекомендуется) и [AMD](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and -Run-on-AMD-GPUs) графические процессоры.

В качестве альтернативы используйте онлайн-сервисы (например, Google Colab):

- [Онлайн-сервисы](../Онлайн-сервисы)

### Автоматическая установка в Windows
1. Установите [Python 3.10.6](https://www.python.org/downloads/windows/), отметив «Добавить Python в PATH».
2. Установите [git](https://git-scm.com/download/win).
3. Загрузите репозиторий stable-diffusion-webui, например, запустив `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`.
4. Поместите `model.ckpt` в каталог `models` (см. [зависимости](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies), чтобы узнать, где его взять).
5. _*(Необязательно)*_ Поместите `GFPGANv1.4.pth` в базовый каталог вместе с `webui.py` (см. [зависимости](https://github.com/AUTOMATIC1111/stable-diffusion-webui/ wiki/Зависимости) для того, чтобы узнать, где его взять).
6. Запустите `webui-user.bat` из проводника Windows как обычный пользователь без прав администратора.

### Автоматическая установка в Linux
1. Установите зависимости:
```bash
# Debian-based:
sudo apt install wget git python3 python3-venv
# Red Hat-based:
sudo dnf install wget git python3
# Arch-based:
sudo pacman -S wget git python3
```
2. Чтобы установить в `/home/$(whoami)/stable-diffusion-webui/`, запустите:
```bash
bash <(wget -qO- https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh)
```

### Установка на Apple Silicon

Найдите инструкции [здесь](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon).
