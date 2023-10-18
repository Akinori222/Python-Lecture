# *args

def get_average(*args):
    print(*args)
    print(args)

    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num

average = get_average(1, 2, 3, 4, 5, 6, 7, 8)
print(average)


# **kwargs
def kwargs_func(**kwargs):
    print(kwargs)
    param1 = kwargs.get("param1", 1)
    param2 = kwargs.get("param2", 2)
    param3 = kwargs.get("param3", 3)

    print(f"param1:{param1}, param2:{param2},param3:{param3}")

kwargs_func(param1=1531252,param2=532232,param3=2222,param4=1111)


# *,**　unpacking operator
numbers = (1, 2, 3)
print(numbers)
print(*numbers)
print(1, 2, 3)

dict_a = {"apple": "red", "lemon": "yellow"}
dict_b = {"melon": "green"}

dict_c = {**dict_a, **dict_b}
print(dict_c)