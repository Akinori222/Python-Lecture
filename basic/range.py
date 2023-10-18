# range(start, stop, step)

# for i in range(1,20,2):  # （開始、未満、ステップ）
#     print(i)
#
# for _ in range(10):
#     print("Hey")

# challenge

# for i in range(1,51):  # 失敗
#     if i % 3 == 0:
#         print(f"{i} = Fizz")
#     elif i % 5 == 0:
#         print(f"{i} = Buzz")
#     elif i % 3 == 0 and i % 5 == 0:
#         print(f"{i} = FizzBuzz")
#     else:
#         print(i)

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:  # i % 15 == 0
        print(f"{i} = FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} = Fizz")
    elif i % 5 == 0:
        print(f"{i} = Buzz")
    else:
        print(i)

# command + ] インデント

