## 什么是pep8
pep8也就是我们熟知的PEP文档中的一部分，它就是著名的Python编码风格指南，我们可以来看两个例子：

我们来看看下面两段代码那个更得人心：
```python
a,b,c="nick","steven","alice"
print("my name is",a)
print("my best friends are",b,"and",c)
```
```python
my_name, friend1, friend2 = "nick", "steven", "alice"
print(f"my name is {my_name}")
print(f"my best friends are {friend1} and {friend2}")
```
这两段代码都会输出以下相同的结果：
```python
my name is nick
my best friends are steven and alice
```
但是我们都知道第二段代码更得人心，代码更加宽松，也更具有可读性，这就是pep8的重要性。

记住，如果你有一个Python开源项目，务必遵守pep8！

pep8的网址在[pep8.org](https://pep8.org)
