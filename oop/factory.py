import time


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))  # True=1, False=0
        # if (today.tm_mon, today.tm_mday) < (month, date):
        #     age = today.tm_year - year - 1
        # else:
        #     age = today.tm_year - year
        return cls(name=name, age=age)


aki = Person("aki", "32")
mitu = Person.create_from_dob("mitu", 2001, 1, 29)
print(aki.age)
print(mitu.name)
print(mitu.age)
print(type(aki))
print(type(mitu))
