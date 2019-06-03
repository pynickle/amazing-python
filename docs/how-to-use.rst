------------
开源项目声明
------------

amazing-python
^^^^^^^^^^^^^^

author : pynickle

license : MIT License

------------
文件功能介绍
------------

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

interesting\_program
^^^^^^^^^^^^^^^^^^^^
*可以用来练手或有用的的小型python程序*

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

how\_many\_code
^^^^^^^^^^^^^^^
*计算路径下你曾经写过多少python代码* 

beautify-your-code
^^^^^^^^^^^^^^^^^^
*使用black库全自动格式化格式化你的代码* 

autopep8\_code
^^^^^^^^^^^^^^
*使用autopep8库全自动格式化你的python代码* 

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

command\_to\_code
^^^^^^^^^^^^^^^^^^^^^
*将python命令行转换为可运行的python代码*

目前已发布置我的GitHub pages，网址为::

    https://code-nick-python.github.io/ctc.html

左边的输入框用来输入命令行，右边会实时显现出转换后的代码

-----------------
How to contribute
-----------------

1. Fork the repository to your own repository
2. Commit your code in your fork repository
3. Change the document accordingly
4. Use the document `Pull_Requests_Template`_ to pull requests

.. _pyaudio-install: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
.. _`Pull_Requests_Template`: https://github.com/code-nick-python/awesome-python-tools/blob/master/Pull_Requests_Template.md
