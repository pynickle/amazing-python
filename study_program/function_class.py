import dis

def method():
	'''this function print and return my name'''
	name = "nick"
	print("l am", name)
	return name

print("help(method) : ")
print(str(help(method)) + "\n")

print("method.__doc__ : ")
print(method.__doc__ + "\n")

print("method.__name__ : ")
print(method.__name__ + "\n")

print("method.__code__ : ")
print(str(method.__code__) + "\n")

print("dis.show_code(method) : ")
print(str(dis.show_code(method)) + "\n")

class A(): pass

class Base(A):
	"""
	document there
	"""
	name="nick"
	__secret="123456"
	def __repr__():
		return name
	def say_hello(name):
		print("hello," + name)
	def _secret_method():
		return __secret__

Base.another="hello world"

print("Base.another : ")
print(Base.another + "\n")

print("Base.__doc__ : ")
print(Base.__doc__ + '\n')

print("Base.__module__ : ")
print(Base.__module__ + '\n')

print("Base.__class__ : ")
print(str(Base.__class__) + "\n")

print("Base.__dict__ : ")
print(str(Base.__dict__) + "\n")

print("Base.__bases__ : ")
print(Base.__bases__)

class Meta(type):
    def __new__(meta, *args, **kwargs):
        clsname, bases, namespace = args

        print(clsname, 'Meta new called')
        return super().__new__(meta, *args)

    def __init__(cls, *args, **kwargs):
        print(cls.__name__, 'Meta init called')
        super().__init__(*args)


    @classmethod
    def __prepare__(meta, name, bases):
        print(name, "Meta prepare called")
        return {}

class Base(metaclass=Meta):

    def __new__(cls, *args, **kwargs):
        print(cls.__name__, 'Base new called')
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print(type(self).__name__, 'Base init called')
    def hello(self):
        pass

b = Base("metaclass expert")
print(type(Base))



class GetAttr:
	def __init__(self, name, age):
		self.name = name
		self.age = age
    
	def __getattribute__(self, obj):
		print("__getattribute__ called.")
		return object.__getattribute__(self, obj)
    
	def __getattr__(self, obj):
		print("__getattr__ called.")
		raise AttributeError(f"Attribute {obj} not assgined!")
		
member = GetAttr("nick", 24)

print(member.name)
try:
	print(member.gender)
except Exception as e:
	print(e)
