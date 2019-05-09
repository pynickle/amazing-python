def find_blank(string):
    for i,num in enumerate(string):
	    if num==" ":
		    print("blank position:"+str(i))
    print()
			
string="   test   "
print("origin:"+string+"\n")

print("lstrip:"+string.lstrip())
find_blank(string.lstrip())

print("rstrip:"+string.rstrip())
find_blank(string.rstrip())

print("strip:"+string.strip())
find_blank(string.strip())
