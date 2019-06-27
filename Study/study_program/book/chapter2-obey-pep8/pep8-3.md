## 工具

开始遵守pep8总免不了出现一些疏忽，这时就需要工具帮助我们。比较有名的工具有下面这几个：
## pylint

pylint堪称是pep8检查的“高手”，他不仅能检查pep8，还能检测到未使用的变量等等，最后还会给你一个评分。最重要的，他是可以被定制的，如果你的团队有些地方有自己独创的风格，那么个性化定制是个好选择。

首先安装：
```bash
pip install pylint
```

接下来使用它：
```bash
pylint test.py
```

会输出像下面这样的结果：
```bash
study_program\grammar.py:365:0: W0312: Found indentation with tabs instead of spaces (mixed-indentation)
study_program\grammar.py:87:0: C0111: Missing function docstring (missing-docstring)
study_program\grammar.py:89:8: W0621: Redefining name 'i' from outer scope (line 26) (redefined-outer-name)
...
Your code has been rated at 5.26/10
```
最左边是文件名，再过去是位置，再过去就是哪里不对的详细解释了。接下来说说怎么自定义：
```bash
pylint --generate-rcfile > .pylintrc
```
执行完上面这个命令后你会看到.pylintrc文件，这就是自定义文件了，别看有几百行，可都是有注释的，比如说：
```python
# Maximum number of characters on a single line.
max-line-length=100
```
这里写道：
```
# 一行内最多允许的字符数目
max-line-length=100
```
接下来就自己调去吧！
## pycodestyle

pycodestyle不像pylint，他只专注于pep8，用法差不多，就不细讲了：
```bash
pip install pycodestyle
pycodestyle test.py
```
## autopep8
发现不对当然要有东西帮我们改正，autopep8就解决了这个问题：
```bash
pip install autopep8
autopep8 --in-place test.py
```
--in-place代表不在命令行输出，直接写入文件，其中-a代表增大优化力度，最大为2级：
```
autopep8 --in-place -a -a test.py
```
由于每次都要输入命令，我便开发了一个工具，可以批量优化一个文件夹里的所有py文件：[beautify_code](https://github.com/pynickle/amazing-python/tree/master/beautify_code)

这是一个图形化界面应用，在我的[github](https://github.com/pynickle/amazing-python/blob/master/README.rst)上有完整的使用方法，不妨去看看吧！