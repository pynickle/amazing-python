import argparse
import os
from gooey import Gooey, GooeyParser


def rexe(file_path, file_type):
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    if file.endswith("." + file_type):
                        os.remove(root + "/" + file)
        except Exception as e:
            print("Errora: " + str(e))
    else:
        print("Error: Path Not Exists!")

@Gooey(program_name = "remove file")
def main():
    parser = GooeyParser()
    parser.add_argument("-p", "--path", help = "enter the file path you want to remove file", required=True, widget="DirChooser")
    parser.add_argument("-t", "--type", help = "enter the file type that you want to remove", required=True)
    args = parser.parse_args()
    file_path = args.path 
    file_type = args.type
    rexe(file_path, file_type)

if __name__ == "__main__":
    main()

