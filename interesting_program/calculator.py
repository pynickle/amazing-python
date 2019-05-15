symbol1 = ("+", "-", "*", "/", "//", "**", "(", ")")
symbol2 = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
question=input(">>>")
legal=True
split_eval=""
test=""
point=False

for i in question:
	if i in symbol1:
		if not point:
			split_eval += str(float(int(test)))
			test=""
			split_eval += i
		else:
			split_eval += test
			test=""
			split_eval += i
	elif i in symbol2:
		test += i
	elif i == ".":
		point = True
		test += i
	if i not in symbol1 and i not in symbol2 and legal and i != ".":
		print(i + " illegal!")
		legal=False

split_eval += str(float(int(test)))
		
if legal:
	try:
		print(split_eval + " = " + str(eval(split_eval)))
	except Exception as e:
		print(e)
		print("illegal!")
