#1. Python Program to Reverse a Strintg 

def strings(word):
    tmp =''
    for i in word:
        tmp = i+tmp
    return tmp

print(strings('hem'))

