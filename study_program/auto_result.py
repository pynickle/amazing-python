from subprocess import Popen, PIPE
import os


NO_PYTHON = ("test.py", "auto_result.py", "README.md")
for root, dirs, files in os.walk("./study_program"):
    for file in files:
        print(file)
        if file.endswith("_result") or file in NO_PYTHON:
            continue
        p = Popen("python " + root + "/" + file, stdout=PIPE, bufsize=1)
        r = p.stdout.read()
        try:
            res = bytes.decode(r, encoding="utf-8").replace("\r", "")
        except Exception:
            res = str(r, encoding="gbk").replace("\r", "")
        index = len(file) - 3
        with open(root + "/" + file[:index] + "_result", "w") as f:
            f.write(res)
        p.stdout.close()
        p.wait()
