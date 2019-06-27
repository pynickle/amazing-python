def get_lcm(num1:int, num2:int)->str:
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

num1 = int(input())
num2 = int(input())

print(get_lcm(num1,num2))

