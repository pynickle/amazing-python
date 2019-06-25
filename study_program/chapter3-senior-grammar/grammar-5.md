## yield和send

我们之前学习了yield作为生成器的语法和好处，其实yield还有另一种用法，看例子：
```python
def yield_send():
    print("please tell me what you want to say")
    while True:
        words= yield
        print("l receive your words : " + str(words))
send_test=yield_send()
next(send_test)
send_test.send("hello")
```
我们直接使用了`words = yield`，并使用`send`给yield传送信息，**注意：要先使用next，不然会报错不能给一个刚开始的函数传递值。** 结果如下：
```python
l received your words : hello
```
## super

首先我们从一个简单的类开始：
```python
class me:
    def hello(self):
        print("Hello,everyone!")
class my_friend(me):
    def hello(self):
        me.hello(self)
        print("l am his friend")
my_friend().hello()
```
这会得到如下结果：
```python
Hello,everyone!
l am his friend
```
那么我们如何使用super重新完成这段代码呢，这样做：
```python
class me:
    def hello(self):
        print("Hello,everyone!")
class my_friend_with_super(me):
	def hello(self):
		#super(my_friend_with_super,self).hello()
		super().hello()
		print("l am his friend")		
my_friend_with_super().hello()
```
我们用super达到了同样的效果。注释掉的那个是简化形式。super可以调用超类中的方法，再来看一个稍微难一点的例子，与classmethod结合使用：
```python
class Tea:
	def __init__(self, things):
		self.things = things
	def __repr__(self):
		return self.things
	@classmethod
	def need(cls):
		return cls(["sugar", "pearl", "water"])
class PearlTea(Tea):
	@classmethod
	def need(cls):
		needed = super().need().things
		needed += ["pearl"] * 2
		return needed
mytea = Tea.need()
mypearltea = PearlTea.need()
print(mytea.things)
print(mypearltea)
```
你会得到：
```python
['sugar', 'pearl', 'water']
['sugar', 'pearl', 'water', 'pearl', 'pearl']
```
我们从中华可以得到，在super只提供第一个参数时，它将返回一个unbound（未绑定的类型）。super是一个较难的知识点，下次我们继续。

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM1NDU1NTMxM119
-->