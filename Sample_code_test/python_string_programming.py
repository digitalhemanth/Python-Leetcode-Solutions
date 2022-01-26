#1. Python Program to Reverse a Strintg 

def strings(word):
    tmp =''
    for i in word:
        tmp = i+tmp
    return tmp

print(strings('hem'))

#2. Python Program to Reverse a Strintg 

word = 'malayalam'
if word == word[::-1]:
    print(word)
else:
    print('Not a palindrom')
    
#remove a spesific charachter from string 
name = 'Hemanth'

res = name.replace('n','')

print(res)