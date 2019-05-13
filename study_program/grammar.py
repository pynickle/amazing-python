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
print()

print("with : ")
class With():
	def __enter__(self):
		print("enter!")
		return self
	def operate(self,name,bug):
		print("operate " + name + "!" + bug)
	def __exit__(self,exc_type,exc_value,traceback):
		print("exc_type : " + str(exc_type))
		print("exc_value : " + str(exc_value))
		print("traceback : " + str(traceback))
		print("exit!")
		return True
		
bug=1
with With() as opr:
	opr.operate("nick",bug)
