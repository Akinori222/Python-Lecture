fruits = ["orange", "apple", "Banana"]

anything_list = ["string", 1, 2, 3, True, None, fruits]

# print(anything_list)
#
# print(fruits[0])
# print(fruits[-1])
#
# print(anything_list[-1])
# print(anything_list[-1][-2])
#
# print("Hello world"[-2])

# list メソッド
# .append:新しいオブジェクトを追加する
print(fruits)
fruits.append("melon")
print(fruits)

# .insert:指定したindexに指定したオブジェクトを追加する
print(fruits)
fruits.insert(3, "lemon")
print(fruits)

# .remove:マッチした最初のオブジェクトを除く
print(fruits)
fruits.remove("apple")
print(fruits)

# .sort:昇順に並び替える
fruits.sort()  # 昇順
print(fruits)
fruits.sort(reverse=True)  # 降順
print(fruits)

# len():リストの要素数を取得する (length)
print(len(fruits))
print(len("Hello world"))
