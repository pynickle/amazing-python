import argparse
import os
from gooey import Gooey, GooeyParser


@Gooey(program_name="copyright")
def copyright_main():
    parser = GooeyParser(
        description = "automatically set the copyright for you"
    )
    parser.add_argument("-p", "--path", required=True, widget="DirChooser",
        help = "choose the path you want to add the copyright")
    parser.add_argument("-t", "--title", required=True,
        help = "add the copyright title")
    parser.add_argument("-l", "--license", required=True,
        help = "add the license name for the copyright")
    parser.add_argument("-y", "--year", required=True,
        help = "add the year the production was made")
    parser.add_argument("-o", "--owner", required=True,
        help = "add the owner of the production")
    parser.add_argument("-d", "--description",
        help = "add description of the program")
    parser.add_argument("-c", "--cversion",
        help = "add the version of the production")
    parser.add_argument("-u", "--update",
        help = "add the latest time that you updated")
    parser.add_argument("-f", "--file",
        help = "add the file name of the program")
    args = parser.parse_args()
    data = '"""'
    data += "Copyright: Copyright (c) " + args.year + "\n"
    data += "License : " + args.license + "\n"
    data += "owner : " + args.owner + "\n"
    data += "title : " + args.title + "\n"
    if args.description:
        data += "description : " + args.description + "\n"
    if args.cversion:
        data += "version : " + args.cversion + "\n"
    if args.update:
        data += "time : " + args.update + "\n"
    if args.file:
        data += "file : " + args.file + "\n"
    data += '"""\n\n'

    for root, dirs, files in os.walk(args.path):
        for file in files:
            with open(root + "/" + file, "r+", encoding="utf-8") as f:
                old = f.read()
                f.seek(0)
                f.write(data)
                f.write(old)

if __name__ == "__main__":
    copyright_main()