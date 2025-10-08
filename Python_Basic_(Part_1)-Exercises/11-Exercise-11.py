# 11.Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.
#######################################################################################################################

# eval : eval() is a built-in Python function that takes a string and executes it as a Python expression, then returns the result.
# eval() lets you turn a string into live Python code.

func= eval(input("Enter the Python Function Name to get docstring of it :  "))

det = func.__doc__
print(det)



