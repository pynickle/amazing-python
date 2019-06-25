from subprocess import Popen, PIPE
import os


NO_PYTHON = ("test.py", "auto_result.py", "README.md")
for root, dirs, files in os.walk("./study_program"):
    for file in files:
        if file.endswith("_result") or file in NO_PYTHON:
            continue
        p = Popen("python " + root + "/" + file, stdout=PIPE, bufsize=1)
        r = p.stdout.read()
        try:
            res = bytes.decode(r, encoding="gbk").replace("\r", "")
        except Exception:
            res = str(r, encoding="utf-8").replace("\r", "")
        index = slice(len(file) - 3)
        with open(root + "/" + file[index] + "_result", "w", encoding="utf-8") as f:
            f.write(res)
        p.stdout.close()
        p.wait()
