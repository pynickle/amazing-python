import os
from subprocess import call
import tkinter
from tkinter.filedialog import askdirectory
import tkinter.messagebox


def selectPath():
    path_ = askdirectory()
    path.set(path_)


def gofmt_file(roots, files, success_files):
    for file in files:
        if file.endswith(".go"):
            try:
                call("gofmt -w " + roots + "/" + file)
                success_files += 1
                success.set("success:" + str(success_files))
                top.update()
            except Exception as e:
                print(e)
                continue
    return success_files


def gofmt():
    success_files = 0
    file_path = path.get()
    if os.path.exists(file_path):
        try:
            for roots, dirs, files in os.walk(file_path):
                success_files = gofmt_file(roots, files, success_files)
        except Exception as e:
            print(e)
    else:
        tkinter.messagebox.showerror("wrong!", "path wrong!")


def autopep8_file(root, files, success_files):
    for file in files:
        if file.endswith(".py"):
            try:
                call("autopep8 --in-place " + root + "/" + file, shell=True)
                success_files += 1
                success.set("success:" + str(success_files))
                top.update()
            except Exception as e:
                print(e)
                continue
    return success_files


def autopep8():
    success_files = 0
    file_path = path.get()
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                success_files = autopep8_file(root, files, success_files)
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("wrong!", "path wrong!")
    else:
        tkinter.messagebox.showerror("wrong!", "path wrong!")


def black_file(root, files, success_files):
    for file in files:
        if file.endswith(".py"):
            try:
                call("black " + root + "/" + file, shell=True)
                success_files += 1
                success.set("success:" + str(success_files))
                top.update()
            except Exception as e:
                print(e)
                continue
    return success_files


def black():
    success_files = 0
    file_path = path.get()
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                success_files = black_file(root, files, success_files)
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("wrong!", "black wrong!")
    else:
        tkinter.messagebox.showerror("wrong!", "path wrong!")


def main():
    global path, success, top

    top = tkinter.Tk()
    top.title("beautify py code")
    top.geometry("200x200")

    path = tkinter.StringVar()
    success = tkinter.StringVar()
    success.set("success:")

    button1 = tkinter.Button(top, text="begin autopep8", command=autopep8).pack()
    button2 = tkinter.Button(top, text="begin black", command=black).pack()
    button3 = tkinter.Button(top, text="begin gofmt", command=gofmt).pack()

    choose_path = tkinter.Button(top, text="choose path", command=selectPath).pack()
    path_show = tkinter.Entry(top, textvariable=path, width=150).pack()
    success_entry = tkinter.Entry(top, textvariable=success, width=150).pack()

    top.mainloop()


if __name__ == "__main__":
    main()
