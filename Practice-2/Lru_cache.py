class Lru_cache:
    def __init__(self,limit:int):
        self.limit = limit
        self.obj = {}
        
    def access(self,key):
       if key not in self.obj:
           return "Key not found"
       else:
           val = self.obj.pop(key)
           self.obj[key]=val
           return val
       
    def create(self,key,val):
       if key in self.obj:
           print("Object alreday in cache !")
           val = self.obj.pop(key)
           self.obj[key] = val
           return val  
       else:
           if len(self.obj)==self.limit:
               del self.obj[next(iter(self.obj))]   
           self.obj[key] = val
    
    def show(self):
        if self.obj is not None:      
            print(self.obj.items())     
           
lru = Lru_cache(3)

lru.create('A','HEMANTH')
lru.create('B','HEM')
lru.create('E','HEM')

print(lru.access('A'))
print(lru.access('L'))

lru.create('N','LOH')

lru.create('A','HEMANTH')

lru.create(2,'H')

lru.show()



PS D:\Code_Place\2_test> python .\Lru_cache.py
HEMANTH
Key not found
Object alreday in cache !
dict_items([('E', 'HEM'), ('N', 'LOH'), ('A', 'HEMANTH')])
PS D:\Code_Place\2_test> python .\Lru_cache.py

