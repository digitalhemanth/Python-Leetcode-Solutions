'''
Python Errors and Built-in Exceptions
These errors can be broadly classified into two classes:
1.	Syntax errors
2.	Logical errors (Exceptions)

Python Syntax Errors
Error caused by not following the proper structure (syntax) of the language is called syntax error or parsing error.

Python Logical Errors (Exceptions)
Errors that occur at runtime (after passing the syntax test) are called exceptions or logical errors.
'''

#KeyboardInterrupt:	Raised when the user presses Ctrl+c, Ctrl+z or Delete
#ImportError : Raised when an imported module does not exist
#MemoryError	Raised when a program runs out of memory
#NameError	Raised when a variable does not exist
#OverflowError	Raised when the result of a numeric calculation is too large
#ZeroDivisionError	Raised when the second operator in a division is zero
#TypeError	Raised when two different types are combined


try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass


raise KeyboardInterrupt
'''
Traceback (most recent call last):
KeyboardInterrupt
raise MemoryError("This is an argument")
Traceback (most recent call last):
MemoryError: This is an argument
'''
try:
     a = int(input("Enter a positive integer: "))
     if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
     print(ve)
    
#Enter a positive integer: -2
#That is not a positive number!


# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
    
    
try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
   
   
   
# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


