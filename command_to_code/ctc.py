def replace_command_to_code(str):
    lst = str.split('\n')
    result = ''
    for i in lst:
        if i.startswith('>>> '):
            i = i.replace('>>> ', '')
        elif i.startswith('... '):
            i = i.replace('... ', '')
        elif i == '...' or i == '>>>':
            i = ''
        result = result+i+'\n'
    return result


print("input command : ")
result = ''
while True:
    command = input()
    if command == 'q':
        break
    else:
        result = result + command + '\n'
print("\ncode : ")
print(replace_command_to_code(result))
