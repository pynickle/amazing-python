# nonlocal

又是python的一个关键字，nonlocal。global相信大家都知道，那么global和nonlocal有什么区别呢？首先我们来看看global：

global是用来引用全局变量的，比如说下面这个例子
```python
test = 1
def global_1():
	print(test)
global_1()
```
这个例子会正常的输出1，但并非次次都如此：
```python
test = 1
def global_2():
	test += 1
	print(test)
global_2()
```
上面这个例子会触发UnboundLocalError，这时候global就发挥作用了：
```python
test = 1
def global_2():
    global test
	test += 1
	print(test)
global_2()
```
这样我们的函数又能正常工作了。

接下来我们来看看nonlocal，nonlocal是用来使用外部变量的，我们看一个例子：
```python
def counter_nonlocal():
    count = 0

    def count_add():
        nonlocal count
        count += 1
        return count
    return count_add

def counter_test():
    num = counter_nonlocal()
    print(num())
    print(num())

counter_test()
```
这个例子会输出1 2，这里的nonlocal声明后我们使用的就是我们在外部定义的count了，也就起到了累加的作用。

## ...

这个语法比较特别，就是...，这是一个可以用来代替pass的方法额，尽管我认为pass更好：
```python
print(type(...))


def hello():
    ...
```
结果：
```python
<class 'ellipsis'>
```