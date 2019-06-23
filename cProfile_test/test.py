import subprocess
import csv
import os


first_line = ['ncalls', 'tottime', 'percall',
              'cumtime', 'percall filename:lineno(function)']
with open('test_result.csv', 'a', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(first_line)


def eval_cmd(path):
    cmd = 'python -m cProfile ' + path
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1)
    write = False
    count = 0

    for line in iter(p.stdout.readline, b''):
        try:
            line = bytes.decode(line)
        except Exception:
            try:
                line = str(line, encoding="gbk")
            except Exception:
                continue
        print(line)
        if write == True:
            count += 1
            if count >= 3:
                line = line.strip()
                line_list = line.split('    ', 4)
                with open('test_result.csv', 'a', newline='') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(line_list)
        if 'Ordered by:' in line:
            write = True

    p.stdout.close()
    p.wait()


def test_main():
    path = input("test file path:")
    if os.path.exists(path):
        eval_cmd(path)
    else:
        print("wrong path!")


if __name__ == "__main__":
    test_main()
