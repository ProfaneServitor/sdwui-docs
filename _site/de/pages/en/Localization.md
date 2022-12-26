# Using localization files
The intended way to do localizations now is via extensions. See:
https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Developing-extensions

# Creating localization files
Go to settings and click `Download localization template` button at the bottom. This will download a template for localization that you can edit.

# Updating old localization with new keys

[This repository](https://github.com/AUTOMATIC1111/stable-diffusion-webui-old-localizations) contrains old orphaned localizations. If you wish to update them with new keys, you can use the following script:

```python
import json
files=['localization_template.json', 'old_localization.json']

with open('new_localization.json', "w") as outfile:
    res = dict()
    for f in files:
        dct = dict(json.load(open(f, "r").read()))
        res.update(dct)
    outfile.write(res)
```

Then translate what was added.
