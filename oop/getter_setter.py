class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age  # getter,setterを使うインスタンス変数はノンパブリックな変数として定義する

    def get_age(self):
        print("get_age called.")
        return self._age

    def set_age(self, age):
        print("set_age called.")
        if age < 0:
            print("Please enter a value greater than or equal to 0.")
        else:
            self._age = age

    age = property(get_age, set_age)


aki = Person("aki", 32)
# print(aki.name)
# print(aki.get_age())
# # print(aki.get_age(20))
# aki.set_age(10)
# print(aki._age)
print(aki.age)
aki.age = -10