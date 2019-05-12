import dis

def method():
	'''this function print my name'''
	print("l am nick")

print("help(method) : ")
print(str(help(method)) + "\n")

print("method.__doc__ : ")
print(method.__doc__ + "\n")

print("method.__name__ : ")
print(method.__name__ + "\n")

print("method.__code__ : ")
print(str(method.__code__) + "\n")

print("dis.show_code(method) : ")
print(str(dis.show_code(method)) + "\n")
