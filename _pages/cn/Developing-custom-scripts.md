---
title: 开发自定义脚本
layout: post
category: development
permalink: /developing-custom-scripts/
machine_translated: true
lang: cn
---
# 安装和使用自定义脚本
脚本类定义可以在 modules/scripts.py 中找到。要创建您自己的自定义脚本，请创建一个实现该类的 python 脚本并将其放入 `scripts` 文件夹，使用以下示例或文件夹中已有的其他脚本作为指南。

Script 类有四种主要方法，下面将通过一个旋转和/或翻转生成的图像的简单示例脚本进一步详细描述。

```python
import modules.scripts as scripts
import gradio as gr
import os

from modules import images
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state


class Script(scripts.Script):  

# The title of the script. This is what will be displayed in the dropdown menu.
    def title(self):

        return "Flip/Rotate Output"


# Determines when the script should be shown in the dropdown menu via the
# returned value. As an example:
# is_img2img is True if the current tab is img2img, and False if it is txt2img.
# Thus, return is_img2img to only show the script on the img2img tab.

    def show(self, is_img2img):

        return is_img2img

# How the script's is displayed in the UI. See https://gradio.app/docs/#components
# for the different UI components you can use and how to create them.
# Most UI components can return a value, such as a boolean for a checkbox.
# The returned values are passed to the run method as parameters.

    def ui(self, is_img2img):
        angle = gr.Slider(minimum=0.0, maximum=360.0, step=1, value=0,
        label="Angle")
        hflip = gr.Checkbox(False, label="Horizontal flip")
        vflip = gr.Checkbox(False, label="Vertical flip")
        overwrite = gr.Checkbox(False, label="Overwrite existing files")
        return [angle, hflip, vflip, overwrite]



# This is where the additional processing is implemented. The parameters include
# self, the model object "p" (a StableDiffusionProcessing class, see
# processing.py), and the parameters returned by the ui method.
# Custom functions can be defined here, and additional libraries can be imported
# to be used in processing. The return value should be a Processed object, which is
# what is returned by the process_images method.

    def run(self, p, angle, hflip, vflip, overwrite):

        # function which takes an image from the Processed object,
        # and the angle and two booleans indicating horizontal and
        # vertical flips from the UI, then returns the
        # image rotated and flipped accordingly
        def rotate_and_flip(im, angle, hflip, vflip):
            from PIL import Image
           
            raf = im
           
            if angle != 0:
                raf = raf.rotate(angle, expand=True)
            if hflip:
                raf = raf.transpose(Image.FLIP_LEFT_RIGHT)
            if vflip:
                raf = raf.transpose(Image.FLIP_TOP_BOTTOM)
            return raf



        # If overwrite is false, append the rotation information to the filename
        # using the "basename" parameter and save it in the same directory.
        # If overwrite is true, stop the model from saving its outputs and
        # save the rotated and flipped images instead.
        basename = ""
        if(not overwrite):
            if angle != 0:
                basename += "rotated_" + str(angle)
            if hflip:
                basename += "_hflip"
            if vflip:
                basename += "_vflip"
        else:
            p.do_not_save_samples = True


        proc = process_images(p)

        # rotate and flip each image in the processed images
        # use the save_images method from images.py to save
        # them.
        for i in range(len(proc.images)):

            proc.images[i] = rotate_and_flip(proc.images[i], angle, hflip, vflip)

            images.save_image(proc.images[i], p.outpath_samples, basename,
            proc.seed + i, proc.prompt, opts.samples_format, info= proc.info, p=p)

        return proc
```
