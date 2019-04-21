import zipfile
import tkinter
from tkinter import filedialog
import tkinter.messagebox
from pathlib import Path

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
            tkinter.messagebox.showinfo("success!", "finish zip " + str(i) + "!")
    except:
        tkinter.messagebox.showwarning("wrong!", "wrong zip!")


def choose_file():
    path_ = filedialog.askopenfilename(filetypes=[("zip files", "*.zip")])
    path.set(path_)


def zip_main():
    top = tkinter.Tk()
    global path, file_choose_1
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

if __name__=="__main__":
    zip_main()