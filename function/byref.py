# 参照渡し(byref), 値渡し(byvalue)

# mutableな引数の場合
def add_num(a, b):
    print(f"before change:::a's ID:{id(a)}, b's ID:{id(b)}")
    a += b
    print(f"after change:::a's ID:{id(a)}, b's ID:{id(b)}")
    return a

one = 1
two = 2

print(f"before function call:::one's ID:{id(one)}, two's Id:{id(two)}")
add_num(one, two)


# immutableな引数の場合
def my_fruits(fruits, fruit):
    print(f"before change:{fruits}ID:{id(fruits)}")
    fruits.append(fruit)
    print(f"after change:{fruits}ID:{id(fruits)}")
    return fruits

fruits = ["aplle", "lemon", "orange"]
fruit = "melon"
print(f"before function call:{fruits}ID:{id(fruits)}")
my_fruits(fruits, fruit)
print(f"after function call:{fruits}ID:{id(fruits)}")




