def solution(x,group,low,high):
    while low <= high:
        mid = low + (high-low)//2
        if group[mid]==x:
            print(x)
            print("element is found")
            break
        elif mid < low:
             low  = mid+1
        else:
            high = mid-1
    else:
        print("element not found !")
    
        
group = [6,8,9,7,4,3]

group = sorted(group)
print(group)
low = 0
high = len(group)+1
x = 4
solution(x,group,low,high)

