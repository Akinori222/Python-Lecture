class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        print(f"{self.name} is walking.")

    def run(self):
        print(f"{self.name} is running.")


john = Person("John", 15, "male")
emma = Person("Emma", 25, "Female")
steve = Person("Steve", 35, "male")

print(john)
print(f"変更前:John is {john.age} years old.")
john.age = 29
print(f"変更後:John is {john.age} years old.")

# インスタンスメソッド
john.walk()
emma.walk()
john.run()


