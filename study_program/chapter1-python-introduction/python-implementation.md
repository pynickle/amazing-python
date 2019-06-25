## python的不同实现

我们一般所用的都是Cython，也就是使用C语言实现的Python，其中还有一些别的Python实现，有些也在尽力赶上Cython的更新。

#### IronPython

IronPython是在NET上实现的Python语言，因此可以便捷的嵌入C#，可惜的是目前最新版本只有2.7。与官方的Cython相比，IronPython有如下优点：
- 没有全局解释器锁（GIL）
- 可以在web中运行

#### Jython

Jython也就是使用Java实现Python，目前最新版本也为2.7。Jython有如下优点：
- 可以无缝使用Java中的类
- 和IronPython类似，没有GIL
- 使用Java垃圾回收，而不是Python的引用计数

#### PyPy

这是我看来最棒的Python实现了，也就是用Python实现Python，最新版本是Python3.6，根据官网（ http://pypy.org ），PyPy有如下优点：

- 使用JIT（Just In Time）显著提升了速度（[什么是JIT编译器](https://baike.baidu.com/item/JIT编译/2886569))
- 对于大型程序使用比Cython更少的内存
- 兼容性高，可以使用cffi或者流行库比如django和twisted
- 支持无栈特性，稍后我们会提到

#### Stackless Python

Stackless Python是无栈的Python实现，网址为（ https://github.com/stackless-dev/stackless ），其实这个项目对Cython源码进行了一些修改，不使用C语言的调用栈。
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzYzNjg0NDI0XX0=
-->