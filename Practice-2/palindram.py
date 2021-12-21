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