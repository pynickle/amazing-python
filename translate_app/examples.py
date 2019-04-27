import subprocess


cmd1 = 'trans -t '
cmd2 = 'trans --trans '

translate_text = 'example'

test1 = subprocess.Popen(cmd1 + translate_text, stdout=subprocess.PIPE, bufsize=1)

for line in iter(test1.stdout.readline,b''):
    print(bytes.decode(line,encoding="gbk"))