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
    

print(BibarySerch([2,4,6,8,12,14], 8))