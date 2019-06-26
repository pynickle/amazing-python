import os
from subprocess import call
import sys

from gooey import Gooey, GooeyParser
from traceback import print_exc


file_num = 0


def PathNotExistsError(Exception):
    pass


def calSize(path):
    global file_num
    for filename in os.listdir(path):
        newpath = os.path.join(path, filename)
        if os.path.isdir(newpath):
            calSize(newpath)
        elif newpath.endswith(".py"):
            file_num += 1
    return str(file_num)


def beautify_file(root, files, file_type, para, success_files, file_num):
    try:
        para = para.replace("{{root}}", root)
    except Exception:
        pass
    if "{{file}}" in para:
        for file in files:
            if file.endswith(file_type):
                try:
                    para = para.replace("{{file}}", file)
                    call(para)
                    success_files += 1
                    print("success : " + str(file_num) +
                          "/" + str(success_files))
                except Exception as e:
                    print_exc()
                    continue
    else:
        call(para)
    return success_files


def beautify(file_type, para, file_path):
    calSize(file_path)
    success_files = 0
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                success_files = beautify_file(
                    root, files, file_type, para, success_files, file_num
                )
        except Exception:
            print_exc()
    else:
        raise PathNotExistsError("Path not exists!", file_path)


@Gooey(
    progress_regex=r"success : (?P<all>\d+)/(?P<success>\d+)$",
    progress_expr="success/all*100",
)
def main():
    parser = GooeyParser(
        description="beautify your code with customized command or standard commands"
    )
    parser.add_argument(
        "-p",
        "--path",
        help="the path you want to execute the command",
        required=True,
        widget="DirChooser",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-a", "--autopep8", help="use autopep8 to beautify py", action="store_true"
    )
    group.add_argument(
        "-b", "--black", help="use black to beautify py", action="store_true"
    )
    group.add_argument(
        "-g", "--gofmt", help="use gofmt to beautify go", action="store_true"
    )
    group.add_argument("-c", "--customized", help="use customized command")
    args = parser.parse_args()
    path = args.path
    if args.autopep8:
        beautify(".py", "autopep8 --in-place {{root}}/{{file}}", path)
    elif args.black:
        beautify(".py", "black {{root}}/{{file}}", path)
    elif args.gofmt:
        beautify(".go", "gofmt -w {{root}}/{{file}}", path)
    elif args.customized:
        customized = args.customized
        try:
            beautify(customized.split(" ** ")
                     [0], customized.split(" ** ")[1], path)
        except Exception as e:
            print_exc()
            print("illegal customized command")
            sys.exit()
    else:
        print("unknown tools")
        sys.exit()


if __name__ == "__main__":
    main()
