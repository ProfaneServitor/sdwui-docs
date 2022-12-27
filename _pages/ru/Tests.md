---
title: Тесты
layout: post
category: development
permalink: /tests
machine_translated: true
lang: ru
---
Есть тесты, которые просто проверяют, работает ли базовое создание образов через API.

Чтобы запустить тесты, добавьте `--tests` в качестве аргумента командной строки для `launch.py` вместе с другими аргументами командной строки:

```
python launch.py --skip-torch-cuda-test --deepdanbooru --no-half-vae --tests
```

Вы найдете выходные данные основной программы в `test/stdout.txt` и `test/stderr.txt`.
