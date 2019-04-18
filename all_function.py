import colorama
from termcolor import colored, cprint
from pathlib import Path
from tkinter import filedialog
import zipfile
import sys
import execjs
import json
from tkinter.filedialog import askdirectory
import validators
import time
import tkinter.messagebox
import tkinter
import requests
from bs4 import BeautifulSoup
from pip._internal.utils.misc import get_installed_distributions
import pip
import re
import os
from subprocess import call


def black_main():
    success = 0
    file_path = input("path:")
    try:
        for root, dirs, files in os.walk(file_path):
            for file in files:
                if file.endswith(".py"):
                    try:
                        call("black " + root + "/" + file, shell=True)
                        success += 1
                    except:
                        continue
    except:
        print("path wrong!")
    print("success:" + str(success))


def analyze_code(codefile_source):
    total_line = 0
    comment_line = 0
    blank_line = 0
    with open(codefile_source, encoding="gb18030", errors="ignore") as f:
        lines = f.readlines()
        total_line = len(lines)
        line_index = 0
        while line_index < total_line:
            line = lines[line_index]
            if line.startswith("#"):
                comment_line += 1
            elif re.match("\s*'''", line) is not None:
                comment_line += 1
                while re.match(".*'''$", line) is None:
                    try:
                        line = lines[line_index]
                        comment_line += 1
                        line_index += 1
                    except:
                        continue
            elif line == "\n":
                blank_line += 1
            line_index += 1
    print("在%s中:" % codefile_source)
    if total_line != 0:
        print("代码行数：", total_line)
        print("注释行数:", comment_line, "占%0.2f%%" %
              (comment_line * 100 / total_line))
        print("空行数:", blank_line, "占%0.2f%%" %
              (blank_line * 100 / total_line), "\n")
    else:
        print("代码行数：", total_line)
    return [total_line, comment_line, blank_line]


def run(file_path):
    os.chdir(file_path)
    total_lines = 0
    total_comment_lines = 0
    total_blank_lines = 0
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith(".py"):
                line = analyze_code(root + "/" + file)
                total_lines, total_comment_lines, total_blank_lines = (
                    total_lines + line[0],
                    total_comment_lines + line[1],
                    total_blank_lines + line[2],
                )
    if total_lines != 0:
        print("总代码行数:", total_lines)
        print(
            "总注释行数:",
            total_comment_lines,
            "占%0.2f%%" % (total_comment_lines * 100 / total_lines),
        )
        print(
            "总空行数:",
            total_blank_lines,
            "占%0.2f%%" % (total_blank_lines * 100 / total_lines) + "\n",
        )
    else:
        print("总代码行数:", total_lines)


def code_main():
    FILE_PATH = input("file path:")
    print("\n")
    run(FILE_PATH)
    os.system("pause")


def pip_main():
    update_now = 1
    package_number = len(get_installed_distributions())
    for dist in get_installed_distributions():
        try:
            call("pip install --upgrade " + dist.project_name, shell=True)
            print("all package:{},update now:{}".format(
                package_number, update_now))
            update_now += 1
        except:
            continuer
    print("all is finished:{}".format(s))


def selectPath():
    path_ = askdirectory()
    path.set(path_)


def is_url(url):
    if validators.url(url) == True:
        return True
    else:
        return False


def scrapy():
    url = link_entry.get()
    path = save_entry.get()
    try:
        response = requests.get(url, timeout=20)
    except:
        tkinter.messagebox.showerror("wrong!", "can not get the url\n请求网址失败")
        return
    soup = BeautifulSoup(response.text, "lxml")
    img_list = soup.find_all("img")
    if img_list == []:
        tkinter.messagebox.showinfo(
            "wrong!", "no images on the website\n在网站上未发现图片")
        return
    for img in img_list:
        img_url = img["src"]
        try:
            img_get = requests.get(img_url, timeout=20)
            name = int(time.time())
            f = open(path + "\\" + str(name) + choice.get(), "wb")
            f.write(img_get.content)
            f.close()
        except:
            try:
                img_url_retry = "https:" + img_url
                img_get = requests.get(img_url_retry, timeout=20)
                name = int(time.time())
                f = open(path + "\\" + str(name) + choice.get(), "wb")
                f.write(img_get.content)
                f.close()
            except:
                continue
    tkinter.messagebox.showinfo("success!", "successfully download images!")


def is_entry_right():
    if is_url(link_entry.get()) & os.path.exists(save_entry.get()):
        scrapy()
    else:
        tkinter.messagebox.showwarning("wrong!", "wrong url or path\n错误的地址或路径")


