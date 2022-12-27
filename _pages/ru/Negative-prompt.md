---
title: Отрицательное приглашение
layout: post
category: Guides
permalink: /negative-prompt/
machine_translated: true
lang: ru
---
Отрицательное приглашение — это способ использования Stable Diffusion таким образом, чтобы пользователь мог указать то, что он не хочет видеть, без дополнительной нагрузки или требований к модели. Насколько я знаю, я был первым, кто использовал этот подход; коммит, который его добавляет, — [757bb7c4](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/757bb7c46b20651853ee23e3109ac4f9fb06a061). Эта функция нашла огромную популярность среди пользователей, которые удаляют с ее помощью обычные деформации Stable Diffusion, такие как лишние конечности. В дополнение к возможности указать, что вы не хотите видеть, что иногда возможно с помощью обычной подсказки, а иногда нет, это позволяет вам сделать это без использования каких-либо ваших разрешенных 75 токенов, из которых состоит подсказка. .

Способ работы отрицательного приглашения заключается в использовании указанного пользователем текста вместо пустой строки для `unconditional_conditioning` при выполнении выборки.

Вот (упрощенный) код из [txt2img.py](https://github.com/CompVis/stable-diffusion/blob/main/scripts/txt2img.py):

```python
# prompts = ["a castle in a forest"]
# batch_size = 1

c = model.get_learned_conditioning(prompts)
uc = model.get_learned_conditioning(batch_size * [""])

samples_ddim, _ = sampler.sample(conditioning=c, unconditional_conditioning=uc, [...])
```

Это запускает сэмплер, который многократно:
- убирает шумы с картинки, чтобы она больше походила на вашу подсказку (кондиционирование)
- устраняет шум изображения, делая его более похожим на пустую подсказку (unconditional_conditioning)
- смотрит на разницу между ними и использует ее для создания набора изменений для зашумленного изображения (разные сэмплеры делают эту часть по-разному)

Чтобы использовать отрицательную подсказку, все, что нужно, это:

```python
# prompts = ["a castle in a forest"]
# negative_prompts = ["grainy, fog"]

c = model.get_learned_conditioning(prompts)
uc = model.get_learned_conditioning(negative_prompts)

samples_ddim, _ = sampler.sample(conditioning=c, unconditional_conditioning=uc, [...])
```

Затем сэмплер рассмотрит различия между изображением, очищенным от шума, чтобы оно выглядело как ваша подсказка (замок), и изображением, очищенным от шума, чтобы оно выглядело как ваша отрицательная подсказка (зернистость, туман), и попытается сдвинуть окончательные результаты к прежнему. и от последнего.

### Примеры:

```
a colorful photo of a castle in the middle of a forest with trees and (((bushes))), by Ismail Inceoglu, ((((shadows)))), ((((high contrast)))), dynamic shading, ((hdr)), detailed vegetation, digital painting, digital drawing, detailed painting, a detailed digital painting, gothic art, featured on deviantart
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 749109862, Size: 896x448, Model hash: 7460a6fa
```

| отрицательная подсказка | изображение |
|---------------------|------------- -------------------------------------------------- -------------------------------------------------------------|
| нет | ![01069-749109862](https://user-images.githubusercontent.com/20920490/192156368-18360487-0dcf-4b7d-b57e-b3fa80a81f1a.png) |
| туман | ![01070-749109862](https://user-images.githubusercontent.com/20920490/192156405-9c43ba8c-4eb8-415d-9f4d-902c8cf69b6d.png) |
| зернистый | ![01071-749109862](https://user-images.githubusercontent.com/20920490/192156421-17e53296-df5c-4e82-bf9a-f1ca562d3ad0.png) |
| туман, зернистый | ![01072-749109862](https://user-images.githubusercontent.com/20920490/192156430-3d05e5c4-2b86-409c-a357-a31178e0cb30.png) |
| туман, зернистый, фиолетовый | ![01073-749109862](https://user-images.githubusercontent.com/20920490/192156440-ec59abe8-1a18-4372-a100-0da8bc1f8d13.png) |
