import os
from subprocess import call
import tkinter
from tkinter.filedialog import askdirectory
import tkinter.messagebox


def selectPath():
    path_ = askdirectory()
    path.set(path_)


def beautify_file(root, files, file_type, para, success_files):
    para = para.replace("{{root}}", root)
    for file in files:
        if file.endswith(file_type):
            try:
                para = para.replace("{{file}}", file)
                call(para)
                success_files += 1
                success.set("success:" + str(success_files))
                top.update()
            except Exception as e:
                print(e)
                continue
    return success_files


def beautify(file_type, para):
    success_files = 0
    file_path = path.get()
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                success_files = beautify_file(
                    root, files, file_type, para, success_files)
        except Exception as e:
            print(e)
    else:
        tkinter.messagebox.showerror("wrong!", "path wrong!")


def main():
    global path, success, top

    top = tkinter.Tk()
    top.title("beautify py code")
    top.geometry("300x300")

    path = tkinter.StringVar()
    path.set("enter path or choose path by the button")
    success = tkinter.StringVar()
    success.set("success files will be shown here")
    para_cust = tkinter.StringVar()
    para_cust.set("enter customized para if you want")

    tkinter.Button(top, text="begin autopep8", command=lambda: beautify(
        ".py", "autopep8 --in-place {{root}}/{{file}}")).pack()
    tkinter.Button(top, text="begin black", command=lambda: beautify(
        ".py", "black {{root}}/{{file}}")).pack()
    tkinter.Button(top, text="begin gofmt", command=lambda: beautify(
        ".go", "gofmt -w {{root}}/{{file}}")).pack()

    tkinter.Button(top, text="for customized", command=lambda: beautify(
        para_cust.get().split(" ** ")[0], para_cust.get().split(" ** ")[1])).pack()

    tkinter.Button(
        top, text="choose path", command=selectPath).pack()

    tkinter.Entry(
        top, textvariable=para_cust, width=150).pack()
    tkinter.Entry(top, textvariable=path, width=150).pack()
    tkinter.Entry(top, textvariable=success, width=150).pack()

    tkinter.Label(
        top, text="see my github for \n how to use customized parameter").pack()

    top.mainloop()


if __name__ == "__main__":
    main()
