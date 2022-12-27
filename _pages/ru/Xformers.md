---
title: Иксформеры
layout: post
category: Guides
permalink: /xformers/
machine_translated: true
lang: ru
---
Библиотека Xformers — это дополнительный способ ускорить создание изображений.

Для винды нет бинарников кроме одной конкретной конфигурации, но собрать можно самому.

Гайд от анонимного пользователя, хотя я думаю он для сборки под линукс:

РУКОВОДСТВО ПО СОЗДАНИЮ XFORMERS
также включает в себя, как снять с себя ограничение sm86 на новый коммит voldy

1. перейдите в каталог webui
2. `источник ./venv/bin/активировать`
3. `CD репозиторий`
3. `клон git https://github.com/facebookresearch/xformers.git`
4. компакт-диски xformers
5. `git submodule update --init --recursive`
6. `pip install -r requirements.txt`
7. `pip install -e .`

## Сборка xFormers в Windows от [@duckness](https://github.com/duckness)

***



### Если вы используете карту Pascal, Turing, Ampere, Lovelace или Hopper с Python 3.10, вам больше не нужно собирать вручную. Удалите существующие xformers и запустите репозиторий с помощью `--xformers`. Будет установлено совместимое колесо.




***


1. [Установить VS Build Tools 2022](https://visualstudio.microsoft.com/downloads/?q=build+tools#build-tools-for-visual-studio-2022), вам нужна только `Разработка рабочего стола с C++ `

![setup_COFbK0AJAZ](https://user-images.githubusercontent.com/6380270/194767872-232136a1-9204-4b16-ae21-3e01f6f526ea.png)

2. [Установить CUDA 11.3](https://developer.nvidia.com/cuda-11.3.0-download-archive) (более поздние версии не тестировались), выбираем custom, нужно только следующее (интеграция с VS возможно не нужна ):

![setup_QwCdsQ28FM](https://user-images.githubusercontent.com/6380270/194767963-6df7ce14-e6eb-4718-8e93-a11abf172f14.png)

3. Клонируйте репозиторий xFormers (https://github.com/facebookresearch/xformers), создайте venv и активируйте его.

```sh
git clone https://github.com/facebookresearch/xformers.git
cd xformers
git submodule update --init --recursive
python -m venv venv
./venv/scripts/activate
```

4. Чтобы избежать проблем с получением версии процессора, [установите pyTorch отдельно](https://pytorch.org/get-started/locally/):

```sh
pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu113
```

5. Затем установите остальные зависимости:

```sh
pip install -r requirements.txt
pip install wheel
```

6. Поскольку CUDA 11.3 довольно старая, вам необходимо принудительно разрешить ее сборку в MS Build Tools 2022. Сделайте `$env:NVCC_FLAGS = "-allow-unsupported-compiler"`, если на `powershell`, или `установите NVCC_FLAGS =-allow-unsupported-compiler` если на `cmd`


7. Наконец-то можно собрать xFormers, учтите, что сборка займет много времени (вероятно, 10-20 минут), сначала может жаловаться на какие-то ошибки, но все равно должна компилироваться корректно.

> НЕОБЯЗАТЕЛЬНЫЙ совет: чтобы еще больше ускорить работу в системах Windows с многоядерными процессорами, установите ninja https://github.com/ninja-build/ninja.
> Шаги по установке:
> 1. Загрузите ninja-win.zip с https://github.com/ninja-build/ninja/releases и разархивируйте
> 2. Поместите ninja.exe в C:\Windows ИЛИ добавьте полный путь к извлеченному ninja.exe в системный PATH
> 3. Запустите ninja -h в cmd и проверьте, отображается ли справочное сообщение.
> 4. Запустите следующие команды, чтобы начать сборку. Он должен автоматически использовать Ninja, никаких дополнительных настроек не требуется. Вы должны увидеть значительно более высокую загрузку ЦП (40%+).
> ```

> сборка python setup.py
> python setup.py bdist_wheel
> ```

> Это сократило время сборки на ПК с Windows с процессором AMD 5800X с 1,5 часов до 10 минут.
> Ninja также поддерживается в Linux и MacOS, но у меня нет этих ОС для тестирования, поэтому я не могу предоставить пошаговое руководство.



8. Запустите следующее:
``ш
сборка python setup.py
python setup.py bdist_wheel
```

9. In `xformers` directory, navigate to the `dist` folder and copy the `.whl` file to the base directory of `stable-diffusion-webui`

10. In `stable-diffusion-webui` directory, install the `.whl`, change the name of the file in the command below if the name is different:

```sh
./venv/скрипты/активировать
pip установить xformers-0.0.14.dev0-cp310-cp310-win_amd64.whl
```

11. Ensure that `xformers` is activated by launching `stable-diffusion-webui` with `--force-enable-xformers`

## Non-deterministic / unstable / inconsistent results:

Known issue. See [this](https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/2705#discussioncomment-4024378 ) list on the discussion page.
