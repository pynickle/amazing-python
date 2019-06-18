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

byte_test = "我是中文"
print("origin : " + byte_test)
byte = byte_test.encode("utf-8")
print("after encode : " + str(byte))
byte_decode = byte.decode("utf-8")
print("after decode : " + byte_decode)

number_str = "12345"
print(number_str.isnumeric())
print(number_str.zfill(10))

blank_str = "   "
print(blank_str.isspace())

english_str = "english"
print(english_str.isalpha())

strip_str = "Hello-World-nick"
print(strip_str.partition("-"))
print(strip_str.rpartition("-"))

line_str = "Hello\nWorld"
print(line_str.splitlines())

weight_str = "Hello World"
print(weight_str.swapcase())

trans1 = "abcde"
trans2 = "12345"
trans_tab = str.maketrans(trans1, trans2)
trans_str = "Hello,everyone.l am nick"
print(trans_str.translate(trans_tab))
