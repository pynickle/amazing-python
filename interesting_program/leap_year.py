x = int(input('please enter a year:'))
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
	print(True)
else:
	print(False)