def scrapy_main():
    top = tkinter.Tk()

    path = tkinter.StringVar()

    top.title("scrapy img")
    top.geometry("300x210+25+25")

    version = tkinter.Label(top, text="version:1.0")
    version.pack()

    choice = tkinter.StringVar()
    choice.set(".png")

    button = tkinter.Button(
        top, text="start scrapy images", command=is_entry_right)
    button.pack()

    link_add = tkinter.Label(top, text="scrapy url:")
    link_add.pack()

    link_entry = tkinter.Entry(top, width=50)
    link_entry.pack()

    save_add = tkinter.Label(top, text="save path:")
    save_add.pack()

    save_entry = tkinter.Entry(top, width=50, textvariable=path)
    save_entry.place(x=0, y=120)

    path_choose = tkinter.Button(top, text="choose path", command=selectPath)
    path_choose.place(x=110, y=145)

    choose_jpg = tkinter.Radiobutton(
        top, text=".jpg", variable=choice, value=".jpg")
    choose_jpg.place(x=25, y=180)
    choose_png = tkinter.Radiobutton(
        top, text=".png", variable=choice, value=".png")
    choose_png.place(x=125, y=180)
    choose_png = tkinter.Radiobutton(
        top, text=".gif", variable=choice, value=".gif")
    choose_png.place(x=225, y=180)

    top.mainloop()


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}


def get_translate_youdao(word):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    Form_data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1512399450582",
        "sign": "78181ebbdcb38de9b4a3f4cd1d38816b",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
        "typoResult": "false",
    }
    try:
        response = requests.post(url, data=Form_data)
        content = json.loads(response.text)
        result = content["translateResult"][0][0]["tgt"]
        return result
    except:
        return "wrong!"


def get_translate_baidu(word):
    url = "https://fanyi.baidu.com/sug"
    Form_data = {"kw": word}
    try:
        response = requests.post(url, data=Form_data, headers=headers)
        content = json.loads(response.text)
        result = content["data"][0]["v"]
        return result
    except:
        try:
            soup = BeautifulSoup(r.text, "lxml")
            correct = soup.find_all("a", class_="correct-link correct-query")
            Form_data = {"kw": correct[0]}
            response = requests.post(url, data=Form_data, headers=headers)
            content = json.loads(response.text)
            result = content["data"][0]["v"]
        except:
            return "wrong!"


class Py4Js:
    def __init__(self):
        self.ctx = execjs.compile(
            """ 
            function TL(a) { 
                var k = ""; 
                var b = 406644; 
                var b1 = 3293161072;       
                var jd = "."; 
                var $b = "+-a^+6"; 
                var Zb = "+-3^+b+-f";    
                for (var e = [], f = 0, g = 0; g < a.length; g++) { 
                    var m = a.charCodeAt(g); 
                    128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
                    e[f++] = m >> 18 | 240, 
                    e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
                    e[f++] = m >> 6 & 63 | 128), 
                    e[f++] = m & 63 | 128) 
                } 
                a = b; 
                for (f = 0; f < e.length; f++) a += e[f], 
                a = RL(a, $b); 
                a = RL(a, Zb); 
                a ^= b1 || 0; 
                0 > a && (a = (a & 2147483647) + 2147483648); 
                a %= 1E6; 
                return a.toString() + jd + (a ^ b) 
            };      
            function RL(a, b) { 
                var t = "a"; 
                var Yb = "+"; 
                for (var c = 0; c < b.length - 2; c += 3) { 
                    var d = b.charAt(c + 2), 
                    d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
                    d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
                    a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
                } 
                return a 
            } 
        """
        )

    def getTk(self, text):
        return self.ctx.call("TL", text)


def buildUrl(text, tk):
    baseUrl = "https://translate.google.cn/translate_a/single"
    baseUrl += "?client=t&"
    baseUrl += "s1=auto&"
    baseUrl += "t1=zh-CN&"
    baseUrl += "h1=zh-CN&"
    baseUrl += "dt=at&"
    baseUrl += "dt=bd&"
    baseUrl += "dt=ex&"
    baseUrl += "dt=ld&"
    baseUrl += "dt=md&"
    baseUrl += "dt=qca&"
    baseUrl += "dt=rw&"
    baseUrl += "dt=rm&"
    baseUrl += "dt=ss&"
    baseUrl += "dt=t&"
    baseUrl += "ie=UTF-8&"
    baseUrl += "oe=UTF-8&"
    baseUrl += "otf=1&"
    baseUrl += "pc=1&"
    baseUrl += "ssel=0&"
    baseUrl += "tsel=0&"
    baseUrl += "kc=2&"
    baseUrl += "tk=" + str(tk) + "&"
    baseUrl += "q=" + text
    return baseUrl


