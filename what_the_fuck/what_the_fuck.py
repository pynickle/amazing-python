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
