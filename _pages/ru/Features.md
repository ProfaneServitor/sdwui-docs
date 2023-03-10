---
title: Функции
layout: post
category: Guides
permalink: /features/
machine_translated: true
lang: ru
---
Это страница демонстрации возможностей [веб-интерфейса стабильной диффузии](https://github.com/AUTOMATIC1111/stable-diffusion-webui).

Все примеры не отобраны, если не указано иное.

# Стабильная диффузия 2.0
## Базовые модели
Поддерживаются модели: 768-v-ema.ckpt ([модель](https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/768-v-ema.ckpt), [config](https ://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference-v.yaml)) и 512-base-ema.ckpt ([модель](https://huggingface .co/stabilityai/stable-diffusion-2-base/blob/main/512-base-ema.ckpt), [config](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/ стабильная диффузия/v2-inference.yaml)). 2.1 чекпоинты тоже должны работать.

- скачать чекпоинт (отсюда: https://huggingface.co/stabilityai/stable-diffusion-2)
- положить в папку models/Stable-Diffusion
- возьмите конфиг из репозитория SD2.0 и поместите его в то же место, что и контрольная точка, переименовав его, чтобы он имел то же имя файла (т.е. если ваша контрольная точка называется `768-v-ema.ckpt`, конфигурация должна называться `768- в-эма.ямл`)
- выберите новую контрольную точку из пользовательского интерфейса

Вкладка «Поезд», скорее всего, будет сломана для моделей 2.0.

Если 2.0 или 2.1 генерируют черные изображения, включите полную точность с помощью `--no-half` или попробуйте использовать оптимизацию `--xformers`.

_**Примечание:**_ SD 2.0 и 2.1 более чувствительны к численной нестабильности FP16 (как отмечено ими самими [здесь](https://github.com/Stability-AI/stablediffusion/commit/c12d960d1ee4f9134c2516862ef991ec52d3f59e)) из-за их новый модуль перекрестного внимания.

На fp16: [комментарий](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/5503#issuecomment-1341495770) для включения в webui-user.bat:

@эхо выключено

установить ПИТОН=
установить GIT =
установить VENV_DIR=
установите COMMANDLINE_ARGS = ваши параметры командной строки
установить STABLE_DIFFUSION_COMMIT_HASH="c12d960d1ee4f9134c2516862ef991ec52d3f59e"
установить ATTN_PRECISION=fp16

позвони в webui.bat

## Модель с наведением по глубине
[Подробнее](https://github.com/Stability-AI/stablediffusion#depth-conditional-stable-diffusion). [PR](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/5542).
Инструкции:
- скачать контрольную точку [512-depth-ema.ckpt](https://huggingface.co/stabilityai/stable-diffusion-2-depth)
- поместите его в models/Stable-diffusion
- возьмите [config](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-midas-inference.yaml) и поместите его в ту же папку, что и контрольная точка
- переименовать конфиг в `512-depth-ema.yaml`
- выберите новую контрольную точку из пользовательского интерфейса

Модель с глубиной будет работать только на вкладке img2img.

# Перекрашивание

Outpainting расширяет исходное изображение и закрашивает созданное пустое пространство.

Пример:

| Оригинал | Окрашивание | Снова перекраска |
|------------------------------|------------------ ---------------------------|------------------------------|
| ![](images/outpainting-1.png) | ![](images/outpainting-2.png) | ![](images/outpainting-3.png) |

Исходное изображение анонимного пользователя с 4chan. Спасибо, анонимный пользователь.

Вы можете найти эту функцию на вкладке img2img внизу, в разделе «Сценарий» -> «Перекрашивание бедняка».

Outpainting, в отличие от обычной генерации изображения, кажется, очень выигрывает от большого количества шагов. Рецепт хорошей перекраски
- хорошая подсказка, соответствующая картинке, ползунки для шумоподавления и шкала CFG установлены на максимум, а количество шагов от 50 до 100 с
Родовые сэмплеры Euler или DPM2.

| 81 шаг, Эйлер А | 30 шагов, Эйлер А | 10 шагов, Эйлер А | 80 шагов, Эйлер А |
|--------------------------------------|------------ ----------------------------|--------------------- ------------------|-------------------------------- -----|
| ![](images/inpainting-81-euler-a.png) | ![](images/inpainting-30-euler-a.png) | ![](images/inpainting-10-euler-a.png) | ![](images/inpainting-80-dpm2-a.png) |

# Закрашивание
На вкладке img2img нарисуйте маску над частью изображения, и эта часть будет закрашена.

![](изображения/inpainting.png)

Варианты покраски:
- нарисовать маску самостоятельно в веб-редакторе
- стереть часть картинки во внешнем редакторе и загрузить прозрачную картинку. Любые даже слегка прозрачные участки станут частью маски. Имейте в виду, что [некоторые редакторы](https://docs.krita.org/en/reference_manual/layers_and_masks/split_alpha.html#how-to-save-a-png-texture-and-keep-color-values-in- полностью прозрачные области) по умолчанию сохраняют полностью прозрачные области черными.
- изменить режим (в правом нижнем углу картинки) на "Загрузить маску" и выбрать для маски отдельное черно-белое изображение (white=inpaint).

## Покраска модели
RunwayML обучил дополнительную модель, специально предназначенную для раскрашивания. Эта модель принимает дополнительные входные данные — исходное изображение без шума плюс маска — и, кажется, работает намного лучше.

Скачать и дополнительную информацию для модели можно здесь: https://github.com/runwayml/stable-diffusion#inpainting-with-stable-diffusion.

Чтобы использовать модель, вы должны переименовать контрольную точку так, чтобы ее имя файла заканчивалось на `inpainting.ckpt`, например, `1.5-inpainting.ckpt`.

После этого просто выберите контрольную точку, как вы обычно выбираете любую контрольную точку, и все готово.

## Маскированный контент
Поле маскированного содержимого определяет, что содержимое помещается в маскированные области до того, как они будут закрашены.

| маска | заполнить | оригинальный | скрытый шум | скрытое ничего |
|------------------------------------------------- |------------------------------------------------- |------------------------------------------------- ----|------------------------------- ---------------------------|------------------------------------- ----------------------|
| ![](images/inpainting-initial-content-mask.png) | ![](images/inpainting-initial-content-fill.png) | ![](images/inpainting-initial-content-original.png) | ![](images/inpainting-initial-content-latent-noise.png) | ![](images/inpainting-initial-content-latent-nothing.png) |

## Inpaint в полном разрешении
Обычно inpainting изменяет размер изображения до целевого разрешения, указанного в пользовательском интерфейсе. С Inpaint в полном разрешении
включена, изменяется размер только маскируемой области, и после обработки она вставляется обратно в исходное изображение.
Это позволяет работать с большими изображениями и позволяет визуализировать закрашенный объект с гораздо большим разрешением.


| Вход | Раскрасить нормальный | Inpaint в полном разрешении |
|--------------------------------------|------------ -----------------------|---------------------------------------- ---------|
| ![](images/inpaint-whole-mask.png) | ![](images/inpaint-whole-no.png) | ![](images/inpaint-whole-yes.png) |


## Маскирующий режим
Существует два варианта маскированного режима:
- Inpaint masked - закрашивается область под маской
- Inpaint not masked - под маской без изменений, все остальное закрашивается

## Альфа-маска

| Вход | Выход |
|------------------------------|------------------ -------------|
| ![](images/inpaint-mask.png) | ![](изображения/inpaint-mask2.png) |


# Матрица подсказок
Разделите несколько подсказок с помощью символа `|`, и система создаст изображение для каждой их комбинации.
Например, если вы используете подсказку «оживленная городская улица в современном городе|иллюстрация|кинематографическое освещение», возможны четыре комбинации (первая часть подсказки всегда сохраняется):

- `оживленная городская улица в современном городе`
- `оживленная городская улица в современном городе, иллюстрация`
- `оживленная городская улица в современном городе, кинематографическое освещение`
- `оживленная городская улица в современном городе, иллюстрация, кинематографическое освещение`

В этом порядке будут созданы четыре изображения, все с одним и тем же начальным числом и каждое с соответствующей подсказкой:
![](images/prompt-matrix.png)

Другой пример, на этот раз с 5 подсказками и 16 вариантами:
![](изображения/prompt_matrix.jpg)

Вы можете найти эту функцию внизу, в разделе «Сценарий» -> «Матрица подсказок».

# Цветной эскиз

Базовый инструмент для раскрашивания img2img. Чтобы использовать эту функцию в img2img, включите ее с помощью `--gradio-img2img-tool color-sketch` в аргументах командной строки. Чтобы использовать эту функцию в режиме рисования, включите ее с помощью `--gradio-inpaint-tool color-sketch`. Браузеры на основе Chromium поддерживают инструмент-дроппер. (см. рисунок)

![дроппер](https://user-images.githubusercontent.com/98228077/196140222-54bc71ad-2746-4c38-8075-5c53fbcde2a9.png)


# Стабильный диффузионный апскейл
Масштабируйте изображение с помощью RealESRGAN/ESRGAN, а затем просматривайте фрагменты результата, улучшая их с помощью img2img.
У него также есть возможность позволить вам самостоятельно выполнять масштабирование во внешней программе и просто просматривать плитки с помощью img2img.

Оригинальная идея: https://github.com/jquesnelle/txt2imghd. Это независимая реализация.

Чтобы использовать эту функцию, выберите «Увеличение SD в раскрывающемся списке сценариев» (вкладка img2img).

![chrome_dl8hcMPYcx](https://user-images.githubusercontent.com/39339941/193300082-be3b8864-3c28-44b7-bb75-f893f92269b6.png)

Входное изображение будет увеличено в два раза по сравнению с оригиналом.
ширина и высота, а ползунки ширины и высоты пользовательского интерфейса определяют размер отдельных плиток. Из-за перекрытия,
размер тайла может быть очень важен: для изображения 512x512 требуется девять тайлов 512x512 (из-за перекрытия), но только
четыре тайла 640x640.

Рекомендуемые параметры для апскейлинга:
- Метод выборки: Эйлер a
- Сила шумоподавления: 0,2, может быть увеличена до 0,4, если вы любите приключения.

| Оригинал | РеалЕСРГАН | топаз гигапиксель | SD высококлассный |
|----------------------------------------------------------|----- -------------------------------------------------------|--------- ----------------------------------|- -----------------------------------------------------------|
| ![](images/sd-upscale-robot-original.png) | ![](images/sd-upscale-robot-realrgan.png) | ![](images/sd-upscale-robot-esrgan-topaz-gigapixel.png) | ![](images/sd-upscale-robot-sd-upscale.png) |
| ![](images/sd-upscale-castle-original.png) | ![](images/sd-upscale-castle-realesrgan.png) | ![](images/sd-upscale-castle-esrgan-topaz-gigapixel.png) | ![](images/sd-upscale-castle-sd-upscale.png) |
| ![](images/sd-upscale-city-original.png) | ![](images/sd-upscale-city-realesrgan.png) | ![](images/sd-upscale-city-esrgan-topaz-gigapixel.png) | ![](images/sd-upscale-city-sd-upscale.png) |

# Внимание/акцент
Использование `()` в подсказке увеличивает внимание модели к заключенным в него словам, а `[]` уменьшает его. Вы можете комбинировать несколько модификаторов:

![](изображения/внимание-3.jpg)

Шпаргалка:

- `a (слово)` - увеличить внимание к `слову` в 1,1 раза
- `a ((слово))` - увеличить внимание к слову в 1,21 раза (= 1,1 * 1,1)
- `a [слово]` - уменьшить внимание к `слову` в 1,1 раза
- `a (word:1.5)` - увеличить внимание к `слову` в 1,5 раза
- `a (word:0.25)` - уменьшить внимание к `слову` в 4 раза (= 1 / 0,25)
- `a \(word\)` - использовать литеральные символы `()` в подсказке

С помощью `()` вес может быть указан следующим образом: `(text:1.4)`. Если вес не указан, предполагается, что он равен 1,1. Указание веса работает только с `()`, но не с `[]`.

Если вы хотите использовать какие-либо буквальные символы `()[]` в подсказке, используйте обратную косую черту, чтобы избежать их: `anime_\(character\)`.

29 сентября 2022 г. была добавлена ​​новая реализация, поддерживающая escape-символы и числовые веса. Недостатком новой реализации является то, что старая не была идеальной и иногда съедала символы: «a (((farm))), daytime», например, без запятой превращалось в «farm daytime». Это поведение не поддерживается новой реализацией, которая корректно сохраняет весь текст, и это означает, что ваши сохраненные начальные значения могут создавать разные изображения. На данный момент в настройках есть возможность использовать старую реализацию.

NAI использует мою реализацию до 2022-09-29, за исключением того, что они имеют 1,05 в качестве множителя и используют `{}` вместо `()`. Таким образом, преобразование применяется:

- их `{word}` = наше `(word:1.05)`
- их `{{word}}` = наше `(word:1.1025)`
- их `[слово]` = наше `(слово:0,952)` (0,952 = 1/1,05)
- их `[[слово]]` = наше `(слово:0,907)` (0,907 = 1/1,05/1,05)


# петля
Выбор сценария обратной связи в img2img позволяет автоматически передавать выходное изображение в качестве входных данных для следующего пакета. Эквивалентно
сохранение выходного изображения и замена им входного изображения. Параметр количества пакетов определяет, сколько итераций
это вы получаете.

Обычно при этом вы сами выбираете одно из многих изображений для следующей итерации, поэтому полезность
этой функции может быть сомнительным, но мне удалось получить с ее помощью несколько очень хороших результатов, которые я не смог
получить иначе.

Пример: (выбранный результат)

![](изображения/loopback.jpg)

Исходное изображение анонимного пользователя с 4chan. Спасибо, анонимный пользователь.

# График X/Y
Создает сетку изображений с различными параметрами. Выберите, какие параметры должны быть общими для строк и столбцов, используя
Поля типа X и типа Y и введите эти параметры, разделенные запятой, в поля значений X/Y. Для целого числа
поддерживаются числа с плавающей запятой и диапазоны. Примеры:

- Простые диапазоны:
- `1-5` = 1, 2, 3, 4, 5
- Диапазоны с приращением в скобках:
- `1-5 (+2)` = 1, 3, 5
- `10-5 (-3)` = 10, 7
- `1-3 (+0,5)` = 1, 1,5, 2, 2,5, 3
- Диапазоны с количеством в квадратных скобках:
- `1-10 [5]` = 1, 3, 5, 7, 10
- `0,0-1,0 [6]` = 0,0, 0,2, 0,4, 0,6, 0,8, 1,0

![](images/xy_grid-medusa.png)

Вот настройки, которые создают график выше:

![](images/xy_grid-medusa-ui.png)

### Подсказка S/R
Подсказка S/R — один из наиболее сложных для понимания режимов работы графика X/Y. S/R означает поиск/замену, и вот что он делает — вы вводите список слов или фраз, он берет первое из списка и обрабатывает его как ключевое слово и заменяет все экземпляры этого ключевого слова другими элементами из списка. .

Например, с подсказкой «человек держит яблоко, 8к чистый» и подсказкой S/R «яблоко, арбуз, пистолет» вы получите три подсказки:

- `человек с яблоком, 8к чистый`
- `человек, держащий арбуз, чистый 8k`
- `человек с пистолетом, чистый 8к`

Список использует тот же синтаксис, что и строка в файле CSV, поэтому, если вы хотите включить запятые в свои записи, вы должны поместить текст в кавычки и убедиться, что между кавычками и разделяющими запятыми нет пробела:

- `тьма, свет, зелень, тепло` - 4 предмета - `тьма`, `свет`, `зелень`, `тепло`
- `тьма, "свет, зелень", тепло` - НЕПРАВИЛЬНО - 4 пункта - `тьма`, ``свет`, `зелень`, `тепло`
- "тьма", "свет, зелень", тепло` - ПРАВИЛЬНО - 3 пункта - `темнота`, `свет, зелень`, `тепло`

# Текстовая инверсия
Краткое пояснение: поместите свои вложения в каталог «embeddings» и используйте имя файла в подсказке.

Длинное объяснение: [текстовая инверсия](текстовая инверсия)

![сетка-0037](https://user-images.githubusercontent.com/20920490/193285770-9454c5e1-e594-463c-8be8-1488ddf2877b.png)

# Изменение размера
Есть три варианта изменения размера входных изображений в режиме img2img:

- Just resize - просто изменяет размер исходного изображения до целевого разрешения, что приводит к неправильному соотношению сторон.
- Обрезка и изменение размера - изменение размера исходного изображения с сохранением соотношения сторон, чтобы оно занимало все целевое разрешение, и обрезка выступающих частей.
- Изменение размера и заполнение - изменение размера исходного изображения с сохранением соотношения сторон, чтобы оно полностью соответствовало целевому разрешению, и заполнение пустого пространства строками/столбцами из исходного изображения.

Пример:
![](изображения/изменение размера.jpg)

# Выбор метода выборки
Выберите один из нескольких методов выборки для txt2img:

![](изображения/выборка.jpg)

# Изменение размера семени
Эта функция позволяет создавать изображения из известных семян с разным разрешением. Обычно при изменении разрешения
изображение полностью изменится, даже если вы сохраните все остальные параметры, включая начальное значение. При изменении размера семени вы указываете разрешение
исходного изображения, и модель, скорее всего, создаст что-то очень похожее на него, даже в другом разрешении.
В приведенном ниже примере крайняя левая картинка имеет размер 512x512, а остальные создаются с точно такими же параметрами, но с большей вертикалью.
разрешающая способность.

| Информация | Изображение |
|----------------------------------- ----------|
| Изменение размера семени не включено | ![](images/seed-noresize.png) |
| Семя изменено с 512x512 | ![](images/seed-resize.png) |

Родовые семплеры в этом немного хуже остальных.

Вы можете найти эту функцию, установив флажок «Дополнительно» рядом с семенем.

# Вариации
Ползунок «Сила вариации» и поле «Исходное значение вариации» позволяют указать, насколько нужно изменить существующее изображение, чтобы оно выглядело
вроде другой. На максимальной силе вы получите картинки с Вариационным сидом, на минимальной - картинки с исходным Сидом (кроме
при использовании наследственных семплеров).

![](images/seed-variations.jpg)

Вы можете найти эту функцию, установив флажок «Дополнительно» рядом с семенем.

# Стили
Нажмите кнопку «Сохранить подсказку как стиль», чтобы записать текущую подсказку в файл styles.csv с набором стилей. Dropbox для
справа от приглашения вы сможете выбрать любой стиль из ранее сохраненных и автоматически добавить его к вашему вводу.
Чтобы удалить стиль, вручную удалите его из styles.csv и перезапустите программу.

если вы используете специальную строку `{prompt}` в своем стиле, она заменит все, что в данный момент находится в приглашении, на эту позицию, а не добавит стиль к вашему приглашению.

# Отрицательное приглашение

Позволяет вам использовать другую подсказку о том, чего модель должна избегать при создании изображения. Это работает с помощью
отрицательное приглашение для безусловного кондиционирования в процессе выборки вместо пустой строки.

Расширенное объяснение: [Отрицательная подсказка](Отрицательная подсказка)

| Оригинал | Негатив: фиолетовый | Отрицательное: щупальца |
|--------------------------------|----------------- ----------------|------------------------------------------------ ---|
| ![](images/negative-base.png) | ![](images/negative-purple.png) | ![](images/negative-tentacles.png) |

# Опросчик CLIP

Автор: https://github.com/pharmapsychotic/clip-interrogator

Опросчик CLIP позволяет извлекать подсказку из изображения. Подсказка не позволит вам воспроизвести это
точное изображение (иногда оно даже не будет близко), но это может быть хорошим началом.

![](images/CLIP-допрос.png)

При первом запуске опросчика CLIP будет загружено несколько гигабайт моделей.

Опросчик CLIP состоит из двух частей: одна представляет собой модель BLIP, которая создает текстовое описание из изображения.
Другая — это модель CLIP, которая выбирает из списка несколько строк, относящихся к изображению. По умолчанию там
всего один список - список художников (из `artists.csv`). Вы можете добавить больше списков, выполнив следующие действия:

- создайте каталог `опросить` в том же месте, что и webui
- поместите в него текстовые файлы с соответствующим описанием в каждой строке

Например, какие текстовые файлы использовать, см. https://github.com/pharmapsychotic/clip-interrogator/tree/main/data.
На самом деле, вы можете просто взять оттуда файлы и использовать их — просто пропустите artist.txt, потому что у вас уже есть список
художников в `artists.csv` (или используйте его тоже, кто вас остановит). Каждый файл добавляет одну строку текста к окончательному описанию.
Если вы добавите ".top3." к имени файла, например, `flavors.top3.txt`, три наиболее релевантные строки из этого файла будут
добавлено в подсказку (другие номера тоже работают).

Существуют настройки, относящиеся к этой функции:
- `Опросить: хранить модели в VRAM` - не выгружать модели Опроса из памяти после их использования. Для пользователей с большим количеством видеопамяти.
- `Опрашивать: использовать художников из artists.csv` - добавляет исполнителя из `artists.csv` при опросе. Может быть полезно отключить, когда у вас есть список исполнителей в каталоге «допросить».
- `Опросить: количество лучей для BLIP` - параметр, влияющий на то, насколько подробны описания из модели BLIP (первая часть сгенерированного приглашения)
- `Опросить: минимальная длина описания` - минимальная длина текста модели BLIP
- `Опросить: максимальная длина описания` - максимальная длина текста модели BLIP
- `Опросить: максимальное количество строк в текстовом файле` - опросчик будет рассматривать только это количество первых строк в файле. Если установлено значение 0, значение по умолчанию равно 1500, то есть примерно столько, сколько может выдержать видеокарта на 4 ГБ.

# Быстрое редактирование

![xy_grid-0022-646033397](https://user-images.githubusercontent.com/20920490/190426933-9748708b-6db0-4cb0-8cb9-3285053916b8.jpg)

Быстрое редактирование позволяет вам начать выборку одного изображения, но в середине переключиться на что-то другое. Базовый синтаксис для этого:

```
[from:to:when]
```

Где «от» и «до» — это произвольные тексты, а «когда» — это число, определяющее, на каком конце цикла выборки должно быть выполнено переключение. Чем позже, тем меньше мощности у модели для рисования текста «в» вместо текста «из». Если `когда` является числом от 0 до 1, это часть количества шагов, после которых нужно сделать переключение. Если это целое число больше нуля, это всего лишь шаг, после которого нужно сделать переключение.

Вложение одной подсказки в другую действительно работает.

Кроме того:
- `[to:when]` - добавляет `to` в подсказку после фиксированного количества шагов (`when`)
- `[from::when]` - удаляет `from` из подсказки после фиксированного количества шагов (`when`)

Пример:
`пейзаж [фэнтези:киберпанк:16]`

- В начале модель будет рисовать "фантазийный пейзаж".
- После шага 16 он переключится на рисование «киберпанк-пейзажа», продолжая с того места, где остановился, с фантазией.

Вот более сложный пример с несколькими правками:
`фантастический пейзаж с [горой:озером:0,25] и [дубом:елкой:0,75][на переднем плане::0,6][на заднем плане:0,25] [дрянной:мастерский:0,5]` ​​(сэмплер имеет 100 шагов)

- в начале `фантастический пейзаж с горой и дубом на переднем плане дрянной`
- после шага 25, `фантастический пейзаж с озером и дубом на переднем плане, на заднем плане дрянной`
- после шага 50 `фантастический пейзаж с озером и дубом на переднем плане на заднем плане мастерски`
- после шага 60, `фантастический пейзаж с озером и дубом на заднем плане мастерски`
- после шага 75, `фантастический пейзаж с озером и рождественской елкой на заднем плане мастерски`

Картинка вверху была сделана с подсказкой:

`Официальный портрет улыбающегося генерала Второй мировой войны, [мужчина:женщина:0,99], веселое, счастливое, детально проработанное лицо, 20 век, высокая детализация, кинематографическое освещение, цифровая художественная картина Грега Рутковски

И число 0,99 заменяется тем, что вы видите в метках столбцов на изображении.

Последний столбец на картинке — [мужчина:женщина:0.0], что, по сути, означает, что вы просите модель нарисовать женщину с самого начала, не начиная с генерала-мужчины, и поэтому она выглядит так не похоже на другие.

## Чередующиеся слова

Удобный синтаксис для замены каждого шага.

[корова|лошадь] в поле

На шаге 1 подсказка «корова в поле». Шаг 2 — «лошадь в поле». Шаг 3 — «корова в поле» и так далее.

![Чередование слов](https://user-images.githubusercontent.com/39339941/197556926-49ceb72b-daf3-4208-86f3-c2e7e9cd775a.gif)




См. более сложный пример ниже. На шаге 8 цепочка возвращается от «мужчина» к «корове».

[корова|корова|лошадь|человек|амурский тигр|бык|человек] в поле

Редактирование подсказок было впервые реализовано Doggettx в [этот пост на myspace.com](https://www.reddit.com/r/StableDiffusion/comments/xas2os/simple_prompt2prompt_implementation_with_prompt/).

# Высокое разрешение. исправить
Удобный вариант для частичного рендеринга изображения с более низким разрешением, увеличения его масштаба, а затем добавления деталей с высоким разрешением. По умолчанию txt2img делает ужасные картинки в очень высоком разрешении, что позволяет избежать использования композиции маленькой картинки. Включается установкой флажка «Highres. fix» на странице txt2img.

| Без | С |
|--------------------------------|----------------- ----------------|
| ![00262-836728130](https://user-images.githubusercontent.com/20920490/191177752-ad983e62-8e1c-4197-8f3b-3165a6a6c31d.png) | ![00261-836728130](https://user-images.githubusercontent.com/20920490/191177785-395a951e-0d2e-4db7-9645-4c5af9321772.png) |
| ![00345-950170121](https://user-images.githubusercontent.com/20920490/191178018-25dcd98d-6c45-4c31-ab7a-3de6c51c52e3.png) | ![00341-950170121](https://user-images.githubusercontent.com/20920490/191178048-3eba3db4-e5be-4617-9bfe-2cb36cebaafc.png) |

# Составная диффузия

Метод, позволяющий комбинировать несколько подсказок.
объединяйте подсказки, используя заглавную букву И

кошка И собака

Поддерживает веса для подсказок: «кошка: 1,2 И собака И пингвин: 2,2»
Значение веса по умолчанию равно 1.
Это может быть очень полезно для объединения нескольких вложений в ваш результат: `creature_embedding in the forest:0.7 AND arcane_embedding:0.5 AND glitch_embedding:0.2`

Использование значения ниже 0,1 практически не даст эффекта. `a cat AND a dog:0.03` даст в основном тот же результат, что и `cat`

Это может быть удобно для создания точно настроенных рекурсивных вариантов, продолжая добавлять дополнительные подсказки к вашей сумме. `creature_embedding на бревне И лягушка: 0,13 И желтые глаза: 0,08`


# Прерывать

Нажмите кнопку «Прерывание», чтобы остановить текущую обработку.

# Поддержка видеокарты 4GB
Оптимизация для графических процессоров с низким объемом видеопамяти. Это должно позволить генерировать изображения 512x512 на видеокартах с 4 Гб памяти.

`--lowvram` — это повторная реализация идеи оптимизации [basujindal](https://github.com/basujindal/stable-diffusion).
Модель разделена на модули, и в памяти GPU хранится только один модуль; когда необходимо запустить другой модуль, предыдущий
удаляется из памяти GPU. Природа этой оптимизации замедляет обработку — примерно в 10 раз медленнее.
по сравнению с нормальной работой на моей RTX 3090.

`--medvram` — это еще одна оптимизация, которая должна значительно сократить использование видеопамяти, не обрабатывая условные и
безусловное шумоподавление в том же пакете.

Эта реализация оптимизации не требует каких-либо модификаций исходного кода Stable Diffusion.

# Реставрация лица
Позволяет улучшать лица на изображениях с помощью GFPGAN или CodeFormer. На каждой вкладке есть флажок, чтобы использовать восстановление лица,
а также отдельная вкладка, которая просто позволяет вам использовать восстановление лица на любом изображении, с ползунком, который контролирует, насколько видимым
эффект есть. Вы можете выбрать один из двух методов в настройках.

| Оригинал | ГФГАН | КодФормер |
|-------------------------|----------------------- -----------------------|-----------------------------------|
| ![](images/facefix.png) | ![](images/facefix-gfpgan.png) | ![](images/facefix-codeformer.png) |


# Сохранение
Нажмите кнопку «Сохранить» в разделе вывода, и сгенерированные изображения будут сохранены в каталоге, указанном в настройках;
параметры генерации будут добавлены в файл csv в том же каталоге.

# Загрузка
Графика загрузки Gradio очень негативно влияет на скорость обработки нейросети.
Моя RTX 3090 делает изображения примерно на 10% быстрее, когда вкладка с градиентом не активна. По умолчанию интерфейс
теперь скрывает анимацию процесса загрузки и заменяет ее статическим текстом «Загрузка...», что позволяет
тот же эффект. Используйте параметр командной строки `--no-progressbar-hiding`, чтобы отменить это и показать анимацию загрузки.

# Оперативная проверка
Stable Diffusion имеет ограничение на длину вводимого текста. Если ваше приглашение слишком длинное, вы получите
предупреждение в поле вывода текста, показывающее, какие части вашего текста были усечены и проигнорированы моделью.

# Информация о PNG
Добавляет информацию о параметрах генерации в PNG в виде текстового фрагмента. Ты
можно просмотреть эту информацию позже с помощью любого программного обеспечения, которое поддерживает просмотр
Информация о фрагменте PNG, например: https://www.nayuki.io/page/png-file-chunk-inspector

# Настройки
Вкладка с настройками, позволяет использовать UI для редактирования более половины параметров, которые ранее
были командной строкой. Настройки сохраняются в файл config.js. Настройки, которые остаются в командной строке
параметры - это те, которые требуются при запуске.

# Формат имен файлов
Поле «Шаблон имени файла изображения» на вкладке «Настройки» позволяет настроить имена файлов сгенерированных изображений txt2img и img2img. Этот шаблон определяет параметры генерации, которые вы хотите включить в имена файлов, и их порядок. Поддерживаемые теги:

`[шаги], [cfg], [приглашение], [prompt_no_styles], [prompt_spaces], [ширина], [высота], [стили], [сэмплер], [seed], [model_hash], [prompt_words], [ дата], [дата-время], [job_timestamp].`

Однако этот список будет пополняться новыми дополнениями. Вы можете получить актуальный список поддерживаемых тегов, наведя указатель мыши на метку «Шаблон имени файла изображений» в пользовательском интерфейсе.

Пример шаблона: `[seed]-[steps]-[cfg]-[sampler]-[prompt_spaces]`

Примечание о тегах «подсказки»: «[подсказка]» добавит символы подчеркивания между словами подсказки, в то время как «[prompt_spaces]» сохранит подсказку без изменений (проще снова скопировать/вставить в пользовательский интерфейс). `[prompt_words]` — это упрощенная и очищенная версия вашей подсказки, которая уже использовалась для создания имен подкаталогов, только со словами вашей подсказки (без пунктуации).

Если вы оставите это поле пустым, будет применен шаблон по умолчанию (`[seed]-[prompt_spaces]`).

Обратите внимание, что теги фактически заменяются внутри шаблона. Это означает, что вы также можете добавить к этому шаблону слова, не являющиеся тегами, чтобы сделать имена файлов еще более явными. Например: `s=[seed],p=[prompt_spaces]`

# Пользовательские скрипты
Если программа запущена с параметром `--allow-code`, появится дополнительное поле ввода текста для кода скрипта.
доступен внизу страницы в разделе Скрипты -> Пользовательский код. Это позволяет вам вводить python
код, который будет работать с изображением.

В коде доступ к параметрам из веб-интерфейса с помощью переменной `p` и предоставление выходных данных для веб-интерфейса.
с помощью функции display(images, seed, info). Также доступны все глобалы из скрипта.

Простой скрипт, который просто обработает изображение и выведет его в обычном режиме:

```python
import modules.processing

processed = modules.processing.process_images(p)

print("Seed was: " + str(processed.seed))

display(processed.images, processed.seed, processed.info)
```

# Конфигурация пользовательского интерфейса
Вы можете изменить параметры элементов пользовательского интерфейса:
- группы радио: выбор по умолчанию
- ползунки: значение по умолчанию, мин., макс., шаг
- флажки: отмеченное состояние
- ввод текста и чисел: значения по умолчанию

Файл ui-config.json находится в каталоге webui, и он создается автоматически, если у вас его нет при запуске программы.

Флажки, которые обычно расширяют скрытый раздел, изначально не будут этого делать, если они установлены в качестве записей конфигурации пользовательского интерфейса.

Некоторые настройки нарушат обработку, например, шаг, не кратный 64 для ширины и высоты, а некоторые, например, изменение значения по умолчанию.
на вкладке img2img, может нарушить пользовательский интерфейс. У меня нет планов обращаться к ним в ближайшем будущем.

#ЕСРГАН
Возможно использование моделей ESRGAN на вкладке «Дополнительно», а также в апскейле SD.

Чтобы использовать модели ESRGAN, поместите их в каталог ESRGAN в том же месте, что и webui.py.
Файл будет загружен как модель, если он имеет расширение .pth. Возьмите модели из [базы данных моделей](https://upscale.wiki/wiki/Model_Database).

Поддерживаются не все модели из базы данных. Все модели 2x, скорее всего, не поддерживаются.

# альтернативный тест img2img
Деконструирует входное изображение, используя обратный диффузор Эйлера, чтобы создать шаблон шума, используемый для создания входной подсказки.

В качестве примера можно использовать это изображение. Выберите альтернативный тест img2img в разделе *scripts*.

![alt_src](https://user-images.githubusercontent.com/1633844/191771623-6293ec7b-c1c0-425c-9fe9-9d03313761fb.png)

Настройте параметры процесса реконструкции:
- Используйте краткое описание сцены: «Улыбающаяся женщина с каштановыми волосами». Описание функций, которые вы хотите изменить, помогает. Установите это как стартовую подсказку и «Исходную подсказку ввода» в настройках скрипта.
- Вы *ДОЛЖНЫ* использовать метод выборки Эйлера, так как этот скрипт построен на нем.
- Шаги выборки: 50-60. Это НАМНОГО совпадает со значением шагов декодирования в сценарии, иначе у вас будут плохие времена. Используйте 50 для этой демонстрации.
- Шкала CFG: 2 или ниже. Для этой демонстрации используйте 1.8. (Подсказка: вы можете отредактировать ui-config.json, чтобы изменить «img2img/CFG Scale/step» на .1 вместо .5.
- Сила шумоподавления - это *имеет* значение, вопреки тому, что говорилось в старых документах. Установите его на 1.
- Ширина/Высота - Используйте ширину/высоту входного изображения.
- Сид... можешь не обращать на это внимания. Обратный Эйлер теперь генерирует шум для изображения.
- Масштаб декодирования cfg - где-то ниже 1 - самое приятное место. Для демонстрации используйте 1.
- Шаги декодирования - как упоминалось выше, это должно соответствовать вашим шагам выборки. 50 для демонстрации, рассмотрите возможность увеличения до 60 для более подробных изображений.

После того, как все вышеперечисленное будет выполнено, вы сможете нажать «Создать» и получить результат, *очень* близкий к оригиналу.

Убедившись, что сценарий повторно создает исходную фотографию с хорошей степенью точности, вы можете попробовать изменить детали подсказки. Более крупные вариации оригинала, скорее всего, приведут к тому, что изображение будет иметь совершенно другую композицию, чем исходное изображение.

Пример вывода с использованием указанных выше настроек и приведенных ниже подсказок (рыжие волосы/пони не показаны)

![демо](https://user-images.githubusercontent.com/1633844/191776138-c77bf232-1981-47c9-a4d3-ae155631f5c8.png)

«Улыбающаяся женщина с голубыми волосами». Работает.
«Хмурая женщина с каштановыми волосами». Работает.
«Хмурая женщина с рыжими волосами». Работает.
«Нахмуренная женщина с рыжими волосами верхом на лошади». Кажется, мы полностью заменили женщину, и теперь у нас есть рыжая пони.

# пользователь.css
Создайте файл с именем `user.css` рядом с `webui.py` и поместите в него собственный код CSS. Например, это делает галерею выше:

```css
#txt2img_gallery, #img2img_gallery{
    min-height: 768px;
}
```
Полезный совет: вы можете добавить `/?__theme=dark` к URL-адресу веб-интерфейса, чтобы включить встроенную * темную тему *.
<br>напр. (`http://127.0.0.1:7860/?__theme=темный`)

Кроме того, вы можете добавить `--theme=dark` к `set COMMANDLINE_ARGS=` в `webui-user.bat`<br>
например `установить COMMANDLINE_ARGS=--theme=темный`


![chrome_O1kvfKs1es](https://user-images.githubusercontent.com/39339941/197560013-51e535d6-7cef-4946-ab6b-747e1c76b007.png)

# уведомление.mp3
Если в корневой папке webui присутствует аудиофайл с именем `notification.mp3`, он будет воспроизведен после завершения процесса генерации.

Как источник вдохновения:
* https://pixabay.com/sound-effects/search/ding/?duration=0-30
* https://pixabay.com/sound-effects/search/notification/?duration=0-30

# Твики

## Игнорировать последние слои модели CLIP
Это ползунок в настройках, и он определяет, насколько рано должна быть остановлена ​​обработка подсказки сетью CLIP.

Более подробное объяснение:

CLIP — это очень продвинутая нейронная сеть, которая преобразует ваш текст подсказок в числовое представление. Нейронные сети очень хорошо работают с этим числовым представлением, поэтому разработчики SD выбрали CLIP в качестве одной из 3 моделей, используемых в методе стабильной диффузии для создания изображений. Поскольку CLIP — это нейронная сеть, это означает, что в ней много слоев. Ваша подсказка оцифровывается простым способом, а затем передается через слои. Вы получаете числовое представление приглашения после 1-го уровня, вы передаете его во второй уровень, вы передаете результат этого в третий и т. д., пока не дойдете до последнего уровня, и это вывод CLIP, который используется в стабильной версии. диффузия. Это значение ползунка равное 1. Но вы можете остановиться раньше и использовать вывод предпоследнего слоя — это значение ползунка равное 2. Чем раньше вы остановитесь, тем меньше слоев нейронной сети обработает подсказку.

Некоторые модели были обучены с такой настройкой, поэтому установка этого значения помогает добиться лучших результатов на этих моделях.
