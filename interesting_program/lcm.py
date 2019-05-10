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

num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print("The least common multiple of " + str(num1) + " and " + str(num2) + " is " + lcm(num1,num2))
