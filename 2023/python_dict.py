global my_dict
my_dict = {}

def add_dict(id, name, age, location):
    my_dict['id'] = id
    my_dict['name'] = name
    my_dict['age'] = age
    my_dict['location'] = location

def show():
    print(my_dict)

while True:
    print(" \n \n1. add data\n2. show data\n3. delete data\n4. Exit\n")

    choice = int(input("Enter your choice :"))
    if choice == 1:
        id = input("Enter your id: ")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        location = input("Enter your location: ")
        add_dict(id, name, age, location)
    elif choice == 2:
        show()
    elif choice == 3:
        my_dict.clear()
        print("Data deleted.")
    elif choice ==4:
        break

        
