def BibarySerch(Arryas, target):
    left = 0
    right = len(Arryas)-1
    
   
    while left <= right :
        middle = (left + right) //2
        mid_ele =  Arryas[middle]
        # print(mid_ele)
        
        if mid_ele == target:
            return middle
        elif mid_ele > target:
            right = middle - 1
        else :
            left = middle + 1

    return "element not found"
    

print(BibarySerch([2,4,6,8,12,14], 5))





"""
    The time complexity of the binary search algorithm implemented in the provided code is O(log N), where N is the number of elements in the array. This is because the search space is halved in each iteration of the while loop, leading to a logarithmic time complexity.

The space complexity of the code is O(1) because it uses a constant amount of additional memory. The variables left, right, middle, and mid_ele require a constant amount of space, regardless of the size of the input array.

In summary:

Time complexity: O(log N)
Space complexity: O(1)

"""