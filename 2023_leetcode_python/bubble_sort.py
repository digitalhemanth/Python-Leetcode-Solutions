def bubblesort(arry):
    for a in range(len(arry)):
        for i in range(0, len(arry)-1):
            if arry[i] > arry[i+1]:
                arry[i] , arry[i+1] = arry[i+1], arry[i]
        print(arry) 
      
    return arry    
                        
arry = [2,8,4,1,-6]
bubblesort(arry)