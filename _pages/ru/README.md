---
title: Стабильный диффузионный веб-интерфейс
layout: home
category: Getting started
permalink: /
machine_translated: true
lang: ru
---
Интерфейс браузера на основе библиотеки Gradio для Stable Diffusion.

![](/sdwui-docs/assets/txt2img_Screenshot.jpg)

Проверьте вики-страницу [пользовательские сценарии](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Custom-Scripts) на наличие дополнительных сценариев, разработанных пользователями.

## Функции
[Подробная демонстрация функций с изображениями](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features):
- Оригинальные режимы txt2img и img2img
- Установить и запустить скрипт одним щелчком мыши (но вы все равно должны установить python и git)
- Окрашивание
- Покраска
- Цветной эскиз
- Матрица подсказок
- Стабильный диффузионный апскейл
- Внимание, укажите части текста, которым модель должна уделить больше внимания
- мужчина в ((смокинге)) - будет уделять больше внимания смокингу
- мужчина в (смокинг:1.21) - альтернативный синтаксис
- выберите текст и нажмите ctrl+up или ctrl+down, чтобы автоматически настроить внимание на выделенный текст (код предоставлен анонимным пользователем)
- Loopback, запустить обработку img2img несколько раз
- График X/Y, способ рисования двухмерного графика изображений с разными параметрами
- Текстовая инверсия
- иметь столько вложений, сколько хотите, и использовать для них любые имена, которые вам нравятся
- использовать несколько вложений с разным количеством векторов на токен
- работает с числами с плавающей запятой половинной точности
- тренируй вложения на 8гб (также отчеты о работе 6гб)
- Вкладка «Дополнительно» с:
- GFPGAN, нейронная сеть, фиксирующая лица
- CodeFormer, инструмент восстановления лица как альтернатива GFPGAN
- RealESRGAN, апскейлер нейронной сети
- ESRGAN, апскейлер нейронной сети с множеством сторонних моделей
- SwinIR и Swin2SR([см. здесь](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/2092)), апскейлеры нейронных сетей
- LDSR, повышение разрешения сверхвысокого разрешения со скрытой диффузией
- Изменение параметров соотношения сторон
- Выбор метода отбора проб
- Отрегулируйте значения eta сэмплера (множитель шума)
- Более продвинутые параметры настройки шума
- Прерывание обработки в любое время
- Поддержка видеокарты 4 ГБ (также сообщается о работе 2 ГБ)
- Правильные семена для партий
- Проверка длины токена подсказки в реальном времени
- Параметры генерации
- параметры, которые вы использовали для создания изображений, сохраняются вместе с этим изображением
- в чанках PNG для PNG, в EXIF ​​для JPEG
- можно перетащить изображение на вкладку информации PNG, чтобы восстановить параметры генерации и автоматически скопировать их в пользовательский интерфейс
- можно отключить в настройках
- перетащите изображение/текстовые параметры в окно подсказки
- Кнопка «Чтение параметров генерации», загружает параметры в поле подсказки в пользовательский интерфейс.
- Страница настроек
- Запуск произвольного кода Python из пользовательского интерфейса (для включения необходимо запустить с параметром --allow-code)
- Подсказки при наведении курсора для большинства элементов пользовательского интерфейса
- Можно изменить значения по умолчанию/микшер/максимум/шаг для элементов пользовательского интерфейса с помощью текстовой конфигурации.
- Кнопка случайного исполнителя
- Поддержка тайлинга, флажок для создания изображений, которые могут быть мозаичными, как текстуры.
- Индикатор выполнения и предварительный просмотр генерации живого изображения
- Отрицательное приглашение, дополнительное текстовое поле, которое позволяет вам перечислить то, что вы не хотите видеть в сгенерированном изображении.
- Стили, способ сохранить часть приглашения и легко применить их позже через раскрывающийся список
- Вариации, способ создания одного и того же изображения, но с небольшими отличиями.
- Изменение размера семени, способ создания того же изображения, но с немного другим разрешением
- Опросчик CLIP, кнопка, которая пытается угадать подсказку по изображению
- Редактирование подсказки, способ изменить подсказку в середине поколения, скажем, начать делать арбуз и переключиться на аниме-девушку на полпути.
- Пакетная обработка, обработка группы файлов с помощью img2img
- Img2img Альтернативный метод обратного Эйлера контроля перекрестного внимания
- Highres Fix, удобная опция для создания изображений высокого разрешения в один клик без обычных искажений
- Перезагрузка чекпоинтов на лету
- Checkpoint Merger, вкладка, позволяющая объединить до 3-х контрольных точек в одну
- [Пользовательские сценарии](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Custom-Scripts) со многими расширениями от сообщества
- [Composable-Diffusion](https://energy-based-model.github.io/Compositional-Visual-Generation-with-Composable-Diffusion-Models/), способ одновременного использования нескольких подсказок.
- разделяйте подсказки с помощью заглавной буквы `И`
- также поддерживает веса для подсказок: «кошка: 1,2 И собака И пингвин: 2,2»
- Нет лимита токенов для подсказок (оригинальная стабильная диффузия позволяет использовать до 75 токенов)
- Интеграция DeepDanbooru, создание тегов в стиле danbooru для подсказок аниме.
- [xformers](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Xformers), значительное увеличение скорости для некоторых карт: (добавьте --xformers в аргументы командной строки)
- через расширение: [вкладка «История»](https://github.com/yfszzx/stable-diffusion-webui-images-browser): удобно просматривать, направлять и удалять изображения в пользовательском интерфейсе.
- Создать навсегда вариант
- вкладка "Обучение"
- варианты гиперсетей и вложений
- Предварительная обработка изображений: обрезка, зеркальное отображение, автопометка с использованием BLIP или deepdanbooru (для аниме)
- Пропустить клип
- Используйте гиперсети
- Используйте VAE
- Расчетное время завершения в индикаторе выполнения
- API
- Поддержка выделенной [модели рисования](https://github.com/runwayml/stable-diffusion#inpainting-with-stable-diffusion) от RunwayML.
- через расширение: [Эстетические градиенты](https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients), способ создания изображений с определенной эстетикой с помощью встраивания изображений клипов (реализация [https: //github.com/vicgalle/stable-diffusion-aesthetic-gradients](https://github.com/vicgalle/stable-diffusion-aesthetic-gradients))
- Поддержка [Stable Diffusion 2.0](https://github.com/Stability-AI/stablediffusion) - см. [wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#stable- диффузия-20) по инструкции

## Установка и запуск
Убедитесь, что необходимые [зависимости](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies) соблюдены, и следуйте инструкциям, доступным для обоих [NVidia](https://github.com/AUTOMATIC1111 /stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPU) (рекомендуется) и [AMD](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and -Run-on-AMD-GPUs) графические процессоры.

В качестве альтернативы используйте онлайн-сервисы (например, Google Colab):

- [Список онлайн-сервисов](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Online-Services)

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

## Содействие
Вот как добавить код в этот репозиторий: [Contributing](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Contributing)

## Документация
Документация была перемещена из этого README в [вики] проекта (https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki).

## Кредиты
- Стабильная диффузия - https://github.com/CompVis/stable-diffusion, https://github.com/CompVis/taming-transformers
- k-диффузия - https://github.com/crowsonkb/k-diffusion.git
- GFPGAN - https://github.com/TencentARC/GFPGAN.git
- CodeFormer - https://github.com/sczhou/CodeFormer
- ЭСРГАН - https://github.com/xinntao/ESRGAN
- SwinIR - https://github.com/JingyunLiang/SwinIR
- Swin2SR - https://github.com/mv-lab/swin2sr
- ЛДСР - https://github.com/Hafiidz/latent-diffusion
- МиДаС - https://github.com/isl-org/MiDaS
- Идеи по оптимизации - https://github.com/basujindal/stable-diffusion
- Оптимизация слоя Cross Attention - Doggettx - https://github.com/Doggettx/stable-diffusion, оригинальная идея для оперативного редактирования.
- Оптимизация уровня перекрестного внимания - InvokeAI, lstein - https://github.com/invoke-ai/InvokeAI (первоначально http://github.com/lstein/stable-diffusion)
- Текстовая инверсия - Ринон Гал - https://github.com/rinongal/textual_inversion (мы не используем его код, но мы используем его идеи).
- Идея для апскейла SD - https://github.com/jquesnelle/txt2imghd
- Генерация шума для перекрашивания мк2 - https://github.com/parlance-zz/g-diffuser-bot
- Идея опросчика CLIP и заимствование кода - https://github.com/pharmapsychotic/clip-interrogator
- Идея компонуемой диффузии - https://github.com/energy-based-model/Compositional-Visual-Generation-with-Composable-Diffusion-Models-PyTorch
- xformers - https://github.com/facebookresearch/xformers
- DeepDanbooru - опросчик для аниме-диффузоров https://github.com/KichangKim/DeepDanbooru
- Совет по безопасности - RyotaK
- Исходный скрипт Gradio - опубликован на 4chan анонимным пользователем. Спасибо Анонимный пользователь.
- (Ты)
