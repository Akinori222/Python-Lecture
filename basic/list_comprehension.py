# リスト内包表記

# for loop
square_list = []

for i in range(11):
    square = i ** 2
    square_list.append(square)

print(square_list)

# list comprehension
square_list = [i ** 2 for i in range(11)]
print(square_list)

even_square_list = [i ** 2 for i in range(11) if i % 2 == 0]
print(even_square_list)
