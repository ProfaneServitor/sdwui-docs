---
title: 否定提示
layout: post
category: Guides
permalink: /negative-prompt/
machine_translated: true
lang: cn
---
否定提示是一种使用 Stable Diffusion 的方式，允许用户指定他不想看到的内容，而无需对模型进行任何额外负载或要求。据我所知，我是第一个使用这种方法的人；添加它的提交是 [757bb7c4](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/757bb7c46b20651853ee23e3109ac4f9fb06a061)。该功能在用户中非常受欢迎，他们消除了稳定扩散的常见畸形，如额外的肢体。除了能够指定您不想看到的内容（有时可以通过通常的提示，有时则不能）之外，这还允许您在不使用任何 75 个令牌的情况下执行此操作，提示包括.

否定提示的工作方式是在进行采样时使用用户指定的文本而不是空字符串作为“unconditional_conditioning”。

这是来自 [txt2img.py](https://github.com/CompVis/stable-diffusion/blob/main/scripts/txt2img.py) 的（简化）代码：

```python
# prompts = ["a castle in a forest"]
# batch_size = 1

c = model.get_learned_conditioning(prompts)
uc = model.get_learned_conditioning(batch_size * [""])

samples_ddim, _ = sampler.sample(conditioning=c, unconditional_conditioning=uc, [...])
```

这将启动重复的采样器：
- 去噪图片引导它看起来更像你的提示（调节）
- 去噪图片引导它看起来更像一个空提示（unconditional_conditioning）
- 查看它们之间的差异并使用它来为嘈杂的图片产生一组变化（不同的采样器以不同的方式执行该部分）

要使用否定提示，所需要的只是：

```python
# prompts = ["a castle in a forest"]
# negative_prompts = ["grainy, fog"]

c = model.get_learned_conditioning(prompts)
uc = model.get_learned_conditioning(negative_prompts)

samples_ddim, _ = sampler.sample(conditioning=c, unconditional_conditioning=uc, [...])
```

然后，采样器将查看去噪后看起来像您的提示（城堡）的图像与去噪后看起来像您的负面提示（颗粒状、雾状）的图像之间的差异，并尝试将最终结果移向前者并远离后者。

＃＃＃ 例子：

```
a colorful photo of a castle in the middle of a forest with trees and (((bushes))), by Ismail Inceoglu, ((((shadows)))), ((((high contrast)))), dynamic shading, ((hdr)), detailed vegetation, digital painting, digital drawing, detailed painting, a detailed digital painting, gothic art, featured on deviantart
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 749109862, Size: 896x448, Model hash: 7460a6fa
```

| negative prompt     | image                                                                                                                     |
|---------------------|---------------------------------------------------------------------------------------------------------------------------|

|无 | ![01069-749109862](https://user-images.githubusercontent.com/20920490/192156368-18360487-0dcf-4b7d-b57e-b3fa80a81f1a.png) |
|雾| ![01070-749109862](https://user-images.githubusercontent.com/20920490/192156405-9c43ba8c-4eb8-415d-9f4d-902c8cf69b6d.png) |
|粒状 | ![01071-749109862](https://user-images.githubusercontent.com/20920490/192156421-17e53296-df5c-4e82-bf9a-f1ca562d3ad0.png) |
|雾，颗粒状 | ![01072-749109862](https://user-images.githubusercontent.com/20920490/192156430-3d05e5c4-2b86-409c-a357-a31178e0cb30.png) |
|雾，颗粒状，紫色 | ![01073-749109862](https://user-images.githubusercontent.com/20920490/192156440-ec59abe8-1a18-4372-a100-0da8bc1f8d13.png) |
