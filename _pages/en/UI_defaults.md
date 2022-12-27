---
title: Changing UI defaults
layout: post
category: Getting started
permalink: /ui-defaults/
priority: 2
lang: en
---
{% include machine-translated.html %}
The default values in the web UI can be changed by editing `ui-config.json`, which appears in the base directory containing `webui.py` after the first run.
The changes are only applied after restarting.

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
