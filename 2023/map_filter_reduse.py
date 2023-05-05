#map() : The map() function takes a function and an iterable as arguments, and applies the function to each element of the iterable,
# returning an iterator with the results.

def square(x):
    result = x**2
    print(f"Square of {x} is {result}")
    return result

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)
print(list(squares))


# filter()
# The filter() function takes a function and an iterable as arguments, and returns an iterator with the elements of the iterable for which the function returns True.


# reduce()
# The reduce() function takes a function and an iterable as arguments, and applies the function to the first two elements of the iterable, 
# then to the result and the next element, and so on, until a single value is returned.


from functools import reduce

def multiply(x, y):
    result = x * y
    print(f"Multiplying {x} and {y} to get {result}")
    return result

numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)
print("Final product:", product)
