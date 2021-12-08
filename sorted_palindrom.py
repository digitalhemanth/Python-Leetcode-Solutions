def ESolustion(s : str) -> str:
 
   
    def helper(l,r):
        while(l>=0 and r<len(s) and s[l]==s[r]):
                l -= 1
                r += 1
                print(s[l+1:r], end = " ")
        return s[l+1:r]
    
    res = ''
    load= []
    
    for i in range(len(s)):
        test = helper(i,i)
        if len(test)>len(res) :
            res = test 
            load.append(res)     
        test = helper(i,i+1)
        if len(test)>len(res) : 
            res = test 
            load.append(res) 
    
   
    return res,load
