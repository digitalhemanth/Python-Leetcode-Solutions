class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class dlinked_list:
    def __init__(self):
        self.head = None
                
    def show(self):
        if self.head is None:
            print(" D linked list is Empty ")
        else:
            n = self.head
            while n is not None:
              print(n.data, end='-> ')
              n = n.nref
              
              
    def revshow(self):
        print("\n")
        if self.head is None:
            print(" D linked list is empty !")
        else:
            while self.head.nref is not None:
                self.head = self.head.nref
            while self.head is not None:
                print(self.head.data,end=' <- ')
                self.head = self.head.pref
                
    def binsert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node               
    
    def einsert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            print(n)
            n.nref = new_node
            new_node.pref = n
            
    def add_before(self,data,x):
        if self.head is None:
            print("List Is empty")    
        else: 
             n = self.head
             while n is not None:
                 if n.data==x:
                    break
                 n = n.nref
             if n is None:
                 print("Eleemnt is not found")
             else:
                 new_node = Node(data)
                 new_node.nref = n
                 new_node.pref = n.pref
                 if n.pref is not None:
                     n.pref.nref = new_node
                 else:
                     self.head = new_node
                 n.pref = new_node
                 
    def add_after(self,data,x):
        if self.head is None:
            print("List Is empty")    
        else: 
             n = self.head
             while n.nref is not None:
                 if n.data==x:
                    break
                 n = n.nref
             if n is None:
                 print("Eleemnt is not found")
             else:
                 new_node = Node(data)
                 new_node.nref = n.nref
                 new_node.pref = n
                 if n.nref is not None:
                     n.nref.pref = new_node
                 else:
                     self.head = new_node
                 n.nref = new_node
            
        
            
obj = dlinked_list()
obj.binsert('A')
obj.binsert('B')
obj.einsert('C')
obj.add_before('P','B')
obj.add_after('S','B')

obj.show()

obj.revshow()


#print(obj.data)
#print(obj.lref)
#print(obj.rref)
        