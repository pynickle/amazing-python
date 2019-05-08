x = int(input('please enter a year:'))
if x % 4 == 0 and x % 100 != 0:
	print(str(x)+'年是闰年')
elif x % 400 == 0:
	print(str(x)+"年是闰年")
else:
	print(str(x)+"年不是闰年")
