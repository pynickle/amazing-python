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

#聚合每个可迭代对象的元素
zip1=['1','2','3']
zip2=['4','5','6']
for i in zip(zip1,zip2):
    print(i)
print()

#转二进制
print("bin(14) : " + bin(14))
print("f'{14:b}' : " + f'{14:b}' + "\n")

#迭代
iter_list=[1,2,3,4,5]
iter_element=iter(iter_list)
print("iter the list[1,2,3,4,5]:")
while True:
    try:
        print(next(iter_element))
    except:
        break

#判断True False
print(bool(None))
print(bool([1,2,3]))

#转为bytes
print(bytes('string',encoding="utf-8"))
print(bytes('我是中文',encoding="utf-8"))
