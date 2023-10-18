class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age  # getter,setterを使うインスタンス変数はノンパブリックな変数として定義する

    @property
    def age(self):
        print("get_age called.")
        return self._age

    @age.setter
    def age(self, age):
        print("set_age called.")
        if age < 0:
            print("Please enter a value greater than or equal to 0.")
        else:
            self._age = age

    # age = property(get_age, set_age)

aki = Person("aki", 32)
aki.age = -100
print(aki.age)
