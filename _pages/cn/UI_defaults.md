---
title: 更改用户界面默认值
layout: post
category: Getting started
permalink: /ui-defaults/
priority: 2
machine_translated: true
lang: cn
---
Web UI 中的默认值可以通过编辑 `ui-config.json` 来更改，它在第一次运行后出现在包含 `webui.py` 的基本目录中。
更改仅在重新启动后应用。

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
