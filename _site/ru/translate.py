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
    do_not_translate = ['<img', 'details>', 'summary>', '----', '.png]', '.jpg]', '{% raw %}', '{% endraw %}']
    header_open = False
    code_open = False
    for line in fle.readlines():
        print(f"   {line}")
        if line[0:3] == '---' and not line[0:4] == '----':
            header_open = not header_open
            result += line
            continue
        if line[0:3] == '```':
            code_open = not code_open
            result += line
            continue
        if any(word in line for word in do_not_translate):
            result += line + "\n"
            continue
        if ((not header_open) and (not code_open)):
            translated = GoogleTranslator(source='auto', target=target_language).translate(line)
            if translated == None:
                translated = line
            result = result + translated + "\n"
            time.sleep(0.05)
        else:
            result += line
    title = re.findall("(?<=title: ).*", result)[0]
    result = re.sub("(?<=title: ).*", GoogleTranslator(source='auto', target=target_language).translate(title), result)
    result = re.sub("(?<=lang: ).*", target_language, result)
    result = re.sub("(?<=lang: ).*", target_language, result)
    result = re.sub("\] \(", '](', result) # link fix
    result = re.sub("(?=lang: )", "machine_translated: true\n", result)
    return result


target_dir = f"_pages/{target_language}"
for file in os.listdir('_pages/en'):
     filename = os.fsdecode(file)
     target_path = f"{target_dir}/{filename}"
     if os.path.exists(target_path):
         f = open(target_path)
         content = f.read()
         if len(content) > 4 and not 'machine_translated: true' in content:
             print(f"{target_path} exists, skipping to next file...")
             f.close()
             continue
         f.close()
     else:
         print(f"Translating {target_path}...")
         f = open(f"_pages/en/{filename}")
         n = open(target_path, "x")
         n.write(translate(f))
         n.close()
