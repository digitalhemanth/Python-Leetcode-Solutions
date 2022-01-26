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

#Count the number of occurrences of a character in a string
name = 'hemanth'
res = name.count('h')
print(res)


# Find the missing number in a given list
arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
# get the array's length
n = len(arr)

# actual size is `n+1` since a number is missing from the list
m = n + 1

# get a sum of integers between 1 and `n+1`
total = m * (m + 1) // 2

# the missing number is the difference between the expected sum and
# the actual sum of integers in the list
res = total - sum(arr)

print(res)