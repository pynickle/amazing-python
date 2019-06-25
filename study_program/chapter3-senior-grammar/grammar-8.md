## classmethod

classmethod可以定义函数为类方法。函数为cls和若干args，通过cls可以访问类的方法和变量，下面是一个例子：
```python
class klassmethod:
    name = "nick"

    def hello():
        print("l am called with classmethod cls")

    @classmethod
    def kmethod(cls):
        print("l am classmethod")
        print("cls.name : " + cls.name)
        cls.hello()

klassmethod.kmethod()
```
结果是：
```python
l am classmethod
cls.name : nick
l am called with classmethod cls
```
可以看到我们成功调用了这些东西，另一个特点是这样不用实例化类。
## *和变量

有时候我们会在变量命名前加上*，这代表什么意思呢？看一个例子你应该就明白了：
```python
first, second, *third = 1, 2, 3, 4
print(first, second, third)
first, *second, third = 1, 2, 3, 4
print(first, second, third)
```
看看结果吧，其实就是取了剩余的部分：
```python
1 2 [3, 4]
1 [2, 3] 4
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTM2Mjg4MzUxXX0=
-->