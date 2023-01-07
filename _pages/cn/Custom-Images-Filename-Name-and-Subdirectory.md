---
title: 自定义图像文件名和子目录
layout: post
category: Guides
permalink: /custom-filenames/
machine_translated: true
lang: cn
---
> 以下信息是关于图像文件名和子目录名，不是`Paths for saving \ Output directorys`
### 默认情况下，Wub UI 将图像保存在输出目录中，文件名结构为

`number`-`seed`-`[prompt_spaces]`

```
01234-987654321-((masterpiece)), ((best quality)), ((illustration)), extremely detailed,style girl.png
```

如果用户愿意，可以使用不同的图像文件名和可选的子目录。

图片文件名模式可以配置在.

`设置选项卡` > `保存图像/网格` > `图像文件名模式`

子目录可以在设置下配置。

`设置选项卡` > `保存到目录` > `目录名称模式`

# 彭定康
Web-Ui 提供了几种模式，可用作将信息插入文件名或子目录的占位符，
用户可以将这些模式链接在一起，形成适合其用例的文件名。

|图案 |说明 |示例 |
|--------------------------------|------------------------------------------------------|---------------------------------------------|

| `[种子]` |种子 | 1234567890 |
| `[步骤]` |步骤 | 20 |
| `[cfg]` | CFG规模 | 7 |
| `[采样器]` |取样方法 |欧拉 |
| `[模型哈希]` |模型的哈希 | 7460a6fa |
| `[宽度]` |图片宽度 | 512|
| `[身高]` |图片高度 | 512|
| `[样式]` |所选样式的名称 |我的风格名称 |
| `[日期]` | ISO 格式的计算机日期 | 2022-10-24 |
| `[日期时间]` | “%Y%m%d%H%M%S”中的日期时间 | 20221025013106 |
| `[日期时间<格式>]` |指定\<格式\> 中的日期时间 | \[日期时间<%Y%m%d_%H%M%S_%f>]<br>20221025_014350_733877 |
| `[日期时间<格式><时区>]` |指定\<格式\> 中特定\<Time Zone\> 的日期时间 | \[日期时间<%Y%m%d_%H%M%S_%f><亚洲/东京>]`<br>20221025_014350_733877 |
| `[prompt_no_styles]` |无样式提示 | 1gir，空白，（（非常重要）），[不重要]，（一些值_1.5），（随便），结束|
| [提示空格] |提示样式 | 1gir, 空白, ((非常重要)), [不重要], (some value_1.5), (whatever), 结束, <br> (((crystals texture Hair)))，((( |
| [提示] |提示样式，空格键替换为 _ | 1gir,\_\_\_white_space,\_((very\_important)),\_[不\_important],\_(some\_value\_1.5),\_(whatever),\_the\_end, \_(((crystals_texture_Hair)))，((( |
| [提示词] |删除了样式、括号和逗号的提示 | 1gir white space very important not important some value 1 5 whatever the end crystals texture Hair, extremely detailed |

### 日期时间格式详细信息
有关 [格式代码](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) 的更多详细信息，请参考 python 文档

### 日期时间时区详细信息
参考 [List of Time Zones](../list-of-time-zones/) 以获取有效时区列表

如果 `<Format>` 为空或无效，它将使用默认时间格式“%Y%m%d%H%M%S”
提示：您可以在 `<Format>` 中使用额外的字符作为标点符号，例如 `_ -`

如果 `<TimeZone>` 为空或无效，它将使用默认的系统时区

用于上述“[prompt]”示例的提示和样式

迅速的：
```
1gir,   white space, ((very important)), [not important], (some value:1.5), (whatever), the end
```
精选款式：
```
(((crystals texture Hair)))，(((((extremely detailed CG))))),((8k_wallpaper))
```

注意：上面提到的`Styles`是指generate按钮下方的两个下拉菜单

###如果提示太长，它会很短
这是由于计算机有最大文件长度

# 保存时在文件名中添加/删除数字
您可以删除前缀号码
通过取消选中下面的复选框

`Setting` > `Saving images/grids` > `Add number to filename when saving`

带前缀号码
```
00123-`987654321-((masterpiece)).png
```

没有前缀号码
```
987654321-((masterpiece)).png
```

### 注意
前缀号的作用是保证保存的图片文件名是**唯一**的。
如果您决定不使用前缀数字，请确保您的模式将生成一个唯一的文件名，

**否则文件可能会被覆盖**。

一般datetime精确到秒应该可以保证文件名是唯一的。

```
[datetime<%Y%m%d_%H%M%S>]-[seed]
```
```
20221025_014350-281391998.png
```

但是对于一些**自定义脚本**可能会在**单批**中使用**相同的种子**生成**多个图像**，

在这种情况下，更安全的做法是将“微秒”也使用“%f”作为十进制数，用零填充到 6 位数字。

```
[datetime<%Y%m%d_%H%M%S_%f>]-[seed]
```
```
20221025_014350_733877-281391998.png
```

# 文件名模式示例

如果您在多台机器上运行 Web-Ui，例如在 Google Colab 和您自己的计算机上，您可能希望使用带有时间前缀的文件名。
这样当您下载犯规时，您可以将它们放在同一个文件夹中。

此外，由于您不知道 Google Colab 使用的时区，因此您需要指定时区。
```
[datetime<%Y%m%d_%H%M%S_%f><Asia/Tokyo>]-[seed]-[prompt_words]
```
```
20221025_032649_058536-3822510847-1girl.png
```

设置子目录的日期可能也很有用，这样一个文件夹就不会有太多图像
```
[datetime<%Y-%m-%d><Asia/Tokyo>]
```
```
2022-10-25
```
