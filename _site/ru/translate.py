# Thing that generates machine-translated files for translations.
# Doesn't translate most of header stuff and code.
# TODO: turn this sucker into a proper gem.

from deep_translator import GoogleTranslator
import sys
import os
import re
import time

target_language = sys.argv[1]

# For file in en folder
#     Check if it exists already
#     If it doesn't, make one
#     Translate function

def translate(fle):
    result = ''
    header_open = False
    code_open = False
    for line in fle.readlines():
        print(f"   {line}")
        if line[0:3] == '---':
            header_open = not header_open
            result += line
            continue
        if line[0:3] == '```':
            code_open = not code_open
            result += line
            continue
        if ((not header_open) and (not code_open)):
            translated = GoogleTranslator(source='auto', target=target_language).translate(line)
            if translated == None:
                translated = line
            result = result + translated + "\n"
            time.sleep(0.2)
        else:
            result += line
    title = re.findall("(?<=title: ).*", result)[0]
    result = re.sub("(?<=title: ).*", GoogleTranslator(source='auto', target=target_language).translate(title), result)
    result = re.sub("(?<=lang: ).*", target_language, result)
    result = re.sub("(?<=lang: ).*", target_language, result)
    result = re.sub("(?=lang: )", "machine_translated: true\n", result)
    return result


target_dir = f"_pages/{target_language}"
for file in os.listdir('_pages/en'):
     filename = os.fsdecode(file)
     target_path = f"{target_dir}/{filename}"
     if os.path.exists(target_path):
         print(f"{target_path} exists, skipping to next file...")
         continue
     else:
         print(f"Translating {target_path}...")
         f = open(f"_pages/en/{filename}")
         n = open(target_path, "x")
         n.write(translate(f))
         n.close()

# f = open('_pages/en/UI_defaults.md')
#
