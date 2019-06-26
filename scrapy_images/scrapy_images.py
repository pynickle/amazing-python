from bs4 import BeautifulSoup
import requests
import tkinter
import tkinter.messagebox
import time
import os
import validators
from tkinter.filedialog import askdirectory


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
    except BaseException:
        tkinter.messagebox.showerror("wrong!", "can not get the url\n请求网址失败")
        return
    soup = BeautifulSoup(response.text, "lxml")
    img_list = soup.find_all("img")
    if img_list == []:
        tkinter.messagebox.showinfo("wrong!", "no images on the website\n在网站上未发现图片")
        return
    for img in img_list:
        img_url = img["src"]
        try:
            img_get = requests.get(img_url, timeout=20)
            name = int(time.time())
            f = open(path + "\\" + str(name) + choice.get(), "wb")
            f.write(img_get.content)
            f.close()
        except BaseException:
            try:
                img_url_retry = "https:" + img_url
                img_get = requests.get(img_url_retry, timeout=20)
                name = int(time.time())
                f = open(path + "\\" + str(name) + choice.get(), "wb")
                f.write(img_get.content)
                f.close()
            except BaseException:
                continue
    tkinter.messagebox.showinfo("success!", "successfully download images!")


def is_entry_right():
    if is_url(link_entry.get()) & os.path.exists(save_entry.get()):
        scrapy()
    else:
        tkinter.messagebox.showwarning("wrong!", "wrong url or path\n错误的地址或路径")


def scrapy_main():
    top = tkinter.Tk()

    global path, link_entry, save_entry

    path = tkinter.StringVar()

    top.title("scrapy img")
    top.geometry("300x210+25+25")

    version = tkinter.Label(top, text="version:1.0")
    version.pack()

    choice = tkinter.StringVar()
    choice.set(".png")

    button = tkinter.Button(top, text="start scrapy images", command=is_entry_right)
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

    choose_jpg = tkinter.Radiobutton(top, text=".jpg", variable=choice, value=".jpg")
    choose_jpg.place(x=25, y=180)
    choose_png = tkinter.Radiobutton(top, text=".png", variable=choice, value=".png")
    choose_png.place(x=125, y=180)
    choose_png = tkinter.Radiobutton(top, text=".gif", variable=choice, value=".gif")
    choose_png.place(x=225, y=180)

    top.mainloop()


if __name__ == "__main__":
    scrapy_main()
