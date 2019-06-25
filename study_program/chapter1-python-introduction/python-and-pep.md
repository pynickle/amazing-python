## Python2和3

Python的历史可以追溯到20世纪80年代，而一个重要时间则是Python3发布的日期：2008年12月3日。Python3和Python2相比主要是这几个变化：

- 支持unicode（unicode_literals）
- print不再是语句，而是一个函数（print_function）
- 导入默认为绝对导入（absolute_import）
- /返回浮点数，//返回整数（division）

上述的这些变化也就是__future__模块给我们提供的。

<b>注意，__future__必须在python文件开头import，并且不要使用from __future__ import *</b>

## Python兼容

正因为Python2的持续使用，才有了保持Python兼容性的工具，包括上面我们提到的__future__标准库，其中还有six库被许多库用来保持兼容性，但这明显也不是最佳解决方案，Python3取代Python2是必然的结果，许多第三方库也将放弃对Python2的支持。

## PEP是什么

PEP的全称为Python Extension Proposal，也就是Python改进提案，也就是Python变化的文档。所有PEP都被汇总在PEP0（ https://www.python.org/dev/peps ），相信大家最熟悉也就是PEP8 ：Python风格指南。
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM1MDEyMV19
-->