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
	return num_list

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

import time
def time_c():
	def wrapper(func):
		start=time.time()
		func()
		end=time.time()
		print(end - start)
	return wrapper

@time_c()
def sleep_test():
	time.sleep(2)

print("yield and send")
def yield_send():
	print("please tell me what you want to say")
	while True:
		words= yield
		print("l receive your words : " + str(words))

send_test=yield_send()
next(send_test)
send_test.send("hello")

print("with no super : ")
class me:
	def hello(self):
		print("Hello,everyone!")

class my_friend(me):
	def hello(self):
		me.hello(self)
		print("l am his friend")
	
my_friend().hello()
print()

print("with super : ")
class my_friend_with_super(me):
	def hello(self):
		#super(my_friend_with_super,self).hello()
		super().hello()
		print("l am his friend")
		
my_friend_with_super().hello()
print()

print("property : ")
class property_test:
	def __init__(self,height,weight):
		self.w = weight
		self.h = height
		
	def __repr__(self):
		return f"{self.__class__.__name__}({self.weight},{self.height})"
		
	@property
	def weight(self):
		return self.w
	
	@weight.setter
	def weight(self,new_weight):
		self.w = new_weight
	
	@property
	def height(self):
		return self.h
	
	@height.setter
	def height(self,new_height):
		self.h = new_height

you=property_test(50,170)
print(you.weight,you.height)
you.weight = 55
print(you)
you.height = 175
print(you)
print(help(property_test))
print()

print("kwargs and args")
def kwargs_args(name,*args,**kwargs):
	print(name)
	print(args)
	print(kwargs)

kwargs_args("nick", "foo", "bar", sex="male")

nums=[i**2 for i in range(10)]
dict_nums={i:i**2 for i in range(10)}
print(nums)
print(dict_nums)

print("lambda : ")
lambda_add = lambda a,b:a + b
print(lambda_add(1,4))

print("classmethod : ")
class klassmethod:
	name="nick"
	def hello():
		print("l am called with classmethod cls")
	
	@classmethod
	def kmethod(cls):
		print("l am classmethod")
		print("cls.name : " + cls.name)
		cls.hello()
klassmethod.kmethod()

first, second, *third = 1,2,3,4
print(first, second, third)
first, *second, third = 1,2,3,4
print(first, second, third)
