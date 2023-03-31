class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'hi {self.name}')
m = Student("Hemanth",28)
m.show()
        