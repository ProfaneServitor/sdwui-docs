---
title: 开发扩展
layout: post
category: development
permalink: /developing-extensions/
machine_translated: true
lang: cn
---
扩展只是 extensions 目录中的一个子目录。

Web ui 通过以下方式与已安装的扩展进行交互：

- 执行扩展的“install.py”脚本（如果存在）。
- `scripts` 目录中的扩展脚本就像普通用户脚本一样执行，除了：
- `sys.path` 被扩展为包含扩展目录，因此您可以放心地导入其中的任何内容
- 你可以使用 `scripts.basedir()` 来获取当前扩展的目录（因为用户可以随意命名）
- 将 `javascript` 目录中的扩展的 javascript 文件添加到页面
- `localizations` 目录中扩展的本地化文件被添加到设置中；如果有两个具有相同名称的本地化，则不会合并它们，一个替换另一个。
- 扩展的 `style.css` 文件被添加到页面
- 如果扩展在其根目录中有 `preload.py` 文件，则在解析命令行参数之前加载它
- 如果扩展的 `preload.py` 有一个 `preload` 函数，它被调用，命令行参数解析器作为参数传递给它。以下是如何使用它添加命令行参数的示例：
```python
def preload(parser):
    parser.add_argument("--wildcards-dir", type=str, help="directory with wildcards", default=None)
```

有关如何开发自定义脚本（通常会完成扩展的大部分工作）的信息，请参阅[开发自定义脚本](../Developing-custom-scripts)。

## 本地化扩展
为项目进行本地化的首选方法是通过扩展。扩展的基本文件结构应该是：

```

 📁 webui root directory
 ┗━━ 📁 extensions
     ┗━━ 📁 webui-localization-la_LA        <----- name of extension

         ┗━━ 📁 localizations                <----- the single directory inside the extension

             ┗━━ 📄 la_LA.json              <----- actual file with translations

```

使用此文件结构创建一个 github 存储库，并要求合作者部分中列出的任何人将您的扩展添加到 wiki。

如果您的语言需要 javascript/css 甚至 python 支持，您也可以将其添加到扩展中。

## 安装.py
`install.py` 是启动器 `launch.py​​` 在 webui 启动之前在一个单独的进程中启动的脚本，它的目的是安装扩展的依赖项。它必须位于扩展的根目录中，而不是脚本目录中。该脚本在 `PYTHONPATH` 环境变量设置为 webui 路径的情况下启动，因此您只需 `import launch` 并使用其功能：

```python
import launch

if not launch.is_installed("aitextgen"):
    launch.run_pip("install aitextgen==0.6.0", "requirements for MagicPrompt")
```
