import os
import re


def analyze_code(codefile_source):
    total_line = 0
    comment_line = 0
    blank_line = 0
    with open(codefile_source, encoding="gb18030", errors="ignore") as f:
        lines = f.readlines()
        total_line = len(lines)
        line_index = 0
        while line_index < total_line:
            line = lines[line_index]
            if line.startswith("#"):
                comment_line += 1
            elif re.match("\s*'''", line) is not None:
                comment_line += 1
                while re.match(".*'''$", line) is None:
                    try:
                        line = lines[line_index]
                        comment_line += 1
                        line_index += 1
                    except:
                        continue
            elif line == "\n":
                blank_line += 1
            line_index += 1
    print("在%s中:" % codefile_source)
    if total_line != 0:
        print("代码行数：", total_line)
        print("注释行数:", comment_line, "占%0.2f%%" % (comment_line * 100 / total_line))
        print("空行数:", blank_line, "占%0.2f%%" % (blank_line * 100 / total_line), "\n")
    else:
        print("代码行数：", total_line)
    return [total_line, comment_line, blank_line]


def run(file_path):
    os.chdir(file_path)
    total_lines = 0
    total_comment_lines = 0
    total_blank_lines = 0
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith(".py"):
                line = analyze_code(root + "/" + file)
                total_lines, total_comment_lines, total_blank_lines = (
                    total_lines + line[0],
                    total_comment_lines + line[1],
                    total_blank_lines + line[2],
                )
    if total_lines != 0:
        print("总代码行数:", total_lines)
        print(
            "总注释行数:",
            total_comment_lines,
            "占%0.2f%%" % (total_comment_lines * 100 / total_lines),
        )
        print(
            "总空行数:",
            total_blank_lines,
            "占%0.2f%%" % (total_blank_lines * 100 / total_lines) + "\n",
        )
    else:
        print("总代码行数:", total_lines)


def code_main():
    FILE_PATH = input("file path:")
    print("\n")
    run(FILE_PATH)
    os.system("pause")


if __name__ == "__main__":
    code_main()
