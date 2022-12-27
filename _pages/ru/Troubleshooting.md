---
title: Исправление проблем
layout: post
category: Guides
permalink: /troubleshooting/
machine_translated: true
lang: ru
---
- **Программа протестирована для работы на Python 3.10.6. Не используйте другие версии, если только вы не ищете проблем.**
- Установщик создает виртуальную среду Python, поэтому ни один из установленных модулей не повлияет на существующие системные установки Python.
- Чтобы использовать системный python вместо создания виртуальной среды, используйте пользовательский параметр, заменяющий `set VENV_DIR=-`.
- Для переустановки с нуля удалите каталоги: `venv`, `repositories`.
- При первом запуске программы отображается путь к интерпретатору python. Если это не тот питон, который вы установили, вы можете указать полный путь в скрипте `webui-user`; см. [Запуск с пользовательскими параметрами](Запуск с пользовательскими параметрами).
- Если нужной версии Python нет в PATH, измените строку `set PYTHON=python` в `webui-user.bat`, указав полный путь к исполняемому файлу python.
- Пример: `set PYTHON=B:\soft\Python310\python.exe`
- Требования к установщику из `requirements_versions.txt`, в котором перечислены версии модулей, специально совместимых с Python 3.10.6. Если это не работает с другими версиями Python, может помочь установка пользовательского параметра `set REQS_FILE=requirements.txt`.

# Видеокарты с низким VRAM
При работе на видеокартах с небольшим объемом видеопамяти (<=4 ГБ) могут возникать ошибки нехватки памяти.
Различные оптимизации могут быть включены с помощью аргументов командной строки, жертвуя некоторой/большой скоростью в пользу использования меньшего количества видеопамяти:
- Если у вас 4 ГБ видеопамяти и вы хотите создавать изображения размером 512x512 (или, возможно, до 640x640), используйте --medvram.
- Если у вас 4 ГБ видеопамяти и вы хотите создавать изображения 512x512, но вы получаете сообщение об ошибке нехватки памяти с помощью `--medvram`, используйте вместо этого `--medvram --opt-split-attention`.
- Если у вас 4 ГБ видеопамяти и вы хотите создавать образы 512x512, но вы все еще получаете сообщение об ошибке нехватки памяти, используйте вместо этого `--lowvram --always-batch-cond-uncond --opt-split-attention`.
- Если у вас 4 ГБ видеопамяти и вы хотите сделать изображения больше, чем вы можете с помощью `--medvram`, используйте `--lowvram --opt-split-attention`.
- Если у вас больше видеопамяти и вы хотите создавать изображения большего размера, чем обычно (например, 1024x1024 вместо 512x512), используйте `--medvram --opt-split-attention`. Вы также можете использовать `--lowvram`, но эффект, скорее всего, будет едва заметен.
- В противном случае не используйте ни один из них.

# Зеленый или черный экран
Видеокарты
При работе на видеокартах, которые не поддерживают числа с плавающей запятой половинной точности (известная проблема с картами 16xx), вместо сгенерированных изображений может появиться зеленый или черный экран.
Это можно исправить, используя аргументы командной строки `--precision full --no-half` при значительном увеличении использования VRAM, что может потребовать `--medvram`.

# "Ошибка CUDA: образ ядра недоступен для выполнения на устройстве" после включения xformers
Установленные вами xformers несовместимы с вашим графическим процессором. Если вы используете Python 3.10, имеете карту Pascal или выше и работаете в Windows, добавьте `--reinstall-xformers --xformers` в свой `COMMANDLINE_ARGS` для обновления до рабочей версии. Удалите --reinstall-xformers после обновления.

# NameError: имя 'xformers' не определено
Если вы используете Windows, это означает, что ваш Python слишком стар. Используйте 3.10

Если Linux, вам придется создавать xformers самостоятельно или просто избегать использования xformers.