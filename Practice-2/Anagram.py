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


PS D:\Code_Place\2_test> python .\Anagram.py
Please enter list of strings: 
hes she dog god moon nomo hemanth hem mhe 
['hes', 'she', 'dog', 'god', 'moon', 'nomo', 'hemanth', 'hem', 'mhe']
[['hes', 'she'], ['dog', 'god'], ['moon', 'nomo'], ['hemanth'], ['hem', 'mhe']]
PS D:\Code_Place\2_test> 
