---
title: Изменение настроек интерфейса
layout: post
category: getting started
permalink: /ui-defaults/
lang: ru
---
Значения по умолчанию в веб-интерфейсе можно изменить, отредактировав файл `ui-config.json`, который появляется в базовом каталоге, содержащем `webui.py`, после первого запуска. Изменения применяются только после перезапуска.

```json
{
    "txt2img/Sampling Steps/value": 20,
    "txt2img/Sampling Steps/minimum": 1,
    "txt2img/Sampling Steps/maximum": 150,
    "txt2img/Sampling Steps/step": 1,
    "txt2img/Batch count/value": 1,
    "txt2img/Batch count/minimum": 1,
    "txt2img/Batch count/maximum": 32,
    "txt2img/Batch count/step": 1,
    "txt2img/Batch size/value": 1,
    "txt2img/Batch size/minimum": 1,
    # ...
}
```
