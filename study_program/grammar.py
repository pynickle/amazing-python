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
print()

print("yield : ")

def yield_test():
	for i in range(10):
		yield i
def normal_test():
	num_list=[]
	for i in range(10):
		num_list.append(i)
	return num_list()

yield_nums=yield_test()
print(yield_nums)
for num in yield_nums:
	print(num)

print("decorator : ")
def do():
	def real_decorator(function):
		def wrapped(*args,**kwargs):
			result=function(*args,**kwargs)
			print("l am a decorator!")
			return result
		return wrapped
	return real_decorator

@do()
def hello():
	print("Hello World!")

hello()

print("yield and send")
def yield_send():
	print("please tell me what you want to say")
	while True:
		words= yield
		print("l receive your words : " + str(words))

send_test=yield_send()
next(send_test)
send_test.send("hello")
