def prime(lower:int,upper:int)->list:
	primes=[]
	for num in range(lower,upper + 1):
		if num > 1:
			for i in range(2,num):
				if num % i==0:
					break
			else:
				primes.append(num)
	return primes
    
lower = int(input("enter the lower number : "))
upper = int(input("enter the upper number : "))

print(prime(lower,upper))
