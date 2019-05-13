print("for ... else ... : ")
for i in range(1,10):
	if i==5:
		break
else:
	print("1.without break")

for i in range(1,10):
	if i==15:
		break
else:
	print("2.without break")
print()

print("函数注解 : def add(num1:int,num2:int)->int:")
def add(num1:int,num2:int)->int:
	return num1+num2
