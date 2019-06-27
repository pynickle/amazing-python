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

class Attr:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, old, new):
        print(f"{old} = {new} created.")
        object.__setattr__(self, old, new)

    def __delattr__(self, key):
        print(f"{key} deleted.")
        del self.__dict__[key]
        
    def __getattr__(self, item):
        return self.__dict__[item] 

member = Attr("nick", 13)
print(member.__dict__)
del member.age
print(member.__dict__)


class Item:
	def __init__(self, *args):
		self.name, self.age = args

	def __getitem__(self, key):
		print("__getitem__ called.")
		self.__dict__.get(key, ValueError)
		return key

	def __setitem__(self, key, value):
		print("__setitem__ called.")   
		self.__dict__.update({key: value})
		return {key:value}

	def __delitem__(self, key):
		print("__delitem__ called.")
		del self.__dict__[key]

a = Item("nick", 13)
print(a.__dict__)

print(a["name"])
print(a.__dict__)

a["name"] = "pynickle"
print(a.__dict__)

del a["age"]
print(a.__dict__)

class klassmethod:
    name = "nick"

    def hello(self):
        print("l am called with classmethod cls")

    @classmethod
    def kmethod(cls):
        print("l am classmethod")
        print("cls.name : " + cls.name)
        cls().hello()


klassmethod.kmethod()

class SlotTest:
    __slots__ = ("ice", "sugar")


tea = SlotTest()
tea.ice = "no ice"
tea.sugar = "a little sugar"
print("you can't add attribute not defined in __slots__")
