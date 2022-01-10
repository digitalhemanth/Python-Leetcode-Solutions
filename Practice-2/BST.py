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
            
            
                
root = BST(2)
print(root.key)

tree = [6,8,3,4,1,0,7,9]

for i in tree:
    root.insert(i)

print('Pre Order : ')
root.show()