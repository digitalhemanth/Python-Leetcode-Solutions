#insertion sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        print(arr)
        print('working on ', arr[i])
        ele = arr[i]
        j = i-1
        while j >=0 and arr[j] > ele:
           arr[j+1] = arr[j]
           j -= 1
        arr[j+1] = ele 
        print(f'{arr} \n')
    return arr       
 
arr = [5, 2, 4, 6, 1, 3]
print('\n',insertion_sort(arr))