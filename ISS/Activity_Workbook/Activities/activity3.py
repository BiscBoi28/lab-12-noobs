'''
Task: Understand decorator functions
'''

def decorator_function(original_function):
    def wrapper_function():
        print("Something before the actual function")
        original_function()
        print("Something after the actual function")
    return wrapper_function

@decorator_function
def fun():
    print("Hello world")
    
fun()

# NOTE: you do not need to understand how to code a decorator function
# NOTE: Just understand how it works