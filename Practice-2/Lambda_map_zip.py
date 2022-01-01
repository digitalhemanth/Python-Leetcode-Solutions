#Lambda:
#Single one line function ,Anoymous function(no name),no def, no return

add = lambda a,b : print(a+b)
add(6,8)

#Map
#The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .

nums = [2,8,6,4]
def sqr(n):
     return n*n
output = list(map(sqr,nums))
print(output)

'''
Syntax: map(fun, iter)
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

'''

nums = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**x, nums))
print(square)


people = ["hemanth", "kumar", "Data Eng"]
up = list(map(lambda x: x.upper(), people))
print(up)

#Filter 

seq = [0, 1, 2, 3, 4, 5]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))



users = [
    {"username": 'samuel', "tweets": ["i love cake", "i am good"]},
    {"username": 'andy', "tweets": []},
    {"username": 'kumal', "tweets": ["India", "Python"]},
    {"username": 'sam', "tweets": []},
    {"username": 'lokesh', "tweets": ["i am good"]},
]

inactive_users = list(filter(lambda a:not a['tweets'], users))
print(inactive_users)

inactive_users=list(map(lambda x:x["username"].upper(),
                    filter(lambda a:not a['tweets'], users)))
print(inactive_users)


names=['lokesh','lassie','bob','to']
new=list(map(lambda name:f"your name is {name}",
        filter(lambda x:len(x)>4,names)))
print(new)


# Zip:
#The zip() function take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.


name = ["Manjeet", "Nikhil", "Shambhavi"]
marks = [40, 50, 60]

mapped = zip(name, marks)

print(dict(mapped))



