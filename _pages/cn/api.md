---
title: API指南
author: Kilvoctu
layout: post
category: Guides
permalink: /api/
machine_translated: true
lang: cn
---
- 首先，当然是使用 `--api` 命令行参数运行 web ui
- 在你的“webui-user.bat”中的例子：`set COMMANDLINE_ARGS=--api`
- 这会启用可在 http://127.0.0.1:7860/docs（或任何 URL 为 + /docs）查看的 api
我感兴趣的基本是这两个。让我们只关注`/sdapi/v1/txt2img`

![图片](https://user-images.githubusercontent.com/2993060/198171114-ed1c5edd-76ce-4c34-ad73-04e388423162.png)

- 当您展开该选项卡时，它会提供一个要发送到 API 的负载示例。我经常用这个作为参考。

![图片](https://user-images.githubusercontent.com/2993060/198171454-5b826ded-5e73-4249-9c0c-a97b32c42569.png)

------


- 这就是后端。 API 基本上说明了可用的内容、要求的内容以及将其发送到哪里。现在转到前端，我将开始使用我想要的参数构建有效负载。一个例子可以是：
```
payload = {
    "prompt": "maltese puppy",
    "steps": 5
}
```
我可以在有效载荷中放入尽可能少或尽可能多的参数。 API 将对我未设置的任何内容使用默认值。

- 之后，我可以将它发送到 API
```
response = requests.post(url=f'http://127.0.0.1:7860/sdapi/v1/txt2img', json=payload)
```
同样，此 URL 需要与 Web 用户界面的 URL 相匹配。
如果我们执行此代码，Web UI 将根据负载生成图像。那很好，但那又怎样呢？哪里都没有图。。。

------


- 在后端完成它的工作后，API 将响应发送回上面分配的变量：`response`。响应包含三个条目； “图像”、“参数”和“信息”，我必须想办法从这些条目中获取信息。
- 首先，我放置了这一行 `r = response.json()` 以便更容易处理响应。
- “图像”是生成的图像，这是我最想要的。没有链接或任何东西；这是一串巨大的随机字符，显然我们必须对其进行解码。我是这样做的：
```
for i in r['images']:
    image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))
```
- 这样，我们在 `image` 变量中就有了一张可以使用的图像，例如使用 `image.save('output.png')` 保存它。
- “参数”显示发送到 API 的内容，这可能很有用，但在这种情况下我想要的是“信息”。我用它来将元数据插入到图像中，这样我就可以将它放到 web ui PNG Info 中。为此，我可以访问`/sdapi/v1/png-info` API。我需要将上面得到的图像输入其中。
```
png_payload = {
        "image": "data:image/png;base64," + i
    }
    response2 = requests.post(url=f'http://127.0.0.1:7860/sdapi/v1/png-info', json=png_payload)
```
之后，我可以使用 `response2.json().get("info")` 获取信息

------


应该工作的示例代码如下所示：
```
import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin

url = "http://127.0.0.1:7860"

payload = {
    "prompt": "puppy dog",
    "steps": 5
}

response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

r = response.json()

for i in r['images']:
    image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

    png_payload = {
        "image": "data:image/png;base64," + i
    }
    response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

    pnginfo = PngImagePlugin.PngInfo()
    pnginfo.add_text("parameters", response2.json().get("info"))
    image.save('output.png', pnginfo=pnginfo)
```
- 导入我需要的东西
- 定义要发送的 url 和有效载荷
- 通过 API 将所述有效负载发送到所述 url
- 在循环中抓取“图像”并对其进行解码
- 对于每个图像，将其发送到 png 信息 API 并取回该信息
- 定义一个插件来添加png信息，然后将我定义的png信息添加到其中
- 最后，使用 png 信息保存图像

-----


关于“override_settings”的注释。
此端点的目的是覆盖单个请求的 Web UI 设置，例如 CLIP 跳过。可以传递到此参数的设置在 url 的 /docs 中可见。

![图片](https://user-images.githubusercontent.com/2993060/202877368-c31a6e9e-0d05-40ec-ade0-49ed2c4be22b.png)

您可以展开选项卡，API 将提供一个列表。有几种方法可以将此值添加到负载中，但我就是这样做的。我将使用“filter_nsfw”和“CLIP_stop_at_last_layers”进行演示。

```
payload = {
    "prompt": "cirno",
    "steps": 20
}

override_settings = {}
override_settings["filter_nsfw"] = true
override_settings["CLIP_stop_at_last_layers"] = 2

override_payload = {
                "override_settings": override_settings
            }
payload.update(override_payload)
```
- 有正常的有效载荷
- 之后，初始化一个字典（我称之为“override_settings”，但可能不是最好的名字）
- 然后我可以添加任意数量的键：值对
- 仅使用此参数创建一个新的有效载荷
- 更新原始有效载荷以将其添加到其中

所以在这种情况下，当我发送有效载荷时，我应该在 20 步时得到一个“cirno”，CLIP 跳过 2 步，并且 NSFW 过滤器打开。


对于某些设置或情况，您可能希望保留更改。为此，您可以发布到 `/sdapi/v1/options` API 端点
我们可以使用到目前为止学到的知识并为此轻松设置代码。这是一个例子：
```
url = "http://127.0.0.1:7860"

option_payload = {
    "sd_model_checkpoint": "Anything-V3.0-pruned.ckpt [2700c435]",
    "CLIP_stop_at_last_layers": 2
}

response = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload)
```
将此有效负载发送到 API 后，模型应切换到我设置的模型并将 CLIP 跳转设置为 2。重申一下，这与“override_settings”不同，因为此更改将持续存在，而“override_settings”是针对单个请求的.
请注意，如果您要更改 `sd_model_checkpoint`，则该值应该是检查点在 Web 用户界面中显示的名称。这可以通过此 API 端点引用（与我们引用“选项”API 的方式相同）

![图片](https://user-images.githubusercontent.com/2993060/202928589-114aff91-2777-4269-9492-2eab015c5bca.png)

“标题”（名称和散列）是您想要使用的。

-----


这是提交 [47a44c7](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/47a44c7e421b98ca07e92dbf88769b04c9e28f86)

要获得更完整的前端实现，如果有人想以我的 Discord 机器人为例，请点击 [此处](https://github.com/Kilvoctu/aiyabot)。大多数操作发生在 stablecog.py 中。有很多注释解释了每个代码的作用。

------


该指南可以在 [讨论](https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/3734) 页面中找到。

另外，查看这个用于 webui 的 python API 客户端库：https://github.com/mix1009/sdwebuiapi
