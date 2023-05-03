class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        print(f"Added {data} to the list.")

    def delete_node(self, data):
        current_node = self.head
        if current_node is not None and current_node.data == data:
            self.head = current_node.next
            current_node = None
            print(f"Deleted {data} from the list.")
            return
        while current_node is not None:
            if current_node.data == data:
                break
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            print(f"{data} not found in the list.")
            return
        prev_node.next = current_node.next
        current_node = None
        print(f"Deleted {data} from the list.")

    def show_list(self):
        if self.head is None:
            print("The list is empty.")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def count_nodes(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        print(f"The list has {count} nodes.")


if __name__ == '__main__':
    linked_list = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Add node")
        print("2. Delete node")
        print("3. Show list")
        print("4. Count nodes")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data: "))
            linked_list.add_node(data)
        elif choice == 2:
            data = int(input("Enter data to be deleted: "))
            linked_list.delete_node(data)
        elif choice == 3:
            linked_list.show_list()
        elif choice == 4:
            linked_list.count_nodes()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")
