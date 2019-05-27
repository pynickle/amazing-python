import time
def time_c(func):
	def wrapper(*args, **kwargs):
		#start = time.perf_counter()
		start = time.time()
		func(*args, **kwargs)
		#elapsed = (time.perf_counter() - start)
		elapsed = (time.time() - start)
		print("{} : Time used: {}".format(func.__name__, elapsed))
	return wrapper
def check_first(number:int):
	if number < 2:
		return False
	elif number == 2:
		return True
	return all([number % i for i in range(2, number)])

def check_second(number:int):
	if number < 2:
		return False
	elif number == 2:
		return True
	for i in range(2,number//2+1):
		if number%i==0:
			return False
	return True
num = 7567

@time_c
def first_test():
	print(check_first(num))
	
@time_c
def second_test():
	print(check_second(num))
first_test()
second_test()

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
