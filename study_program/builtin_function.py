#绝对值
print("abs(-10) : " + str(abs(-10)) + "\n")

#遍历下标和元素
print("In ['first','second','third']")
for i,num in enumerate(["first","second","third"]):
	print(i,num)
print()

#判断类型
print("isinstance('str',str) : " + str(isinstance("str",str)))
print("isinstance(5.5,int) : " + str(isinstance(5.5,int)) + "\n")

#得到类型
print("type(False) : " + str(type(False)))
print("type(5.5) : " + str(type(5.5)) + "\n")

#获取长度
print("len('Hello World!') : " + str(len('Hello World!')))
print("len([1,2,3,4,5]) : " + str(len([1,2,3,4,5])) + "\n")

#排序
print("sorted([3,4,2,1,5]) : " + str(sorted([3,4,2,1,5]))+"\n")

#求和
print("sum((1,2,3,4,5,6)) : " + str(sum((1,2,3,4,5,6))))
print("sum([[1,2],[3,4],[5,6]],[]) : " + str(sum([[1,2],[3,4],[5,6]],[])) + "\n")
