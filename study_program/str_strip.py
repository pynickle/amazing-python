string="   test   "
print("origin:"+string)
print("lstrip:"+string.lstrip())
for i,num in enumerate(string.lstrip()):
	if num==" ":
		print("blank position:"+str(i))
print("rstrip:"+string.rstrip())
for i,num in enumerate(string.rstrip()):
	if num==" ":
		print("blank position:"+str(i))
print("strip:"+string.strip())
for i,num in enumerate(string.strip()):
	if num==" ":
		print("blank position:"+str(i))
