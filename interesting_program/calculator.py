symbol=("+","-","*","/","//","**","(",")","1","2","3","4","5","6","7","8","9","0")
question=input(">>>")
legal=True
for i in question:
	if i not in symbol and legal:
		print("illegal!")
		legal=False
if legal:
	try:
		print(eval(question))
	except:
		print("illegal!")
