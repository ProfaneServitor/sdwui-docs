---
title: 测试
layout: post
category: development
permalink: /tests
machine_translated: true
lang: cn
---
＃＃ 入门

{% assign nestedarray = 'install, dependencies' |split: ',' %}

{% for link in nestedarray %}
* [{{链接}}]（{{链接}}）
{% endfor %}

## 指南

＃＃ 发展


有一些测试只是验证基本图像创建是否适用于 vi API。

要运行测试，请将 `--tests` 作为命令行参数添加到 `launch.py​​` 以及其他命令行参数：

```
python launch.py --skip-torch-cuda-test --deepdanbooru --no-half-vae --tests
```

您会在 `test/stdout.txt` 和 `test/stderr.txt` 中找到主程序的输出。
