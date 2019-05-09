#调整位置
print("title".center(30,"-"))
print("content1".ljust(30),"content2".rjust(30) + "\n")

#反转字符串
reverse="test-str"
print("origin : " + reverse)
print("string[::-1] : " + reverse[::-1] + "\n")

#去除首尾字符串
def find_blank(string):
    for i,num in enumerate(string):
	    if num==" ":
		    print("blank position:"+str(i))
    print()
			
no_blank="   test   "
print("origin:"+no_blank+"\n")

print("lstrip:"+no_blank.lstrip())
find_blank(no_blank.lstrip())

print("rstrip:"+no_blank.rstrip())
find_blank(no_blank.rstrip())

print("strip:"+no_blank.strip())
find_blank(no_blank.strip())
