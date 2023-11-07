def main():
    print("This program converts US dollars to Pounds Sterling")
    print()
    dollars = eval(input("Enter amount in dollars: "))
    pounds = convert_to_pounds(dollars)
    print("That is", pounds, "pounds. ")


convert_to_pounds = lambda dollars: dollars * 0.82
# what does lambda is doing here  
# In the given code, lambda is used to define an anonymous function in Python. The lambda function takes the parameter dollars and multiplies it by 0.82, returning the result. This lambda function is assigned to the variable convert_to_pounds.
# here in convert_to_pounds in this variable we defined a variable and an operation with that , so that means whenever we call the function and give it an argument then it becomes assigned to the vaiable  we defined in that so an the operation takes place and finally we the result assigned to the convert_to_pounds . that'is how it works . 

main()
# in python we need to call a function to execute it.
# The eval() function is used for dynamically evaluating Python code from strings.

# Reading the type of value passing through eval():
# To determine the type of value that is being passed through the eval() function, you need to understand how the function is used in the context of your code. The parameter names provided (__source, __globals, __locals) give you hints about the kind of values they expect.

# For example, if you're using eval() to execute a specific expression, you can look at the string you're passing as __source to understand what kind of code will be evaluated. If you're using the __globals or __locals parameters, you can examine the dictionaries you're passing to see what variables or values are available to the code being evaluated.

# Additionally, you can use Python's built-in type() function to explicitly determine the type of any variable or value you're passing to eval(). For instance:
source_code = "2 + 3"
result = eval(source_code)
print(type(source_code))  # <class 'str'>
print(type(result))       # <class 'int'>

