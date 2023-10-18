fruits = ["apple", "Banana", "orange", "melon"]

# print("apple" in fruits)
# print("lemon" in fruits)
# print("peace" not in fruits)
#
# print("w" in "hello world")

# challenge

fruits = ["apple", "Banana", "orange", "melon"]
text = "What fruits do you like?"

favorite_fruits = input(text)

if favorite_fruits in fruits:
    print(f"{favorite_fruits}?\nI'll give it to you.")
    fruits.remove(favorite_fruits)
    print("Here are fruits I have now.\n{}".format(fruits))

else:
    print(f"{favorite_fruits}?\nI'll stock it.")
    print("Here are fruits I have now.\n{}".format(fruits))
    fruits.append(favorite_fruits)
