# closure

# 関数もオブジェクト
def compute_square(num):
    return num * num

print(compute_square(10))
func = compute_square
print(type(func))

print(func(10))

function_list = ["one", 1, True, func]
print(function_list)
print(function_list[-1](10))


# 関数も引数に渡せる
def excute_func(func, param):
    return func(param)

f = excute_func(func, 10)
print(f)


# closure 状態をキープした関数を作ることができる
# 状態が静的
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power

power_four = power(4)
print(power_four)
print(power_four(3))

power_six = power(6)
print(power_six(5))


# 状態が動的
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average

average_nums = average()
print(average_nums(5))
print(average_nums(10))
print(average_nums(25))
print(average_nums(25))
print(average_nums(25))