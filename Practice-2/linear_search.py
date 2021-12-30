def solution(arr,x):
    for i in range(len(arr)):
        try : 
             if x==arr[i]:
               print('element found')
               break 
        except:
            print("sorry the element is not found")
       
    

arr = [9,3,7,0,4,6,1]
print(arr)
size = len(arr)
x = 1
solution(arr,x)

print("O(n)")


PS D:\Code_Place\2_test> python .\linear_search.py
[9, 3, 7, 0, 4, 6, 1]
element found
O(n)