---
title: Локализация
layout: post
category: Guides
permalink: /localization/
machine_translated: true
lang: ru
---
# Использование файлов локализации
Предполагаемый способ локализации сейчас — через расширения. Видеть:
https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Разработка-расширения

# Создание файлов локализации
Перейдите в настройки и нажмите кнопку «Загрузить шаблон локализации» внизу. Это загрузит шаблон для локализации, который вы сможете редактировать.

# Обновление старой локализации новыми ключами

[Этот репозиторий] (https://github.com/AUTOMATIC1111/stable-diffusion-webui-old-localizations) содержит старые потерянные локализации. Если вы хотите обновить их новыми ключами, вы можете использовать следующий скрипт:

```python
import json
files=['localization_template.json', 'old_localization.json']

with open('new_localization.json', "w") as outfile:
    res = dict()
    for f in files:
        dct = dict(json.load(open(f, "r").read()))
        res.update(dct)
    outfile.write(res)
```

Затем переведите то, что было добавлено.
