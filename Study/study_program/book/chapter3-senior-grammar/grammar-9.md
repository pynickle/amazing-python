## assert
assert是一种能让你快速进行测试的工具，它是一个关键字。用法如下
```python
assert expression [",", expression]
```
如果还是有点蒙，那么一个例子可能会让你明白：
```python
def hello(name: str):
    assert len(name) > 1, "your name is too short!"
    print("hello,", name)


hello("nick")
try:
    hello("a")
except Exception as e:
    print(e)
```
结果为：
```python
hello, nick
your name is too short!
```
我们来仔细看看这个assert语句，首先跟着的是条件，也就是名字长度要大于1，接下来是一个字符串。连起来就是条件不成立，assert把错抛。
## raise

我们写程序时是不是会遇到一些bug，那么我们怎么自己来定义并抛出错误呢，这时候就要用到我们的raise关键字了：
```python
import traceback
class ExitBye(Exception):
    pass

try:
    print(1 / 0)
except Exception as e:
    try:
        raise ExitBye("have an error with raise") from e
    except Exception as e:
        traceback.print_exc()
```
首先我们定义了一个自己的错误，这个错误也就是继承Exception类的，这是一个“错误”的基类。

随后我们进行了一次错误的操作，触发了ZeroDivisionError，我们使用except避免了这个错误，并再次进入到try中，我们的raise就出场了。

raise的基本语法
```python
raise what_error("error message")
```
那么大家可能就疑惑于我们后面的from e是什么意思了，这就代表是上面这个e错误触发了下面的错误，看看结果吧，我想你会明白的：
```python
Traceback (most recent call last):
  File "/tmp/711293792/main.py", line 7, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tmp/711293792/main.py", line 10, in <module>
    raise ExitBye("have an error with raise") from e
ExitBye: have an error with raise
```
我们在中间可以看到“上面的错误直接导致了下面下面的错误”，这也就印证了我们的解释。

最后我们使用traceback和print_exc函数获取完整的错误信息，也就是打印出来的那些啦
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAxNDAwNDIxNl19
-->