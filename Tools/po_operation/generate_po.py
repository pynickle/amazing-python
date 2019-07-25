'''
@Description: generate po file of po parser
@Author: pynickle
@LastEditors: pynickle
'''
import os
import string
import re


def origin(a):
    origin_str = ["=", "-", "~", "#"]

    if not a:
        return False

    for i in a:
        if i not in origin_str:
            return False
    return True

def generate(file_name, path):
    is_code = False
    is_code_first = False
    join = []

    if os.path.isfile(file_name):
        os.remove(file_name)
    f = open(file_name, "a", encoding="utf-8")
    f.close()


    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".rst"):
                with open(root + "/" + file, "r", encoding="utf-8") as f:
                    content = f.read()
                    sentences = content.split("\n")
                    for index, value in enumerate(sentences):
                        exper = value.strip()
                        if origin(exper):
                            continue

                        if is_code:
                            if is_code_first:
                                is_code_first = False
                                continue
                            if not value.startswith("    "):
                                if not sentences[index+1].startswith("    ") and not sentences[index+2].startswith("    "):
                                    is_code = False
                                    continue
                                else:
                                    pass
                            if exper.startswith("#"):
                                pass
                            else:
                                continue

                        if re.match(".. code:: (.*?)", exper) or re.match("..code-block:: (.*?)", exper):
                            is_code = True
                            is_code_first = True
                            continue

                        """
                        if re.match(".. _this link: (.*?)", exper):
                            continue
                        """

                        if exper:
                            value = value.replace(r'"', r'\"')
                            if value in join:
                                continue
                            model = ""
                            model += '#: ' + \
                                root + "/" + file + \
                                ':' + str(index + 1) + '\n'
                            model += 'msgid "' + value + '"\n'
                            model += 'msgstr ""\n'
                            with open(file_name, "a", encoding="utf-8") as f2:
                                f2.write(model)
                            join.append(value)
                        else:
                            continue

def main():
    print("Welcome to rst po generator!")
    file_name = input("enter the final file name: ")
    path = input("enter the docs path: ")
    generate(file_name, path)

if __name__ == "__main__":
    main()
