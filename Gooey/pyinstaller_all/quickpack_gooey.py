# -*- coding:UTF-8 -*-

from __future__ import print_function, unicode_literals
import os
import shutil
import argparse
from subprocess import call
import colorama
from gooey import Gooey, GooeyParser


colorama.init(autoreset=True)

def exe(file, root, success_files):
    for file in files:
        if file.endswith(".py"):
            try:
                get_file = "now update : " + file
                print("\033[33m" + get_file.center(50, '='))
                root.replace("\\", "/")
                call("cd " + root + "&pyinstaller -F " +
                    file, shell=True)
                shutil.rmtree(root + "/build")
                shutil.rmtree(root + "/__pycache__")
                shutil.copyfile(
                    root + "/dist/" +
                    file[0: len(file) - 3] + ".exe",
                    root + "/" + file[0: len(file) - 3] + ".exe",
                )
                shutil.rmtree(root + "/dist")
                os.remove(
                    root + "/" + file[0: len(file) - 3] + ".spec")
                success_files += 1
            except Exception as e:
                print(e)
                continue
    return success_files

def py_to_exe(file_path):
    success_files = 0
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                success_files = exe(file, root, success_files)
        except Exception:
            print("\033[31mwrong when walking path!")
    else:
        print("\033[31mpath not exist!")
    get_success = "pack success : " + str(success_files)
    print(get_success.center(50, '-'))

def rexe(files, success_files):
    for file in files:
        if file.endswith(".exe"):
            try:
                os.remove(root + "/" + file)
                success_files += 1
            except BaseException:
                continue
    return success_files

def remove_exe(file_path):
    success_files = 0
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                success_files = rexe(files, success_files)
        except BaseException:
            print("\033[31mwrong when walking path!")
    else:
        print("\033[31mpath not exist!")
    get_success = "remove exe success : " + str(success_files)
    print(get_success.center(50, '-'))

@Gooey(program_name="quickpack")
def pyinstaller_main():
    parser = GooeyParser(
        description="pack your python file")
    parser.add_argument('-p', '--path', required=True,
                        help="Enter the file path you want to pack", widget="DirChooser")
    parser.add_argument(
        '-r',
        '--remove',
        action="store_true",
        help="remove all exe under the path")
    parser.add_argument(
        "-e",
        "--exe",
        action="store_true",
        help="pack py file to exe by pyinstaller")
    args = parser.parse_args()
    file_path = args.path
    remove = args.remove
    exe = args.exe
    if remove:
        remove_exe(file_path)
    if exe:
        py_to_exe(file_path)


if __name__ == "__main__":
    pyinstaller_main()
