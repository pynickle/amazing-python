import calendar

year = int(input("enter the year : "))
month = int(input("enter the month : "))

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

print("itertools.combinations('1234', 2) : " + str(list(itertools.combinations("1234", 2))))
