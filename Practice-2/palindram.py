'''
 

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
    
PS D:\Code_Place\2_test> python .\palindram.py
Please enter a string : malayalam
 yes it palindrom

'''
   
'''
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

PS D:\Code_Place\2_test> python .\palindram.py
Please eneter any word malayalam
m malayalam a ala alayala l layal a aya y a ala l a m 15


def solution(string):
    N = len(string)
    maxword = ''
    maxcount = 0
    for i in range(N):
        for j in range(i+1,N+1):
            tmp = string[i:j]
            if tmp == tmp[::-1]:
                if len(tmp) > maxcount:
                    maxcount = len(tmp)
                    maxword = tmp
               
    return maxword

string = input("Please eneter any word ").lower()
print(solution(string))

PS D:\Code_Place\2_test> python .\palindram.py
Please eneter any word hemmalayalamheh
malayalam
PS D:\Code_Place\2_test> 

'''
def solution(string):
    N = len(string)
    strings = set()
    
    for id , word in enumerate(string):
        start , end = id-1, id+1
        while start >=0 and  end < N and string[start]==string[end]:
            strings.add(string[start:end+1])      
            start -=1
            end +=1
            
        start , end = id, id+1
        while start >=0 and  end < N and string[start]==string[end]:
            strings.add(string[start:end+1])      
            start -=1
            end +=1    
  
    return strings
string = input("Please eneter any word ").lower()
print(solution(string))

PS D:\Code_Place\2_test> python .\palindram.py
Please eneter any word malayalamgoog
{'oo', 'alayala', 'goog', 'layal', 'malayalam', 'ala', 'aya'}

