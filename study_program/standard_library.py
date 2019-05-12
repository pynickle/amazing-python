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
jointimer=timeit.Timer("join_test()","from __main__ import join_test")
plustimer=timeit.Timer("plus_test()","from __main__ import plus_test")
	
print("join : {}".format(jointimer.timeit(number=times)))
print("plus : {}".format(plustimer.timeit(number=times)))
