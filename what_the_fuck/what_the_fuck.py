"""
Don't let return and finally meet!
Really terrible!
"""
def return_and_finally():
    try:
        return 'from_try'
    finally:
        return 'from_finally'
        
print(return_and_finally())
"""
You will surprising find from_finally on the screen!
How can that happen!
Actually,when break, continue or return in try sentence, and exactly there is a finally sentence...
It will run finally first!
"""



"""
l thought l would see two True on the screen...
"""
print('what' * 5 is "whatwhatwhatwhatwhat")
print('what' * 6 is "whatwhatwhatwhatwhatwhat")
"""
But actually...
One True and One False
How can that happan!
eee...Because of the existance of constant folding...
a powerful technology...
constant folding in python will convert a string with less than twenty characters.
But if the string has more than two characters, python will not convert it.
Think about pyc's feeling!
"""



"""
If the first two is correct...
It seems like all the sentences below can run correctly...
"""
print('right?''')
print("right?""")
#print('''right?')
#print("""right?")
"""
But actually not!It will cause a Syntax Error.
You can use three double quotes or three single quotes to end a string.
But if the scanner first get three double quotes or single,it will try to find another.
If there is not another,it will raise a Syntax Error.Surprising?Yes?
"""
