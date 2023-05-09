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