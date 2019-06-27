def get_mcd(num1:int, num2:int)->str:
	mcd = 0
	if num1 > num2:
		counter = num2
	else:
		counter = num1
	for i in range(1,counter + 1):
		if((num1 % i == 0) and (num2 % i == 0)):
			mcd = i
		
	return str(mcd)
 
num1 = int(input())
num2 = int(input())

print(get_mcd(num1,num2))
