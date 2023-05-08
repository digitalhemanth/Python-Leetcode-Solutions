# ambda function in Python, often called a lambda expression or anonymous function. In Python, a lambda function is a way to create small, anonymous functions without using the def keyword.


# lambda arguments: expression
#

a = lambda x,y : x/y
print(a(8,2))


# In Python, args and kwargs are commonly used to handle variable-length arguments in functions.

# args stands for "arguments" and is used to pass a variable number of non-keyword arguments to a function. It allows you to pass an arbitrary number of positional arguments, which are then accessible as a tuple within the function.


def print_arguments(*args):
    for arg in args:
        print(arg)

print_arguments('apple', 'banana', 'cherry')


# kwargs stands for "keyword arguments" and allows you to pass a variable number of keyword arguments to a function. It enables you to pass arguments as key-value pairs, and the function receives them as a dictionary.

