def solution(arr):
    for i in range(len(arr)):
        minval = min(arr[i:])
        ind = arr.index(minval)
        arr[i],arr[ind]=arr[ind],arr[i]
    return arr

arr = [9,3,7,0,4,6,1]
print(arr)
size = len(arr)
print(solution(arr))
   
