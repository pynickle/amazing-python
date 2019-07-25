'''
@Description: get po file of po parser
@Author: pynickle
@LastEditors: pynickle
'''
import os
import re

# ##############################
# NOTE find magid and msgstr
# ##############################

def get(file_name):
    global msgid_list
    global msgstr_list

    with open(file_name, "r", encoding="utf-8") as f:
        contents = f.readlines()
        all_content = "".join(contents)

    msgid_list = []
    msgstr_list = []

    files = re.findall(r"#: (.*):(.*)", all_content)


    msgid_pattern = re.compile(r"msgid")
    msgstr_pattern = re.compile(r"msgstr")
    content_pattern = re.compile(r'"(.*)"')

    msgid_temporary = ""
    msgstr_temporary = ""

    is_first = True
    for line in contents:
        if line and msgid_pattern.match(line):
            current_tag = "msgid"
            if not is_first:
                msgstr_list.append(msgstr_temporary)
            else:
                is_first = False
            msgstr_temporary = ""

        if line and msgstr_pattern.match(line):
            current_tag = "msgstr"
            msgid_list.append(msgid_temporary)
            msgid_temporary = ""

        for content in content_pattern.findall(line):

            if current_tag == "msgid":
                msgid_temporary += content

            if current_tag == "msgstr":
                msgstr_temporary += content

    msgstr_list.append(msgstr_temporary)

# ##############################
# NOTE deal with backslash
# ##############################

def backslash():
    global msgid_list
    global msgstr_lost

    msgstr_temp = msgstr_list
    msgstr_temp2 = ""
    double = False

    for index, value in enumerate(msgstr_list):
        with open("temp.txt", "w", encoding="utf-8") as f:
            print(value, file=f)
        with open("temp.txt", "r", encoding="utf-8") as f:
            value = f.read().replace("\\\\", "\\").replace("\\", "")

        msgstr_temp[index] = value
        msgstr_temp2 = ""

    msgstr_list = msgstr_temp
    msgstr_temp = ""

    msgid_temp = msgid_list
    msgid_temp2 = ""
    double = False

    for index, value in enumerate(msgid_list):
        with open("temp.txt", "w", encoding="utf-8") as f:
            print(value, file=f)
        with open("temp.txt", "r", encoding="utf-8") as f:
            value = f.read().replace("\\\\", "\\").replace("\\", "")

        msgid_temp[index] = value
        msgid_temp2 = ""

    msgid_list = msgid_temp
    msgid_temp = ""
    if os.path.isfile("temp.txt"):
        os.remove("temp.txt")

# ##############################
# NOTE write in turn
# ##############################
"""
for i, j, k in zip(msgid_list, msgstr_list, files):
    if j:
        with open("tutorial_res/" + k[0], "r", encoding="utf-8") as f:
            temp = f.readlines()

        temp2 = []
        index = 0

        for value in temp:
            index += 1
            if index == int(k[1]):
                value = j + "\n"
            temp2.append(value)

        temp = temp2
        with open("tutorial_res/" + k[0], "w", encoding="utf-8") as f:
            f.writelines(temp)
    else:
        continue
"""
# ##############################
# NOTE read, find and write
# ##############################

def write(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            with open(root + "/" + file, "r", encoding="utf-8") as f:
                contents = f.readlines()

            temp = []
            index = 0

            for i in contents:
                index += 1
                if i in msgid_list:
                    change = msgstr_list[msgid_list.index(i)]
                    if change.strip():
                        i = change
                temp.append(i)
    
            contents = temp
            temp = []
            with open(root + "/" + file, "w", encoding="utf-8") as f:
                f.writelines(contents)

def main():
    print("welcome to po getter!")
    file_name = input("enter the po file name: ")
    path = input("enter the origin file path: ")
    get(file_name)
    backslash()
    write(path)

if __name__ == "__main__":
    main()
