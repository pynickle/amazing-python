import subprocess


cmd1 = 'trans -t '
cmd2 = 'trans --trans '

translate_text = 'example'

test1 = subprocess.Popen(cmd1 + translate_text,
                         stdout=subprocess.PIPE, bufsize=1)
test2 = subprocess.Popen(cmd2 + translate_text,
                         stdout=subprocess.PIPE, bufsize=1)

print("trans -t example:")
for line in iter(test1.stdout.readline, b''):
    print(bytes.decode(line, encoding="gbk"))

print("trans --trans example:")
for line in iter(test2.stdout.readline, b''):
    print(bytes.decode(line, encoding="gbk"))
