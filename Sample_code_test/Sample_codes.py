'''
str1 = input("Enter Str 1")
str2 = input("Enter Str 2")

if sorted(str1)==sorted(str2):
    print("Stings are Anagram!")
'''

strings = []
inputs = input("Please enter list of strings: \n").lower()
strings = inputs.split()
print(strings)

anagramse={}

for word in strings:
    sorted_str = str(sorted(word))
    if sorted_str in anagramse:
        anagramse[sorted_str].append(word)
    else:
        anagramse[sorted_str] = [word]

print(list(anagramse.values()))

-------------------------------------------------------------------------------------------
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
    

