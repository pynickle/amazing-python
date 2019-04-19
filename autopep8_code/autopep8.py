import os
from subprocess import call
import tkinter
from tkinter.filedialog import askdirectory
import tkinter.messagebox


def selectPath():
    path_ = askdirectory()
    path.set(path_)


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


def main():
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
    success.set("success:")
    top.mainloop()


if __name__ == "__main__":
    main()
