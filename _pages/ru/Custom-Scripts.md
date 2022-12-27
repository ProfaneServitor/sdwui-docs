---
title: Пользовательские скрипты
layout: post
category: Guides
permalink: /custom-scripts/
machine_translated: true
lang: ru
---
# Установка и использование пользовательских скриптов
Чтобы установить пользовательские сценарии, поместите их в каталог `scripts` и нажмите кнопку `Обновить пользовательский сценарий` внизу на вкладке настроек. Пользовательские сценарии появятся в раскрывающемся меню в левом нижнем углу на вкладках txt2img и img2img после установки. Ниже приведены некоторые известные пользовательские сценарии, созданные пользователями веб-интерфейса:

# Пользовательские сценарии от пользователей

## Улучшенная матрица подсказок
https://github.com/ArrowM/auto1111-улучшенная-подсказка-матрица

Этот скрипт [advanced-prompt-matrix](https://github.com/GRMrGecko/stable-diffusion-webui-automatic/blob/advanced_matrix/scripts/advanced_prompt_matrix.py) изменен для поддержки `пакетного подсчета`. Сетки не создаются.

**Применение:**

Используйте `<` `>`, чтобы создать группу альтернативных текстов. Разделяйте параметры текста символом `|`. Можно использовать несколько групп и несколько вариантов. Например:

Ввод `<корги|кошка> в <очках|шляпе>`
Будет выведено 4 подсказки: «корги в очках», «корги в шляпе», «кот в очках», «кот в шляпе».

При использовании `количества пакетов` > 1 каждый вариант подсказки будет создан для каждого начального числа. `размер пакета` игнорируется.

## txt2img2img
https://github.com/ThereforeGames/txt2img2img

Значительно улучшите возможность редактирования любого персонажа/объекта, сохранив при этом их сходство. Основной мотивацией для этого скрипта является улучшение возможности редактирования вложений, созданных с помощью [текстовой инверсии](https://textual-inversion.github.io/).

(будьте осторожны с клонированием, так как оно немного проверено)

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/98228077/200106431-21a22657-db24-4e9c-b7fa-e3a8e9096b89.png" width="624" height="312" />
</details>

## txt2маска
https://github.com/ThereforeGames/txt2mask

Позволяет указать маску рисования с текстом, а не с кистью.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/95403634/190878562-d020887c-ccb0-411c-ab37-38e2115552eb.png" ширина="674" высота="312" />
</details>

## Интерфейс рисования маски
https://github.com/dfaker/stable-diffusion-webui-cv2-external-masking-script

Предоставляет локальное всплывающее окно на основе CV2, которое позволяет добавить маску перед обработкой.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/98228077/200109495-3d6741f1-0e25-4ae5-9f84-d93f886f302a.png" width="302" height="312" />
</details>

## Img2img видео
https://github.com/memes-forever/Stable-diffusion-webui-video

Используя img2img, генерирует картинки одну за другой.

## Путешествие с семенами
https://github.com/yownas/seed_travel

Выберите два (или более) начальных значения и сгенерируйте последовательность изображений, интерполируя их. При желании, пусть он создаст видео результата.

Пример того, что вы можете с ним сделать:
https://www.youtube.com/watch?v=4c71iUclY4U

<details><summary>Другой пример пользователя:</summary>
<img src="https://github.com/ClashSAN/bloated-gifs/blob/main/seedtravel.gif" width="512" height="512" />
</details>

## Расширенное смешивание семян
https://github.com/amotile/stable-diffusion-backend/tree/master/src/process/implementations/automatic1111_scripts

Этот сценарий позволяет вам основывать начальный шум на нескольких взвешенных начальных значениях.

Бывший. `seed1:2, seed2:1, seed3:1`

Веса нормализованы, поэтому вы можете использовать больше, как указано выше, или вы можете использовать числа с плавающей запятой:

Бывший. `seed1: 0,5, seed2: 0,25, seed3: 0,25`

## Быстрое смешивание
https://github.com/amotile/stable-diffusion-backend/tree/master/src/process/implementations/automatic1111_scripts

Этот скрипт позволяет вам объединять несколько взвешенных подсказок, математически комбинируя их текстовые вложения перед созданием изображения.

Бывший.
{% raw %}
`Кристалл, содержащий элементаль {огонь|лед}`

Он поддерживает вложенные определения, поэтому вы также можете сделать это:

`Кристалл, содержащий элементаль {{огонь:5|лед}|земля}`
{% endraw %}
## Аниматор
https://github.com/Аниматор-Анон/Аниматор

Базовый скрипт img2img, который выгружает кадры и создает видеофайл. Подходит для создания интересного зума в фильмах с деформацией, но в настоящее время не более того.

## Секвенсор параметров
https://github.com/rewbs/sd-parseq

Создавайте видео с жестким контролем и гибкой интерполяцией по многим параметрам Stable Diffusion (таким как начальное число, масштаб, быстрые веса, сила шумоподавления...), а также параметрам входной обработки (таким как масштабирование, панорамирование, 3D-поворот...)

## Альтернативные расписания шума
https://gist.github.com/dfaker/f88aa62e3a14b559fe4e5f6b345db664

Использует альтернативные генераторы для графика сигма сэмплера.

Предоставляет доступ к графикам Karras, Exponential и Variance Preserving из crowsonkb/k-diffusion вместе с их параметрами.

## Vid2Vid
https://github.com/Filarius/stable-diffusion-webui/blob/master/scripts/vid2vid.py

Из реального видео, img2img кадры и склеить их вместе. Не распаковывает кадры на жесткий диск.

## Txt2VectorGraphics
https://github.com/GeorgLegato/Txt2Vectorgraphics

Создавайте настраиваемые масштабируемые значки из подсказок в формате SVG или PDF.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>

| приглашение |PNG |SVG |
| :-------- | :-----------------: | :----------------------------------: |
| Счастливый Эйнштейн | <img src="https://user-images.githubusercontent.com/7210708/193370360-506eb6b5-4fa7-4b2a-9fec-6430f6d027f5.png" width="40%" /> | <img src="https://user-images.githubusercontent.com/7210708/193370379-2680aa2a-f460-44e7-9c4e-592cf096de71.svg" width=30%/> |
| Скоростной спуск на горном велосипеде | <img src="https://user-images.githubusercontent.com/7210708/193371353-f0f5ff6f-12f7-423b-a481-f9bd119631dd.png" width=40%/> | <img src="https://user-images.githubusercontent.com/7210708/193371585-68dea4ca-6c1a-4d31-965d-c1b5f145bb6f.svg" width=30%/> |
кофейная кружка в форме сердца | <img src="https://user-images.githubusercontent.com/7210708/193374299-98379ca1-3106-4ceb-bcd3-fa129e30817a.png" width=40%/> | <img src="https://user-images.githubusercontent.com/7210708/193374525-460395af-9588-476e-bcf6-6a8ad426be8e.svg" width=30%/> |
| Наушники | <img src="https://user-images.githubusercontent.com/7210708/193376238-5c4d4a8f-1f06-4ba4-b780-d2fa2e794eda.png" width=40%/> | <img src="https://user-images.githubusercontent.com/7210708/193376255-80e25271-6313-4bff-a98e-ba3ae48538ca.svg" width=30%/> |

</details>

## Переключение внимания
https://github.com/yownas/shift-внимание

Создайте последовательность изображений, переключающих внимание в подсказке.

Этот сценарий позволяет указать диапазон веса жетонов в подсказке, а затем сгенерировать последовательность изображений, переходя от первого ко второму.

## Зацикливание и наложение
https://github.com/DiceOwl/StableDiffusionStuff

https://github.com/DiceOwl/StableDiffusionStuff/blob/main/loopback_superimpose.py

Смешивает вывод img2img с исходным входным изображением с силой альфа. Результат снова загружается в img2img (в цикле>=2), и эта процедура повторяется. Имеет тенденцию повышать резкость изображения, улучшать согласованность, снижать творческий потенциал и уменьшать мелкие детали.

## Интерполировать
https://github.com/DiceOwl/StableDiffusionStuff

https://github.com/DiceOwl/StableDiffusionStuff/blob/main/interpolate.py

Скрипт img2img для создания промежуточных изображений. Позволяет два входных изображения для интерполяции. Дополнительные функции показаны в [readme](https://github.com/DiceOwl/StableDiffusionStuff).

## Выполнить n раз
https://gist.github.com/camenduru/9ec5f8141db9902e375967e93250860f

Выполнить n раз со случайным начальным числом.

## Расширенный цикл обратной связи
https://github.com/Extraltodeus/advanced-loopback-for-sd-webui

Динамическое масштабирование с изменением параметров и быстрым переключением среди других функций!

## быстрое преобразование
https://github.com/feffy380/prompt-morph

Создавайте последовательности морфинга с помощью Stable Diffusion. Интерполируйте между двумя или более подсказками и создавайте изображение на каждом шаге.

Использует новое ключевое слово AND и может дополнительно экспортировать последовательность как видео.

## оперативная интерполяция
https://github.com/EugeoSynthesisThirtyTwo/prompt-interpolation-script-for-sd-webui

С помощью этого сценария вы можете выполнять интерполяцию между двумя подсказками (используя ключевое слово «И») и генерировать столько изображений, сколько хотите.
Вы также можете создать GIF с результатом. Работает как для txt2img, так и для img2img.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>

![gif](https://user-images.githubusercontent.com/24735555/195470874-afc3dfdc-7b35-4b23-9c34-5888a4100ac1.gif)

</details>

## Ассиметричная мозаика
https://github.com/tjm35/асимметричная плитка-sd-webui/

Управляйте горизонтальной/вертикальной бесшовной мозаикой независимо друг от друга.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/19196175/195132862-8c050327-92f3-44a4-9c02-0f11cce0b609.png" width="624" height="312" />
</details>

## Силовая симметрия
https://gist.github.com/1ort/2fe6214cf1abe4c07087aac8d91d0d8a

см. https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/2441

применяет симметрию к изображению каждые n шагов и отправляет результат далее в img2img.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/83316072/196016119-0a03664b-c3e4-49f0-81ac-a9e719b24bd1.png" width="624" height="312" />
</details>

## SD-скрытое зеркалирование
https://github.com/dfaker/SD-латентное-зеркалирование

Применяет зеркальное отражение и отражение к скрытым изображениям для создания чего угодно, от тонких сбалансированных композиций до идеальных отражений.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/35278260/199627881-6f62a227-3a6c-4470-9c18-2ed8bc57194c.png" width="624" height="312" />
</details>

## txt2палитра
https://github.com/1ort/txt2palette

Создавайте палитры по текстовому описанию. Этот скрипт берет сгенерированные изображения и преобразует их в цветовые палитры.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/83316072/199360686-62f0f5ec-ed3d-4c0f-95b4-af9c67d1e248.png" ширина="352" высота="312" />
</details>


## СтилиСтрелки
https://github.com/some9000/StylePile

Простой способ смешивания и сопоставления элементов с подсказками, которые влияют на стиль результата.
<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/17021558/199468444-99e78027-1889-4bec-b97b-25f801e33c0a.jpg" ширина="960" высота="120" />
</details>

## Сценарий графика XYZ
https://github.com/xrpgame/xyz_plot_script

Создает файл .html для интерактивного просмотра набора изображений. Используйте колесо прокрутки или клавиши со стрелками для перемещения по оси Z.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://raw.githubusercontent.com/xrpgame/xyz_plot_script/master/example1.png" ширина="522" высота="312" />
</details>

## xyz-сюжетная сетка
https://github.com/Gerschel/xyz-сюжет-сетка

Поместите xyz_grid.py в папку скриптов рядом с другими скриптами.
Работает как график x/y, как и следовало ожидать, но теперь имеет z. Работает так, как вы ожидаете, с легендами сетки.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://github.com/Gerschel/xyz-plot-grid/raw/main/000.png" width="574" height="390" />
</details>

## Расширенная сетка XY
https://github.com/0xALIVEBEEF/Расширенная-XY-сетка

Пользовательский скрипт для стабильной диффузии-webui AUTOMATIC1111, который добавляет больше возможностей в стандартную сетку xy:

- Multitool: позволяет использовать несколько параметров на одной оси, теоретически позволяет регулировать неограниченное количество параметров в одной координатной сетке.

- Настраиваемая матрица подсказок

- Группировать файлы в каталоге

- S/R Placeholder — замените значение-заполнитель (первое значение в списке параметров) на нужные значения.

- Добавить PNGinfo в изображение сетки

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>

<img src="https://user-images.githubusercontent.com/80003301/202277871-a4a3341b-13f7-42f4-a3e6-ca8f8cd8250a.png" ширина="574" высота="197" />

Примеры изображений: Подсказка: "Дарт Вейдер едет на велосипеде, модификатор"; X: Multitool: "Подсказка S/R: велосипед, мотоцикл | Масштаб CFG: 7.5, 10 | Подсказка S/R Placeholder: модификатор, 4k, artstation"; Y: Multitool: «Сэмплер: Эйлер, Эйлер a | Шаги: 20, 50»

</details>



## Автодополнение тега Booru
https://github.com/DominikDoom/a1111-sd-webui-tagcomplete

Отображает подсказки автозаполнения для тегов с досок «image booru», таких как Danbooru. Использует файлы CSV с локальными тегами и включает конфигурацию для настройки.

Также поддерживает завершение для [подстановочных знаков](https://github.com/adieyal/sd-dynamic-prompts#wildcard-files)

## Встраивание в PNG
https://github.com/dfaker/embedding-to-png-скрипт

Преобразует существующие вложения в общедоступные версии изображений.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/35278260/196052398-268a3a3e-0fad-46cd-b37d-9808480ceb18.png" width="263" height="256" />
</details>

## Альфа-канвас
https://github.com/TKoestlerx/sdexperiments

Закрасьте регион. Концепция бесконечного перекрашивания использовала в качестве основы два существующих скрипта перекрашивания из репозитория AUTOMATIC1111.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/86352149/199517938-3430170b-adca-487c-992b-eb89b3b63681.jpg" ширина="446" высота="312" />
</details>

## Случайная сетка
https://github.com/lilly1987/AI-WEBUI-scripts-Random

Произвольно введите значения сетки xy.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/20321215/197346726-f93b7e84-f808-4167-9969-dc42763eeff1.png" width="198" height="312" />

Основная логика аналогична графику x/y, только внутри тип x фиксируется как шаг, а тип y фиксируется как cfg.
Генерирует значения x, равные количеству шагов (10) в диапазоне значений step1|2 (10-30)
Генерирует столько значений x, сколько отсчетов cfg (10) в диапазоне значений cfg1|2 (6-15)
Даже если вы перевернете ограничение диапазона 1|2 вверх дном, оно автоматически изменится.
В случае значения cfg оно рассматривается как тип int, и десятичное значение не читается.
</details>

## Случайный
https://github.com/lilly1987/AI-WEBUI-scripts-Random

Повторить простое количество раз без сетки.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/20321215/197346617-0ed1cd09-0ddd-48ad-8161-bc1540d628ad.png" ширина="258" высота="312" />
</details>

## Эстетическая оценка стабильной диффузии
https://github.com/grexzen/SD-Чад

Оценивает ваши изображения.

## img2tiles
https://github.com/arcanite24/img2tiles

генерировать тайлы из базового изображения. Основан на высококлассном сценарии SD.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://github.com/arcanite24/img2tiles/raw/master/examples/example5.png" width="312" height="312" />
</details>

## img2mosiac
https://github.com/1ort/img2mosaic

Создавайте мозаики из изображений. Скрипт разрезает изображение на тайлы и обрабатывает каждый тайл отдельно. Размер каждой плитки выбирается случайным образом.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://user-images.githubusercontent.com/83316072/200170569-0e7131e4-1da8-4caf-9cd9-5b785c9d21b0.png" width="758" height="312" />
</details>

## Карты глубины
https://github.com/thygate/stable-diffusion-webui-depthmap-script

Этот скрипт является надстройкой для [веб-интерфейса AUTOMATIC1111 Stable Diffusion](https://github.com/AUTOMATIC1111/stable-diffusion-webui), который создает «карты глубины» из сгенерированных изображений. Результат можно просматривать на 3D- или голографических устройствах, таких как VR-гарнитуры или дисплей [lookglass](https://lookglassfactory.com/), использовать в Render- или Game-Engine на плоскости с модификатором смещения и, возможно, даже на 3D-печати. .

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>
<img src="https://github.com/thygate/stable-diffusion-webui-depthmap-script/raw/main/examples.png" width="780" height="312" />
</details>

## Проверить мою подсказку
https://github.com/Extraltodeus/test_my_prompt

Вы когда-нибудь использовали очень длинную подсказку, полную слов, которые, как вы не уверены, действительно влияют на ваш имидж? Вы потеряли смелость попытаться удалить их один за другим, чтобы проверить, достойны ли их эффекты вашего мощного графического процессора?

ХОРОШО, теперь вам не нужна смелость, так как этот сценарий был СДЕЛАН ДЛЯ ВАС!

Он генерирует столько изображений, сколько слов в вашей подсказке (конечно, вы можете выбрать разделитель).

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>

Здесь подсказка просто: «**банан, в огне, снег**», и, как вы можете видеть, он сгенерировал каждое изображение без каждого описания в нем.

<img src="https://user-images.githubusercontent.com/15731540/200349119-e45d3cfb-39f0-4999-a8f0-4671a6393824.png" width="512" height="512" />

Вы также можете проверить свою отрицательную подсказку.

</details>

## Пиксель арт
https://github.com/C10udburst/stable-diffusion-webui-скрипты

Простой скрипт, который изменяет размер изображения на переменную величину, а также преобразует изображение для использования цветовой палитры заданного размера.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>

| Отключено | Включено x8, без изменения размера назад, без цветовой палитры | Включено x8, без цветовой палитры | Включена цветовая палитра x8, 16 |
| :---: | :---: | :---: | :---: |

|![предварительная версия](https://user-images.githubusercontent.com/18114966/201491785-e30cfa9d-c850-4853-98b8-11db8de78c8d.png) | ![предварительный просмотр](https://user-images.githubusercontent.com/18114966/201492204-f4303694-e98d-4ea3-8256-538a88ea26b6.png) | ![предварительная версия](https://user-images.githubusercontent.com/18114966/201491864-d0c0c9f1-e34f-4cb6-a68e-7043ec5ce74e.png) | ![предварительная версия](https://user-images.githubusercontent.com/18114966/201492175-c55fa260-a17d-47c9-a919-9116e1caa8fe.png) |

[используемая модель](https://publicprompts.art/all-in-one-pixel-art-dreambooth-model/)
```text
japanese pagoda with blossoming cherry trees, full body game asset, in pixelsprite style
Steps: 20, Sampler: DDIM, CFG scale: 7, Seed: 4288895889, Size: 512x512, Model hash: 916ea38c, Batch size: 4
```

</details>

## Несколько гиперсетей
https://github.com/antis0007/sd-webui-multiple-hypernetworks

Добавляет возможность применять сразу несколько гиперсетей. Переопределяет функции перехвата, оптимизации и переадресации CrossAttention для последовательного применения нескольких гиперсетей с разными весами.

## Структура гиперсети (.hns)/Переменные Dropout/Monkey Patches
https://github.com/aria1th/Hypernetwork-MonkeyPatch-Extension

Добавляет возможность применять структуру гиперсети, определяя ее в файле .hns. см. [здесь](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/4334) для получения подробной информации.

Добавляет возможность использовать правильную переменную скорость отсева, например 0,05. Также устраняет проблемы с использованием гиперсети сразу после тренировки.

Добавляет создание бета-гиперсети (выпадение) и бета-обучение, которое позволяет автоматически косинусный отжиг и использование исходных изображений без обрезки.

## Конфиг-пресеты
https://github.com/Zyin055/Config-Presets-Script-OLD-

Быстро меняйте настройки на вкладках txt2img и img2img, используя настраиваемый раскрывающийся список предустановленных значений.

<details><summary>Пример: (Нажмите, чтобы развернуть:)</summary>

<img src="https://camo.githubusercontent.com/fd878bf6e95b5b4d4bc95e1aef7d3253a5cd3832c65e97de942455572ee3e561/68747470733a2f2f692e696d6775722e636f6d2f4231654d5741772e6a7067" width="512" height="146" />

</details>


## Сохранение шагов процесса выборки

Этот сценарий сохранит этапы процесса выборки в каталог.
```python
import os.path

import modules.scripts as scripts
import gradio as gr

from modules import sd_samplers, shared
from modules.processing import Processed, process_images


class Script(scripts.Script):
    def title(self):
        return "Save steps of the sampling process to files"

    def ui(self, is_img2img):
        path = gr.Textbox(label="Save images to path")
        return [path]

    def run(self, p, path):
        index = [0]

        def store_latent(x):
            image = shared.state.current_image = sd_samplers.sample_to_image(x)
            image.save(os.path.join(path, f"sample-{index[0]:05}.png"))
            index[0] += 1
            fun(x)

        fun = sd_samplers.store_latent
        sd_samplers.store_latent = store_latent

        try:
            proc = process_images(p)
        finally:
            sd_samplers.store_latent = fun

        return Processed(p, proc.images, p.seed, "")
```
