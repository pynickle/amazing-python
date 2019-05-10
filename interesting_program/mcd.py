def mcd(num1:int, num2:int)->str:
	if num1 > num2:
		counter = num2
	else:
		counter = num1
	for i in range(1,counter + 1):
		if((num1 % i == 0) and (num2 % i == 0)):
			mcd = i
		
	return str(mcd)
 
num1 = int(input("enter the first nunber : "))
num2 = int(input("enter the second number : "))

print("The maximum common divisor of " + str(num1) + " and " + str(num2) + " is " + mcd(num1, num2))
