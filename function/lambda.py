# lambda関数　（無名関数）

def square(x):
    return x * x


# f = lambda x: x * x

print(square(3))
# print(f(3))


def power(exponent):
    # def inner_power(base):
    #     return base ** exponent
    return lambda base: base ** exponent
    # return inner_power

four_power = power(4)
print(four_power(2))


numbers = [32, 22, 14, 129, 1991, 2001]

# def filter_func(num):
    # if num % 2 == 0:
    #     return False
    # else:
    #     return True

    # return not num % 2 == 0
    # return num % 2

# filter_num = filter(filter_func, numbers)
filter_num = filter(lambda num: num % 2, numbers)  # filter関数：第２引数の要素を第１引数に入れた時に、Trueになる要素だけを取ってくる
print(list(filter_num))


# for num in numbers:
#     print(filter_func(num))