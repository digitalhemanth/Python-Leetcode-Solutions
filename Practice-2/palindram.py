"""

def solution(word):
    res = ''
    for i in word:
          res = i+res
    return res
        
word = input("Please enter a string : ").lower()

out = solution(word)
if out==word:
    print(" yes it palindrom")
else:
    print("sorry its not an pallindrom ")
    
"""

def solution(string):
    N = len(string)
    count = 0
    for i in range(N):
        for j in range(i+1,N+1):
            tmp = string[i:j]
            if tmp == tmp[::-1]:
                print(tmp, end=' ')
                count += 1
    return count

string = input("Please eneter any word ").lower()
print(solution(string))

'''
PS D:\Code_Place\2_test> python .\palindram.py
Please eneter any word racesar
r a c e s a r 7
PS D:\Code_Place\2_test> python .\palindram.py
Please eneter any word tmp
t m p 3
PS D:\Code_Place\2_test> python .\palindram.pyPlease eneter any word tmmpt m mm m p 5
PS D:\Code_Place\2_test>    
'''