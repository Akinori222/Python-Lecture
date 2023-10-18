# getter setter

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self, age):
        self._age = age


aki = Person("aki", 32)
print(aki.age)
