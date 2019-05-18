from setuptools import setup, find_packages
setup(
    name="quickpack",
    version="0.0.2",
    description="pack your file with pyinstaller and automatically remove all useless files",
    long_description="""
    you can use this in the command line,the tool will pack all py files under the path you enter,this is a example::

        pack -p path

    you can also remove all exe under the path before packing::
        
        pack -r -p path
    
    use pack -h to get more information
    """,
    author='code-nick-python',
    author_email='2330458484@qq.com',
    url="https://github.com/code-nick-python/awesome-python-tools/tree/master/pyinstaller_all",
    license='Apache2.0 License',
    packages=find_packages(),
    platforms="any",
    py_modules=['quickpack'],
    install_requires=[
        'colorama',
        'pyinstaller',
    ],
    classifiers={
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    },
    entry_points={
        'console_scripts': [
            'pack = quickpack:pyinstaller_main',
        ],
    }
)
