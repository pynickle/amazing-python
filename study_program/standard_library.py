import calendar

year = 2019
month = 5

print(f"year : {year} , month : {month}")
print(calendar.month(year,month))



import pprint
data = (
	    "string1",
	    ("first", "second", "third"),
		{"hello":"python3", "bye":"python2"},
	    "string2"
    ) 
print("pprint.pprint : ")
pprint.pprint(data)
print()

print("print : ")
print(data)



import itertools
def run_itertools(func):
    counter=0
    for i in func:
	    print(i)
	    if counter==9:
		    break
	    counter += 1
print("list(itertools.repeat(10, 3)) : " + str(list(itertools.repeat(10, 3))) + "\n")

print("itertools.cycle('Hello') : ")
cycle=itertools.cycle("Hello")
run_itertools(cycle)
print()

print("itertools.count(10) : ")
count = itertools.count(10)
run_itertools(count)
print()

print("itertools.combinations('1234', 2) : " + str(list(itertools.combinations("1234", 2))) + "\n")



import time
print("time now : " + time.strftime("%Y-%m-%d %H:%M:%S"))

start=time.time()
time.sleep(1)
end=time.time()
print("it takes " + str(end-start))



import timeit

string=["a very very long long string" for i in range(1000)]

def join_test():
	return "".join(string)

def plus_test():
	result=""
	for i in string:
	    result+=i
	return result

times=1000
#jointimer=timeit.Timer("join_test()","from __main__ import join_test")
#plustimer=timeit.Timer("plus_test()","from __main__ import plus_test")
	
print("join : {}".format(timeit.timeit("""
string=['a very very long long string' for i in range(1000)]
result=''.join(string)
""", number=times)))
print("plus : {}".format(timeit.timeit("""
string=['a very very long long string' for i in range(1000)]
result='';
for i in string:
	result+=i
""", number=times)))
print()



import sys
print("version : " + sys.version + "\n")
print("path : ")
pprint.pprint(sys.path)
print()
print("getfilesystemencoding : " + sys.getfilesystemencoding() + "\n")
print("platform : " + sys.platform + "\n")



import dis

def lcm(num1:int, num2:int)->str:
	if num1 > num2:
		counter = num1
	else:
		counter = num2

	while True:
		if counter % num1 == 0 and counter % num2 == 0:
			lcm = counter
			break
		counter += 1
	return str(lcm)


dis.dis("lcm(1,100)")



import re
def print_re(result):
	print(result)
	if result==None:
		return
	elif isinstance(result,list):
		return
	else:
		try:
			print(result.span())
		except:
			pass
		try:
			print(result.groups())
		except:
			pass

pattern1 = "ll"
pattern2 = "j"
string1 = "hello ll"
string2 = "ll hello"
string3 = "17 jh 2h"
string4 = "JY 1768 jh"
compile_pattern1 = re.compile(r"\D")

result1 = re.search(pattern1, string1)

result2 = re.match(pattern1, string1)
result3 = re.match(pattern1, string2)

result4 = re.findall(pattern1, string1)
result5 = re.findall(pattern1, string2)

result6 = compile_pattern1.findall(string3)

result7 = re.split('\W+', string3) 
result8 = re.split('\W+', string3, 1)

result9 = re.findall(pattern=pattern2, string=string4, flags=re.I)

for i in range(1,10):
	print("result" + str(i))
	exec("print_re(result" + str(i) + ")")
	print()

	
	
import gc

a = ["a"]
b = ["b"]
a.append(b)
b.append(a)
sys.getrefcount(a)    
sys.getrefcount(b)    
del a
del b
try:
    sys.getrefcount(a)
except Exception as e:
	print(e)
print(gc.collect())



import functools

reduce_lst=[1,2,3,4,5]
def add(x, y):
	return x + y
print(functools.reduce(lambda x,y:x + y, reduce_lst))
print(functools.reduce(add, reduce_lst, 5))

@functools.lru_cache(None)
def fibonacci(n):
	if n < 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(5):
	print(fibonacci(i))
	
	
	
import ast

print(ast.parse("def hello():print('Hello world')"))
ast_tree=ast.parse("def hello():print('Hello world')")
ast_dump=ast.dump(ast_tree).replace('(','(\n\t')
print(ast_dump)
				
print(ast.literal_eval("1+2"))
try:
	  ast.literal_eval("__import__('os').system('dir')")
except:
	  print("ast.literal_eval is safe than eval")

      
      
import asyncio
async def print_num(num):
    print(num)

loop=asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.wait([
        print_num(num)
        for num in range(10)
    ])
)



from enum import Enum, auto
class EnumTest(Enum):
    first = 6 
    second = auto()
    third = "hello"

    
for i in EnumTest:
	print(str(i) + " : " + str(i.value))

	
	
from dataclasses import dataclass
@dataclass
class dataklass:
    name:str
    def hello(self):
        print("hello " + self.name)
a=dataklass('nick')
print(a.name)
a.hello()
print(a)



import keyword
print(keyword.kwlist)



import glob
print(glob.glob('*.py'))



import logging
FORMATLOG = "[%(asctime)s] %(filename)s . %(funcName)s . %(name)s : %(levelname)s : %(message)s"
def logger1():
    logging.basicConfig(
        level=logging.DEBUG,
        format=FORMATLOG
    )

    logging.debug('debug')
    logging.info('info')
    logging.warn('warn')
    logging.error('error')
    logging.critical('critical')


def logger2():
    logger = logging.getLogger('foo')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(FORMATLOG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug('debug without BasicConfig')

logger1()
logger2()



import traceback
def wrong():
	print("l am a wrong sentence!" + 1)

try:
	wrong()
except Exception as e:
	traceback.print_exc()
