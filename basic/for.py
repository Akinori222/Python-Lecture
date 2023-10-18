# for リストの要素をループ

fruits = ["apple", "Banana", "orange", "melon"]

# for fruit in fruits:  # ループで回す ⇨ iteration (iterationができるオブジェクト ⇨ iterable)
#     print(f"I love {fruit}!!")
#
# for char in "Hello world":
#     print(f"cher:{char}")

# challenge1
# favorite_fruits = input("What fruits do you like\n")

# for fruit in fruits:
#     if fruit == favorite_fruits:
#         print(f"I love {fruit}")
#     else:
#         print(f"I don't love {fruit}")

# challenge2
favorite_fruits = []
normal_fruits = []

for fruit in fruits:
    answer = input(f"""Do you like {fruit}? y/n
""")
    if answer == "y":
        favorite_fruits.append(fruit)
    else:
        normal_fruits.append(fruit)

print(f"Your favorite fruits: {favorite_fruits}.")
print(f"Other than that: {normal_fruits}")