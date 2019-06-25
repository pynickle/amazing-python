继续我们的高级语法：

## with语句

相信大家对下面的代码已经很熟悉了：
```python
with open(“test.txt”,”a”) as f:
    f.write(“Hello,open!”)
```
上面这段代码的含义也就是打开test.txt文件并写入Hello,open!，然而大家有没有想过with真正有什么用呢，下面是一个不用with的例子：
```python
try:
    f=open(“test.txt”,”a”)
    f.write(“Hello,open!”)
except:
    pass
finally:
    f.close()
```
很明显使用with后代码量减少了，也使代码更具可读性了，接下来我们就来讲讲怎么自己实现一个类来和with结合使用：
```python
class With():
    def __enter__(self):
        print("enter!")
        return self
    def operate(self,name,bug):
        print("operate " + name + "!" + bug)
    def __exit__(self,exc_type,exc_value,traceback):
        print("exc_type : " + str(exc_type))
        print("exc_value : " + str(exc_value))
        print("traceback : " + str(traceback))
        print("exit!")
bug=1
with With() as opr:
    opr.operate("nick",bug)
```
上述代码执行结果为：
```python
enter!
exc_type : <class 'TypeError'>
exc_value : must be str, not int
traceback : <traceback object at 0x7fd9130c16c8>
exit!
Traceback (most recent call last):
  File "/tmp/225769800/main.py", line 16, in <module>
    opr.operate("nick",bug)
  File "/tmp/225769800/main.py", line 6, in operate
    print("operate " + name + "!" + bug)
TypeError: must be str, not int
```
首先我们使用__enter__方法表示开始的一些操作，接下来我们可以在类中定义我们进行的操作，最后使用__exit__方法保证退出，可以看出虽然抛出了错误，程序依然执行完了最后的__exit__方法，那么如果我们不想让程序抛出错误呢？
```python
class With():
	def __enter__(self):
		print("enter!")
		return self
	def operate(self,name,bug):
		print("operate " + name + "!" + bug)
	def __exit__(self,exc_type,exc_value,traceback):
		print("exc_type : " + str(exc_type))
		print("exc_value : " + str(exc_value))
		print("traceback : " + str(traceback))
		print("exit!")
		return True
		
bug=1
with With() as opr:
	opr.operate("nick",bug)
```
执行结果为：
```python
enter!
exc_type : <class 'TypeError'>
exc_value : must be str, not int
traceback : <traceback object at 0x7f64bb550708>
exit!
```
只要我们在__exit__方法中return True程序就不会抛出错误了。


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNTk5OTg5NTldfQ==
-->