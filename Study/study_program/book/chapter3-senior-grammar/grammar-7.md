## 列表推导式

所谓列表推导式也就是更方便的创建（带有特点条件的）数组，比如说我们想创建一个1到100间偶数的列表，不用列表推导式：
```python
lst = []
for i in range(10):
	lst.append(i)
```
这会创建一个0到9的列表，看看列表推导式的写法
```python
nums = [i for i in range(10)]
```
或者更复杂一些
```python
nums = [i**2 for i in range(10)]   #创建0-9的平方
dict_nums = {i: i**2 for i in range(10)}   #字典实现
```
或者加入一些条件在后面，偶数列表：
```python
if_nums = [i for i in range(10) if i % 2 == 0]
```
## lambda关键字

lambda用于创建一些简单的函数，下面是一个正常的例子：
```python
def lambda_add(a, b):
    return a + b
```
这么一个简单的函数可以使用可读性更好的lambda解决：
```python
lambda_add = lambda a, b:a + b
```
接下来你就可以按一个正常的函数使用它了。

这次我们介绍一个其他的用处，就是在tkinter设置button的command处只能设置没有参数的函数的情况，只能这样
```python
def no_para(): pass
a = top.Button("top", text = "with no para", command = no_para)
```
用了lambda，我们可以使用带参数的函数了！
```python
def have_para(para): print(para)
a = top.Button("top", text="have para", command=lambda:have_para("para here"))
```
lambda有用吧！
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NjY3NDg0MF19
-->