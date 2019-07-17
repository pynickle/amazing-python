import argparse
import os

def rexe(file_path, file_type):
    if os.path.exists(file_path):
        try:
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    if file.endswith("." + file_type):
                        os.remove(file)
        except Exception as e:
            print("Errora: " + e)
    else:
        print("Error: Path Not Exists!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help = "enter the file path you want to remove file", required=True)
    parser.add_argument("-t", "--type", help = "enter the file type that you want to remove")
    args = parser.parse_args()
    file_path = args.path 
    file_type = args.type
    rexe(file_path, file_type)

if __name__ == "__main__":
    main()

