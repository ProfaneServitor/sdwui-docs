---
title: Tests
layout: post
category: development
permalink: /tests
lang: en
---
## Getting started

{% assign nestedarray = 'install, dependencies' |split: ',' %}

{% for link in nestedarray %}
  * [{{ link }}]({{ link }})
{% endfor %}

## Guides

## Development


There are tests that just verify that basic image creation works vi API.

To run tests, add `--tests` as a commandline argument to `launch.py` along with your other command line arguments:

```
python launch.py --skip-torch-cuda-test --deepdanbooru --no-half-vae --tests
```

You'll find outputs of main program in `test/stdout.txt` and `test/stderr.txt`.
