class Dog() :
    """说明"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " sit!")

    def bark(self):
        print(self.name + " bark")


my_dog = Dog("diandian", 11)
print(my_dog.name)
my_dog.sit()