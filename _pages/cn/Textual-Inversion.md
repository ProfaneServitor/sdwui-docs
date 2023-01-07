---
title: 文字倒置
layout: post
category: Guides
permalink: /textual-inversion/
machine_translated: true
lang: cn
---
# 什么是文本倒置？
Textual Inversion 允许您在自己的图片上训练神经网络的一小部分，并在生成新图片时使用结果。在这种情况下，嵌入是您训练的神经网络的一小部分的名称。

训练的结果是一个 .pt 或 .bin 文件（前者是原作者使用的格式，后者是扩散器库使用的格式），其中包含嵌入。

有关什么是文本反转的更多详细信息，请参见原始站点：https://textual-inversion.github.io/。

# 使用预训练嵌入
将嵌入放入 embeddings 目录并在提示中使用其文件名。您不必重新启动程序即可使其工作。

例如，这里是 [Usada Pekora](https://drive.google.com/file/d/1MDSmzSbzkIcw5_aw_i79xfO3CRWQDl-8/view?usp=sharing) 的嵌入，我在 WD1.2 模型上训练了 53 张图片（ 119 增加）19500 步，每个标记设置 8 个向量。

它生成的图片：
![grid-0037](https://user-images.githubusercontent.com/20920490/193285043-5d5d57d8-7b5e-4803-a211-5ca5220c35f4.png)
```
portrait of usada pekora
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 4077357776, Size: 512x512, Model hash: 45dee52b
```

您可以在一个提示中组合多个嵌入：
![grid-0038](https://user-images.githubusercontent.com/20920490/193285265-a5224378-4ae2-48bf-ad7d-e79a9f998f9c.png)
```
portrait of usada pekora, mignon
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 4077357776, Size: 512x512, Model hash: 45dee52b
```

非常小心你使用的是哪种模型与你的嵌入：它们与你在训练期间使用的模型一起工作得很好，但在不同的模型上不太好。例如，这里是上面的嵌入和香草 1.4 稳定扩散模型：
![grid-0036](https://user-images.githubusercontent.com/20920490/193285611-486373f2-35d0-437c-895a-71454564a7c4.png)
```
portrait of usada pekora
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 4077357776, Size: 512x512, Model hash: 7460a6fa
```

# 训练嵌入
## 文本反转选项卡
对用户界面中训练嵌入的实验支持。
- 创建一个新的空嵌入，选择带有图像的目录，在其上训练嵌入
- 该功能非常原始，使用风险自负
- 经过几万步后，我能够重现我在其他回购协议中将动漫艺术家训练为风格的结果
- 适用于半精度浮点数，但需要试验以查看结果是否同样好
- 如果你有足够的内存，使用 `--no-half --precision full` 运行更安全
- 用于自动运行图像预处理的 UI 部分。
- 你可以在不丢失任何数据的情况下中断和恢复训练（AdamW 优化参数除外，但似乎现有的回购协议都没有保存这些参数，所以一般认为它们并不重要）
- 不支持批量大小或梯度累积
- 不应使用 `--lowvram` 和 `--medvram` 标志来运行它。

## 参数说明

### 创建嵌入
- **名称**：创建嵌入的文件名。在提及嵌入时，您还将在提示中使用此文本。
- **初始化文本**：您创建的嵌入最初将填充此文本的向量。如果您创建一个名为“zzzz1234”的单向量嵌入，并将“tree”作为初始化文本，并在提示中使用它而不进行训练，那么提示“a zzzz1234 by monet”将产生与“a tree by monet”相同的图片。
- **每个标记的向量数量**：嵌入的大小。这个值越大，你可以嵌入到主题中的信息就越多，但它会从你的提示容许量中拿走的词也越多。对于稳定扩散，您在提示中有 75 个标记的限制。如果您在提示中使用包含 16 个向量的嵌入，那将为您留出 75 - 16 = 59 的空间。同样根据我的经验，向量的数量越多，获得良好结果所需的图片就越多。

### 预处理
这从目录中获取图像，处理它们以准备好进行文本反转，并将结果写入另一个目录。这是一个方便的功能，您可以根据需要自行预处理图片。
- **源目录**：包含图像的目录
- **目标目录**：将写入结果的目录
- **创建翻转副本**：对于每个图像，还写入其镜像副本
- **将超大图像一分为二**：如果图像太高或太宽，调整其大小以使其短边与所需分辨率相匹配，并从中创建两个可能相交的图片。
- **使用 BLIP 标题作为文件名**：使用询问器的 BLIP 模型为文件名添加标题。

### 训练嵌入
- **嵌入**：从此下拉列表中选择要训练的嵌入。
- **学习率**：训练应该进行多快。将此参数设置为较高值的危险在于，如果将其设置得太高，则可能会破坏嵌入。如果你在训练信息文本框中看到“Loss: nan”，这意味着你失败了，嵌入已经死了。使用默认值，这不应该发生。可以使用以下语法在此设置中指定多个学习率：`0.005:100, 1e-3:1000, 1e-5` - 这将在前 100 步使用 `0.005` 的 lr 进行训练，然后是 `1e-3 ` 直到 1000 步，然后 `1e-5` 直到结束。
- **数据集目录**：包含用于训练的图像的目录。它们都必须是正方形的。
- **日志目录**：样本图像和部分训练嵌入的副本将写入此目录。
- **提示模板文件**：带有提示的文本文件，每行一个，用于训练模型。请参阅目录“textual_inversion_templates”中的文件，了解您可以使用这些文件做什么。在训练样式时使用 `style.txt`，在训练对象嵌入时使用 `subject.txt`。文件中可以使用以下标签：
- `[name]`: 嵌入的名称
- `[filewords]`：来自数据集中图像文件名的单词。有关更多信息，请参见下文。
- **最大步数**：训练将在完成这么多步后停止。一个步骤是当一张图片（或一批图片，但目前不支持批量）显示给模型并用于改进嵌入。如果您中断训练并在稍后恢复，则步数会保留。
- **保存嵌入 PNG 块中的图像**：每次生成图像时，它都会与最近记录的嵌入相结合，并以既可以作为图像共享又可以放入嵌入文件夹的格式保存到 image_embeddings并加载。
- **预览提示**：如果不为空，该提示将用于生成预览图片。如果为空，将使用培训提示。

### 文件字
`[filewords]` 是提示模板文件的标签，允许您将文件名中的文本插入到提示中。默认情况下，文件的扩展名以及文件名开头的所有数字和破折号 (`-`) 都被删除。所以这个文件名：`000001-1-a man in suit.png` 将变成提示文本：`a man in suit`。文件名中的文本格式保持原样。

可以使用选项 `Filename word regex` 和 `Filename join string` 来改变文件名中的文本：例如，使用 word regex = `\w+` 和 join string = `, `，上面的文件将产生这个文本: `a, man, in, suit`。正则表达式用于从文本中提取单词（它们是 `['a', 'man', 'in', 'suit', ]`），并在这些单词之间放置连接字符串 (', ') 以创建一个文本：`a, man, in, suit`。

也可以创建一个与图像文件名相同的文本文件（`000001-1-a man in suit.txt`），然后将提示文本放在那里。不会使用文件名和正则表达式选项。

## 第三方回购
我使用这些存储库成功地训练了嵌入：

- [nicolai256](https://github.com/nicolai256/Stable-textual-inversion_win)
- [lstein](https://github.com/invoke-ai/InvokeAI)

其他选择是在 colabs 上训练和/或使用扩散器库，我对此一无所知。

# 在线查找嵌入

- [huggingface 概念库](https://cyberes.github.io/stable-diffusion-textual-inversion-models/) - 很多不同的嵌入，但是
- [16777216c](https://gitlab.com/16777216c/stable-diffusion-embeddings) - NSFW，一个神秘陌生人的动漫艺术家风格。
- [cattoroboto](https://gitlab.com/cattoroboto/waifu-broadcast-embeds) - anon 的一些动漫嵌入。
- [viper1](https://gitgud.io/viper1/stable-diffusion-embeddings) - NSFW，毛茸茸的女孩。
- [anon 的嵌入](https://mega.nz/folder/7k0R2arB#5_u6PYfdn-ZS7sRdoecD2A) - NSFW，动漫艺术家。
- [rentry](https://rentry.org/embeddings) - 一个包含来自许多来源的嵌入链接的页面。

# 超网络

Hypernetworks 是一个新颖的（明白吗？）概念，用于在不影响其任何权重的情况下微调模型。

当前训练超网络的方法是在文本反转选项卡中。

训练的工作方式与文本倒置相同。

唯一的要求是使用非常非常低的学习率，比如 0.000005 或 0.0000005。

### 愚蠢的愚蠢的指南
一位匿名用户编写了一份使用超网络的图片指南：https://rentry.org/hypernetwork4dumdums

### 训练时从 VRAM 中卸载 VAE 和 CLIP
设置选项卡上的此选项允许您以较慢的预览图片生成为代价节省一些内存。
