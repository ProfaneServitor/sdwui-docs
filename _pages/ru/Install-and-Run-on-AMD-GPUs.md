---
title: установить на амд
layout: post
category: development
permalink: /install-on-amd/
machine_translated: true
lang: ru
---
Инструкции ниже работают только в Linux! Альтернативное руководство для пользователя Windows можно найти [здесь](https://rentry.org/ayymd-stable-diffustion-v1_4-guide) (непроверено).

# Работает изначально

Выполните следующее:

```bash
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
cd stable-diffusion-webui
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip wheel

# It's possible that you don't need "--precision full", dropping "--no-half" however crashes my drivers
TORCH_COMMAND='pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/rocm5.1.1' python launch.py --precision full --no-half
```

В следующих прогонах вам нужно будет выполнить только:
```bash
cd stable-diffusion-webui
# Optional: "git pull" to update the repository
source venv/bin/activate

# It's possible that you don't need "--precision full", dropping "--no-half" however crashes my drivers
TORCH_COMMAND='pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/rocm5.1.1' python launch.py --precision full --no-half
```

Первое поколение после запуска WebUI может занять очень много времени, и вы можете увидеть сообщение, похожее на это:
> MIOpen(HIP): Предупреждение [SQLiteBase] Отсутствует файл системной базы данных: gfx1030_40.kdb Производительность может ухудшиться. Пожалуйста, следуйте
> инструкции по установке: https://github.com/ROCmSoftwarePlatform/MIOpen#installing-miopen-kernels-package

Следующие поколения должны работать с регулярной производительностью. Вы можете перейти по ссылке в сообщении, и если вдруг
чтобы использовать ту же операционную систему, выполните описанные здесь действия, чтобы устранить эту проблему. Если нет четкого способа компиляции или
установите ядра MIOpen для вашей операционной системы, рассмотрите возможность следования приведенному ниже руководству «Запуск внутри Docker».



# Запуск внутри Docker
Извлеките последний образ Docker `rocm/pytorch`, запустите образ и прикрепите его к контейнеру (взято из `rocm/pytorch`
документация): `docker run -it --network=host --device=/dev/kfd --device=/dev/dri --group-add=video --ipc=host
--cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v $HOME/dockerx:/dockerx rocm/pytorch`

Выполните следующее внутри контейнера:
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

Следующие запуски потребуют от вас только перезапустить контейнер, снова подключиться к нему и выполнить следующее внутри
container: найдите имя контейнера в этом списке: `docker container ls --all`, выберите тот, который соответствует
`rocm/pytorch`, перезапустите его: `docker container restart <container-id>`, затем подключитесь к нему: `docker exec -it
<идентификатор-контейнера> bash`.

```bash
cd /dockerx/stable-diffusion-webui
# Optional: "git pull" to update the repository
source venv/bin/activate

# It's possible that you don't need "--precision full", dropping "--no-half" however crashes my drivers
TORCH_COMMAND='pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/rocm5.1.1' REQS_FILE='requirements.txt' python launch.py --precision full --no-half
```

Папка `/dockerx` внутри контейнера должна быть доступна в вашем домашнем каталоге под тем же именем.

## Обновление версии Python внутри Docker
Если веб-интерфейс становится несовместимым с предустановленной версией Python 3.7 внутри образа Docker, вот
инструкции по его обновлению (при условии, что вы успешно выполнили «Запуск внутри Docker»):

Выполните следующее внутри контейнера:
```bash
apt install python3.9-full # Confirm every prompt
update-alternatives --install /usr/local/bin/python python /usr/bin/python3.9 1
echo 'PATH=/usr/local/bin:$PATH' >> ~/.bashrc
```

Затем перезапустите контейнер и снова подключитесь. Если вы проверите `python --version`, теперь должно быть написано `Python 3.9.5` или новее.

Запустите rm -rf /dockerx/stable-diffusion-webui/venv внутри контейнера, а затем следуйте инструкциям в разделе «Запуск внутри
Docker», пропуская «git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui» и используя модифицированный
вместо этого запустите команду ниже:

```bash
TORCH_COMMAND='pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/rocm5.1.1' python launch.py --precision full --no-half
```
Возможно, вам не нужно "--precision full", убрав "--no-half", однако это может не сработать для всех.
Некоторые карты, такие как Radeon RX 6000 Series и RX 500 Series, будут нормально работать без опции `--precision full --no-half`, что сэкономит много оперативной памяти. (отмечено [здесь](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/5468).)

С этого момента всегда используйте эту новую команду запуска, а также при перезапуске веб-интерфейса в следующих запусках.
