from setuptools import setup, find_packages
setup(
    name="quicktranslate",
    version="1.0.1",
    description="translate with youdao,baidu and google",
    long_description="""
    you can use this in the command line,this is a example::

        trans -t example

    or::
        
        trans --trans example
    
    'example' means what you want to translate
    """,
    author='code-nick-python',
    author_email='2330458484@qq.com',
    url="https://github.com/code-nick-python/daily-tools/tree/master/translate_app",
    license='MIT License',
    packages=find_packages(),
    platforms="any",
    py_modules=['quicktranslate'],
    install_requires=[
        'requests',
        'bs4',
        'pyexecjs'
    ],
    classifiers={
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    },
    entry_points={
        'console_scripts': [
            'trans = quicktranslate:translate_main',
        ],
    }
)
