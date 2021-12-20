class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
                    
    def inserssion(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def ins_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next=new_node
    
    def inset_any(self,data,x):
        print(x)
        n = self.head
        while n is not None:
            if x == n.data:
               break
            n = n.next
        if n is None:
            print("The element is not found in the Linked list")
        else:    
            new_node = Node(data)       
            new_node.next = n.next
            n.next = new_node
            
    def add_before(self,data,x):
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n is not None:
            if x == n.next.data:   
                break
            n = n.next
        if n is None:
            print(" Sorry the Element is Not found")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node     
             
    def show(self):
        n = self.head
        if n is None:
            print("Liked list is Empty : ")
        while n is not None:
            print(n.data, end='-> ')
            n = n.next
    
    def remove_s(self):
        if self.head is None:
            print("Sorry there is No nodes present here !")
        else:
            self.head = self.head.next
    
    def del_end(self):
        if self.head is None:
            print("Sorry there is No nodes present here !")
        elif self.head.next is None:
            self.head = None
        else:
            try:
                n = self.head
                while n.next.next is not None:
                    n = n.next
                n.next = None
            except:
                print("seems you have only one node")
                
    def del_item(self,x):
        if self.head.data == x:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        try: 
            if n is not None:
               n.next = n.next.next
        except:
            print("Sorry the element is not found ")
           
        
        
#obj = Node('A')

cobj = linked_list()
cobj.inserssion('B')
cobj.inserssion('A')
cobj.ins_end('H')
cobj.inset_any('S','V')
cobj.inset_any('S','B')
cobj.add_before('L','B')
cobj.show()

#print("\n")
#cobj.remove_s()
#cobj.show()
#print("\n")
#cobj.del_end()
#cobj.show()
print("\n")
cobj.del_item('K')
cobj.show()
print("\n")
cobj.del_item('B')
cobj.show()
#print(obj.data)
#print(obj.next)
        