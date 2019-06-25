## yield
yield也就是生成器，我们用代码说话：
```Python
def yield_test():
    for i in range(10):
		yield i
def normal_test():
	num_list=[]
	for i in range(10):
		num_list.append(i)
	return num_list

yield_nums=yield_test()
print(yield_nums)
for num in yield_nums:
	print(num)
```
你会得到如下结果：
```python
<generator object yield_test at 0x7f4880aeb410>
0
1
2
3
4
5
6
7
8
9
```
从上面这段代码来看，明显yield的实现更加简洁，再看一个例子：
```python
def yield_test():
	for i in range(10):
		yield i
yield_nums = yield_test()
while True:
	try:
		print(yield_nums.__next__())
		print(next(yield_nums))
	except StopIteration as e:
		print(e)
		break
```
我们可以使用next来获取下一个值，在没有yield时会触发StopIterarion错误。

其中yield还有一个其他的作用：节约你的内存。yield只在你需要时计算下一个值，这里我们不加叙述，大家可以参考内置库itertools中的一些函数。
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MjY2MjkzOV19
-->