Welcome to amazing-python!
==========================

.. image:: https://pynickle.github.io/amazing-python-logo.jpg

-----

Enjoy the amazing tools here!
*****

And study more from study program and interesting program!
*****

Do not forget to have fun from what the f*ck!
*****

-----

**Code here all run in the latest python stable version python3.7**

.. image:: https://codebeat.co/assets/svg/badges/A-398b39-669406e9e1b136187b91af587d4092b0160370f271f66a651f444b990c2730e9.svg
    :target: https://codebeat.co/projects/github-com-pynickle-amazing-python-master

.. image:: https://badges.gitter.im/amazing-python/community.svg
    :target: https://gitter.im/amazing-python/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge

.. image:: https://hits.b3log.org/b3log/awesome-python-tools.svg
    :target: https://github.com/pynickle/amazing-python
    
.. image:: https://img.shields.io/github/languages/code-size/b3log/awesome-python-tools.svg
    :target: https://github.com/pynickle/amazing-python

=================== =====
**Travis CI**       .. image:: https://travis-ci.org/pynickle/amazing-python.svg?branch=master
                        :target: https://travis-ci.org/pynickle/amazing-python  
=================== =====
**Azure Pipelines** .. image:: https://dev.azure.com/2330458484/2330458484/_apis/build/status/pynickle.amazing-python?branchName=master
                        :target: https://github.com/pynickle/amazing-python
=================== =====

Usage
^^^^^

requirements.txt
^^^^^^^^^^^^^^^^
这个项目需要用到的所有第三方库，用::

    pip install -r requirements.txt
    
安装所有第三方库，pyaudio库由于会安装失败，请自行到 `pyaudio-install`_ 下载

Pull\_Requests\_Template
^^^^^^^^^^^^^^^^^^^^^^^^
*用于pull requests的模板文档*

Python\_Use
^^^^^^^^^^^
*Python的框架和它们的网站整理*

study\_program
^^^^^^^^^^^^^^
*通过程序学习python及其高极用法*

这里面的book文件夹则是我对这些知识的解析。

**-- written by me**

interesting\_program
^^^^^^^^^^^^^^^^^^^^
*可以用来练手或有用的的小型python程序*

what\_the\_fuck
^^^^^^^^^^^^^^^
*为wtfpython所启发，收集各种令人难以理解的输出并解释*

pip\_update 
^^^^^^^^^^^
*使用pip库一键升级python第三方库*

no thread的文件代表不使用redis数据库，在速度方面会慢一些。

而with thread使用redis数据库，在使用前请自行查询相关教程安装好redis！首先运行一遍主程序（注意，只运行一遍！）。然后在多个命令行里运行slave1.py，然后等待完成。

scrapy\_images 
^^^^^^^^^^^^^^
*抓取任意网站图片并保存到指定路径* 

你可以制定抓取网址，存储位置和存储格式。

translate\_app 
^^^^^^^^^^^^^^
*多种方式翻译你的文本*

目前已发布到pypi上，可以使用如下命令下载::

    pip install quicktranslate
    
使用方式如下::

    trans -t example

zip\_to\_see 
^^^^^^^^^^^^
*快速解压zip文件* 

选择zip文件并按下按钮，该文件会被解压到当前目录下

how\_many\_code
^^^^^^^^^^^^^^^
*计算路径下你曾经写过多少python代码* 

输入路径，程序会输出每个文件的注释行数，空行数和代码行数以及总的数据

beautify\_code
^^^^^^^^^^^^^^^^^^
*使用gofmt（格式化go代码），autopep8或black格式化你的代码，目前支持自定义参数*

**自定义参数规则如下**::

    file_type ** parameters_run
    
file_type代表文件类型，示例：.py .go

parameters_run代表你要执行的命令，其中可以包括两个变量，他们用{{ }}包裹：
- root ： 代表你输入的文件路径
- file ： 代表该路径下的所有文件

file_type和parameters_run用 ** 分割

一个示例自定义参数如下::

    .py ** autopep8 --in-place -a {{root}}/{{file}}

pyinstaller\_all
^^^^^^^^^^^^^^^^
*批量以-F开启时使用pyinstaller打包文件并自动删除冗余文件，也可删除路径下所有exe文件*

目前已发布到pypi上，可以使用如下方式下载::

    pip install quickpack
    
如下方式使用::

    pack -r -p path
    
-r代表在打包前去除所有exe文件。

**注意，带tkinter的已经停止维护，以命令行使用为最新版本**

voice\_picture
^^^^^^^^^^^^^^
*音频可视化每一帧，以图片形式更清晰*

test
^^^^
*用cProfile测试你的代码并将结果写入csv文件*

pyaudio
^^^^^^^
*录音并保存到文件，也可播放*

可以选择秒数，文件名，按下按钮开始。保存到当前目录，也可以使用下面的按钮直接回收。

command\_to\_code
^^^^^^^^^^^^^^^^^^^^^
*将python命令行转换为可运行的python代码*

目前已发布置我的GitHub pages，网址为::

    https://code-nick-python.github.io/ctc.html

左边的输入框用来输入命令行，右边会实时显现出转换后的代码

-----------------
How to contribute
-----------------

1. **Fork the repository to your own repository**
2. **Commit your code in your fork repository**
3. **Change the document accordingly**
4. **Use the document** `Pull_Requests_Template`_ **to pull requests**

**PS : If you have any good idea, welcome talk and pull requests!**

License
^^^^^^^

author : **pynickle**

license : 

*FOR STUDY PROGRAM(EXCEPT BOOK FOLDER), INTERESTING PROGRAM AND WHAT THE FUCK:*

**MIT License**

*FOR BOOK FOLDER:*

**BSD-2-Clause License**

*FOR ELSE:*

**WTFPL License**


.. _pyaudio-install: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
.. _`Pull_Requests_Template`: https://github.com/code-nick-python/awesome-python-tools/blob/master/Pull_Requests_Template.md
