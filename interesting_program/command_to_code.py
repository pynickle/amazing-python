def replace_command_to_code(str):
	lst=str.split('\n')
	result=''
	for i in lst:
		if i.startswith(">>> "):
			i=i.replace('>>> ','')
		elif i.startswith("... "):
			i=i.replace('... ','')
		elif i=='...':
			i=''
		elif i=='>>>':
			i=''
		result=result+i+'\n'
	return result
