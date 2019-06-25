首先我们从Python鲜为人知或是高级语法开始学习。
## for ... else ...

我们所熟知的python中的for循环的用法是这样的：
```python
for i in range(1,10):
    print(i)
#或者是这样：
for i in [1,2,3]:
    print(i)
```
  然而真的就只有这些吗？答案是否定的。事实上，Python也给for循环增加了else语法，看下面的例子：
```python
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
```
输出为：
```python
2.without break
```
可以看出else语句在没有break时执行。

## 函数注解

尽管Python是一门动态类型语言，但在Python3.5中加入了类型检查功能，代码如下：
```python
def add(num1:int,num2:int)->int:
    return num1+num2
```
你可以使用`parameter:type`和`->type`来表示参数类型和返回类型。

你也可以使用__annotations__属性获取这些type。当然，由于Python强大的动态特性，你可以现场修改这些type，（虽然这明显不是一个很好的实践）：
```python
print(add.__annotations__)
print(add(1,2))

add.__annotations__["num1"] = str
add.__annotations__["num2"] = str
add.__annotations__["return"] = str

print(add.__annotations__)
print(add("hello ", "world"))
```
结果：
```python
{'num1': <class 'int'>, 'num2': <class 'int'>, 'return': <class 'int'>}
3
{'num1': <class 'str'>, 'num2': <class 'str'>, 'return': <class 'str'>}
hello world
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA0MDYwMjA4NV19
-->