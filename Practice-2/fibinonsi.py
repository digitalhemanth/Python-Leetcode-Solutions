def solution(n):
    p = 5
    count = 0 
    while p<=n:
        count = count + (n/p)
        p = p*5
    return round(count)

print(solution(30))



def solution_1(n):
    if n==0:
        return 1
    else:
        return n*solution_1(n-1)
res = solution_1(30)
print(res)



PS D:\Code_Place\2_test> python .\fibinonsi.py    
7
265252859812191058636308480000000

