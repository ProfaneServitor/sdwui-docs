---
layout: home
title: Docs readme
lang: en
permalink: /docs-readme
---

This is docs translation repository for Stable Diffusion web User Interface.

## How to translate a page

All content is in _pages folder. Copy a page from en folder, change language in header and translate its content.

## How to add a language

Add a language code in `_config_yml`, `languages` variable. Then create a folder of the same name in `_pages` folder..

## Compile

Currently github actions are broken, so the thing needs to be built before changes on site are rendered.

```
bundle
bundle exec jekyll build
```

## Credits

* Powered by [Jekyll](https://jekyllrb.com/)
* [Gitbook theme](https://github.com/sighingnow/jekyll-gitbook) by Tao He
*
