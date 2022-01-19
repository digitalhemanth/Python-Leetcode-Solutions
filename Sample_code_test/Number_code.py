#1. Python Program to Reverse a Number

def numres(num : int) -> int:
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10    
    
    return reversed_num

print(numres(12345))

'''
def strings(word):
    tmp =''
    for i in word:
        tmp = i+tmp
    return tmp

print(strings('hem'))

'''
