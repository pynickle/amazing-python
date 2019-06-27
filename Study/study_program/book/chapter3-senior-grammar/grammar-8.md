
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

## int

这次我们来点有趣的小例子，我们来探究一下int类的妙用。首先int类的self有一个叫做numerator的玩意，我们用代码来解释一下这到底是什么：
```python
class test(int):
	def __call__(self, x):
		print(x, self, self.numerator)
		return test(self.numerator + x)
a = test()
a(1)(2)(3)
```
多个括号即会触发多次call，上述代码的运行结果为：
```python
1 0 0
2 1 1
3 3 3
```
从中我们可以看出numerator能帮我们累计一些东西。

我们可以再来看看int类中的一段定义numerator的代码
```python
numerator = property(lambda self: object(), lambda self, v: None, lambda self: None) 
# default  """the numerator of a rational number in lowest terms"""
```
除了上面这种写法，我们还可以把这个类包在函数中：
```python
def add(x):
    class AddNum(int):
        def __call__(self, x):
            return AddNum(self.numerator + x)
    return AddNum(x)

print(add(1)(2)(3)(4))
```
显而易见，结果是10