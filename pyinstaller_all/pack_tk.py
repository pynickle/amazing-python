import os
import shutil
from subprocess import call
import tkinter
from tkinter.filedialog import askdirectory
import tkinter.messagebox


def selectPath():
    path_ = askdirectory()
    path.set(path_)


def exe(root, dirs, files, successful_files):
    for file in files:
        if file.endswith(".py"):
            try:
                get_file = "now update : " + file
                print("\033[33m" + get_file.center(50, '='))
                root.replace("\\", "/")
                call("cd " + root + "&pyinstaller -F " + file, shell=True)
                shutil.rmtree(root + "/build")
                shutil.rmtree(root + "/__pycache__")
                shutil.copyfile(
                    root + "/dist/" + file[0: len(file) - 3] + ".exe",
                    root + "/" + file[0: len(file) - 3] + ".exe",
                )
                shutil.rmtree(root + "/dist")
                os.remove(root + "/" + file[0: len(file) - 3] + ".spec")
                success_files += 1
                success.set("success:" + str(success_files))
                top.update()
            except Exception as e:
                print(e)
                continue


def py_to_exe():
    success_files = 0
    file_path = path.get()
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                exe(root, dirs, files, success_files)
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("wrong!", "path wrong!")
    else:
        tkinter.messagebox.showerror("wrong!", "path wrong!")
    get_success = "pack success : " + str(success_files)
    print(get_success.center(50, '-'))


def remove(root, dirs, files, successful_files):
    for file in files:
        if file.endswith(".exe"):
            try:
                os.remove(root + "/" + file)
                success_files += 1
                success.set("success:" + str(success_files))
                top.update()
            except:
                continue


def remove_exe():
    success_files = 0
    file_path = path.get()
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                remove(root, dirs, files, success_files)
        except:
            tkinter.messagebox.showerror("wrong!", "path wrong!")
    else:
        tkinter.messagebox.showerror("wrong!", "path wrong!")
    get_success = "remove exe success : " + str(success_files)
    print(get_success.center(50, '-'))


def pyinstaller_main():
    global path, success, top
    top = tkinter.Tk()
    path, success = tkinter.StringVar(), tkinter.StringVar()
    button_py = tkinter.Button(
        top, text="begin pyinstaller", command=py_to_exe).pack()
    button_exe = tkinter.Button(
        top, text="remove exe", command=remove_exe).pack()
    choose_path = tkinter.Button(
        top, text="choose path", command=selectPath).pack()
    path_show = tkinter.Entry(top, textvariable=path).pack()
    success_entry = tkinter.Entry(top, textvariable=success).pack()
    success.set("success:")
    top.mainloop()


if __name__ == "__main__":
    pyinstaller_main()