def get_translate_google(text):
    js = Py4Js()
    header = {
        "authority": "translate.google.cn",
        "method": "GET",
        "path": "",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": "",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        "x-client-data": "CIa2yQEIpbbJAQjBtskBCPqcygEIqZ3KAQioo8oBGJGjygE=",
    }
    url = buildUrl(text, js.getTk(text))
    res = ""
    try:
        r = requests.get(url)
        result = json.loads(r.text)
        if result[7] != None:
            try:
                correctText = (
                    result[7][0].replace("<b><i>", " ").replace("</i></b>", "")
                )
                correctUrl = buildUrl(correctText, js.getTk(correctText))
                correctR = requests.get(correctUrl)
                newResult = json.loads(correctR.text)
                res = newResult[0][0][0]
            except Exception as e:
                res = result[0][0][0]
        else:
            res = result[0][0][0]
    except:
        return "wrong!"
    finally:
        return res


def translate_main():
    while True:
        print("翻译内容（q退出）：")
        translate_text = input()
        js = Py4Js()
        if translate_text == "q":
            sys.exit()

        youdao = get_translate_youdao(translate_text)
        baidu = get_translate_baidu(translate_text)
        google = get_translate_google(translate_text)

        print("有道翻译结果：", youdao)
        print("百度翻译结果：", baidu)
        print("谷歌翻译结果：", google, "\n")


def un_zip(file_name):
    i = 0
    try:
        path_use = file_choose_1.get()
        with zipfile.ZipFile(path_use, "r") as f:
            for fn in f.namelist():
                i += 1
                extracted_path = Path(f.extract(fn))
                try:
                    extracted_path.rename(fn.encode("cp437").decode("gbk"))
                except:
                    tkinter.messagebox.showwarning("wrong!", "wrong zip!")
            tkinter.messagebox.showinfo(
                "success!", "finish zip " + str(i) + "!")
    except:
        tkinter.messagebox.showwarning("wrong!", "wrong zip!")


def choose_file():
    path_ = filedialog.askopenfilename(filetypes=[("zip files", "*.zip")])
    path.set(path_)


def zip_main():
    top = tkinter.Tk()
    path = tkinter.StringVar()
    button_begin = tkinter.Button(
        top, text="begin", command=lambda: un_zip(file_name=path)
    )
    button_begin.pack()
    button = tkinter.Button(top, text="choose zip file", command=choose_file)
    button.pack()
    file_choose_1 = tkinter.Entry(top, textvariable=path, width=50)
    file_choose_1.pack()
    top.mainloop()


def autopep8():
    success_files = 0
    file_path = path.get()
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    if file.endswith(".py"):
                        try:
                            call("autopep8 --in-place " +
                                 root + "/" + file, shell=True)
                            success_files += 1
                            success.set('success:'+str(success_files))
                        except:
                            continue
        except:
            tkinter.messagebox.showerror("wrong!", "path wrong!")
    else:
        tkinter.messagebox.showerror("wrong!", "path wrong!")


def autopep8_main():
    global path, success
    top = tkinter.Tk()
    path = tkinter.StringVar()
    success = tkinter.StringVar()
    button = tkinter.Button(top, text="begin autopep8", command=autopep8)
    button.pack()
    choose_path = tkinter.Button(top, text="choose path", command=selectPath)
    choose_path.pack()
    path_show = tkinter.Entry(top, textvariable=path)
    path_show.pack()
    success_entry = tkinter.Entry(top, textvariable=success)
    success_entry.pack()
    top.mainloop()


def black():
    success_files = 0
    file_path = path.get()
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    if file.endswith(".py"):
                        try:
                            call("black " + root + "/" + file, shell=True)
                            success_files += 1
                            success.set('success:'+str(success_files))
                        except:
                            continue
        except:
            tkinter.messagebox.showerror("wrong!", "path wrong!")
    else:
        tkinter.messagebox.showerror("wrong!", "path wrong!")


def black_main():
    global path, success
    top = tkinter.Tk()
    path = tkinter.StringVar()
    success = tkinter.StringVar()
    button = tkinter.Button(top, text="begin black", command=black)
    button.pack()
    choose_path = tkinter.Button(top, text="choose path", command=selectPath)
    choose_path.pack()
    path_show = tkinter.Entry(top, textvariable=path)
    path_show.pack()
    success_entry = tkinter.Entry(top, textvariable=success)
    success_entry.pack()
    top.mainloop()


colorama.init()


def main():
    print('\n')
    print('all function'.center(50))
    cprint("please choose:", "red")
    print("1.use black to beautify your code")
    print("2.count how many python code have you written")
    print("3.use pip to update your library automatically")
    print("4.scrapy images you like on any website")
    print("5.translate word with various website")
    print("6.unzip the zip files you want")
    print('7.use autopep8 to beautify your code')
    choose_function = input()
    if choose_function == "1":
        black_main()
    elif choose_function == "2":
        code_main()
    elif choose_function == "3":
        pip_main()
    elif choose_function == "4":
        scrapy_main()
    elif choose_function == "5":
        translate_main()
    elif choose_function == "6":
        zip_main()
    elif choose_function == "7":
        autopep8_main()
    else:
        print("wrong input!")


main()
