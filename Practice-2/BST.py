class BST:
    def __init__(self,key):
        self.key = key
        self.lnode = None
        self.rnode = None
        
    def insert(self,data):
        if self.key is None:
            self.key = BST(data)
            return
        if self.key > data:
            if self.lnode:
               self.lnode.insert(data)
            else:
                self.lnode = BST(data)
        else:
            if self.rnode:
                self.rnode.insert(data)
            else:
                self.rnode = BST(data)
                
    def show(self):
        print(self.key, end= ' ')
        if self.lnode:
            self.lnode.show()
        if self.rnode:
            self.rnode.show()
            
                
    def inshow(self):
        if self.lnode:
            self.lnode.show()
        print(self.key, end= ' ')
        if self.rnode:
            self.rnode.show()
                
    def postshow(self):
        if self.lnode:
            self.lnode.show()
        if self.rnode:
            self.rnode.show()
        print(self.key, end= ' ')            
    
    def search(self,x):
        if self.key is None:
            print("Sorry binary serch tree is empty !")
            return 
        if self.key == x:
            print(x, ' is found !')
            return
        if self.key > x:
            if self.lnode:
               self.lnode.search(x)
            else:
                print("sorry the element is not found")
        else:
            if self.rnode:
               self.rnode.search(x)
            else:
                print("sorry the element is not found")
            
            
                
root = BST(2)
print(root.key)

tree = [6,8,3,4,1,0,7,9]

for i in tree:
    root.insert(i)

print('\n Pre Order : ')
root.show()

print('\n IN Order : ')
root.inshow()

print('\n Post Order : ')
root.postshow()

print('\n Search X : ')
root.search(5)

print('\n Search X : ')
root.search(4)


