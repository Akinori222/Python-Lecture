fruits = {"apple": "red", "melon": "green", "lemon": "yellow"}

# if "peach" in fruits:
#     print(fruits["peach"])
# else:
#     print("the key is not found.")

# .get
fruit = input("Please choose a fruit\n")
print(fruits.get(fruit, "Nothing"))

# .update()
fruits2 = {"peach": "pink"}
fruits.update(fruits2)

print(fruits)
