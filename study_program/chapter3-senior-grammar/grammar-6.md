## property

property装饰器会会让我们定义设置包括获取属性等的操作，下面是一个比较经典的例子，正方形：
```python
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
```
看看结果吧：
```python
170 50
property_test(55,50)
property_test(55,175)
Help on class property_test in module __main__:

class property_test(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, height, weight)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  height
 |  
 |  weight

None
```
通过property装饰器我们可以便捷地设置和获取属性，快使用起来吧。
## *args and **kwargs
*args和**kwargs帮助我们自定义参数，*args接受像 ,a,这样的，而**kwargs接受像 ,a = b, 之类的参数：
```python
def kwargs_args(name,*args,**kwargs):
	print(name)
	print(args)
	print(kwargs)

kwargs_args("nick", "foo", "bar", sex="male")
```
上述代码得到的结果是：（我想不用解释了吧）
```python
nick
('foo', 'bar')
{'sex': 'male'}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NDM0NTQ4NzZdfQ==
-->