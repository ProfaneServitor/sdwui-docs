---
title: 本土化
layout: post
category: Guides
permalink: /localization/
machine_translated: true
lang: cn
---
# 使用本地化文件
现在进行本地化的预期方法是通过扩展。看：
https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Developing-extensions

# 创建本地化文件
转到设置并单击底部的“下载本地化模板”按钮。这将下载一个您可以编辑的本地化模板。

# 使用新密钥更新旧本地化

[此存储库](https://github.com/AUTOMATIC1111/stable-diffusion-webui-old-localizations) 包含旧的孤立本地化。如果你想用新密钥更新它们，你可以使用以下脚本：

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

然后翻译添加的内容。
