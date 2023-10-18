# dictionary: キーと値の組み合わせを複数所持するデータ型

# date_of_birth = {"aki": "19910104", "mituki": "20010129"}
# print(date_of_birth)
# print(date_of_birth["aki"])  # 順番は保持しない。キーと値の組み合わせでのみ保持
#
# date_of_birth["sasaki"] = "19900101"  # 値とキーの追加
# print(date_of_birth)
#
# number = {1: "one", "two": 2, "three": [3, "san"], "four": {4: "yon"}}
# print(number)
#
# print(number["four"])
# print(number["four"][4])

# color = {}
# color[1] = "red"
# color[0] = "yellow"
# color[3] = "white"
# print(color)
#
# # .keys():キーでループを回す　　.values()：値でループを回す
fruits = {"apple": "red", "melon": "green", "lemon": "yellow"}

# for fruit in fruits.keys():
#     print(fruit)
#
# for color in fruits.values():
#     print(color)

# # for x in fruits:  # keysとvaluesを指定しなければkeyでループする。
# #     print(x)

# .items()
for fruit, color in fruits.items():  # キーと値をタプルでループ
    print(f"{fruit} is {color}.")

