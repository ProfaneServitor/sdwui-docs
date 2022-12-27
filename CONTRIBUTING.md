To contribute to github's repositories, you need git.

https://git-scm.com/

After that, fork repository and clone it locally for editing.

```bash
git clone https://github.com/<your_github_username>/sdwui-docs
```

# Improving existing translations

All translatable files lie in `_pages/<language code>`. Just open that folder and edit those files. Don't forget to change the title and remove `machine_translated` line.

# Adding translations

Open `_config.yml` and add your language code to this line:

```yaml
languages: ["en", "ru", ...]
```

## Machine-generated translations

`translate.py` is a script which can populate site with machine-generated translations. To install its prerequisites, run:

```bash
pip install deep_translator
```

To translate:

```bash
python translate.py <language_code>
```
