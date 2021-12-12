class Node:
    def __init__(self,data):
        self.data = data
        self.lref = None
        self.rref = None
        
obj = Node('A')

print(obj.data)
print(obj.lref)
print(obj.rref)
        