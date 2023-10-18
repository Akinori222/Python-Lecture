# tuple 変更できないリスト　()を使用

data_of_birth = [1991, 1, 4]
data_of_birth2 = (1991, 1, 4)

print(data_of_birth)
data_of_birth[0] = 1990
print(data_of_birth)

# data_of_birth2[0] = 1991
# print(data_of_birth2)

year, month, day = data_of_birth2  # unpack（アンパック）する
print(year)
print(month)
print(day)

for x in enumerate(data_of_birth2):
    print(x)

for x in data_of_birth2:
    print(x)
