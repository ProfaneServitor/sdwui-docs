---
title: Contributing
layout: post
category: development
permalink: /contributing/
lang: en
---

[features](../Features)

# Pull requests

To contribute, clone the repository, make your changes, commit and push to your clone, and submit a pull request.

Make sure that your changes do not break anything by running [tests](Tests).

If you're adding a lot of code, consider making your contribution an [extension](Extensions), and only PR small changes you need in main code to make the extension possible.

If you are making changes to used libraries or the installation script, you must verify them to work on default Windows installation from scratch. If you cannot test if it works (due to your OS or anything else), do not make those changes (with possible exception of changes that explicitly are guarded from being executed on Windows by `if`s or something else).

# Code style
I mostly follow code style suggested by PyCharm, with the exception of disabled line length limit. Please do not submit PRs where you just take existing lines and reformat them without changing what they do.

# Gradio
Gradio at some point wanted to add this section to shill their project in the contributing section, which I didn't have at the time, so here it is now.

For [Gradio](https://github.com/gradio-app/gradio) check out the [docs](https://gradio.app/docs/) to contribute:
Have an issue or feature request with Gradio? open a issue/feature request on github for support: https://github.com/gradio-app/gradio/issues
