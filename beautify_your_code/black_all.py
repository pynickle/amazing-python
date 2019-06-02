import os
from subprocess import call
import tkinter
from tkinter.filedialog import askdirectory
import tkinter.messagebox


def selectPath():
    path_ = askdirectory()
    path.set(path_)

def black_file(root,dir,files,success_files):
    for file in files:
        if file.endswith(".py"):
            try:
                call("black " + root + "/" + file, shell=True)
                success_files += 1
                success.set("success:" + str(success_files))
            except:
                continue
    
def black():
    success_files = 0
    file_path = path.get()
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                black_file(root,dir,files,successful_files)
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


if __name__ == "__main__":
    black_main()
