def main_code(macros):
    def say_hai():
        print("just called")
        macros()
        print("helow ms hemanth")
    return say_hai

@main_code
def helow():
    print("hey im from aditinal function")

helow()


#Itarators 

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item

# Usage:
my_list = [1, 2, 3]
my_iterator = MyIterator(my_list)
for item in my_iterator:
    print(item)


#genarators

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Usage:
even_gen = even_numbers(10)
for num in even_gen:
    print(num)
