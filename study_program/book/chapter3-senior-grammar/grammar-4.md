## 装饰器
装饰器可以精简代码，使代码更可读，它可以用来装饰函数或者类，看一个简单的例子吧：
```python
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
```
这段代码运行结果如下：
```python
Hello World!
l am a decorator!
```
装饰器的语法是在函数的前面使用@wrapper，我们来逐步分析一下这段代码：
```python
result=function(*args,**kwargs)
```
这段代码表示执行这个函数。
```python
print("l am a decorator!")
```
这是我们在函数执行完后做的操作。
```python
return result
```
返回函数运行结果。
```python
    return wrapped
return real_decorator
```
返回这些里面的函数。

接下来我们就能看到在函数执行好后输出了l am a decorator了。接下来我们来写一个更加实用的装饰器，计算函数运行时间：
```python
import time
def time_c(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        elapsed = (time.time() - start)
        print("{} : Time used: {}".format(func.__name__, elapsed))
    return wrapper

@time_c
def sleep_test():
    time.sleep(2)
sleep_test()
```
结果为：
```python
sleep_test : Time used: 2.000603675842285
```
注意一点，func.__name__即是函数的名字。
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NDgwMjM2MDddfQ==
-->