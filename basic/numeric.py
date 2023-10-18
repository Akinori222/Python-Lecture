# 数値型(numeric)  integer:整数, float:浮動小数点, complex:複素数

print(type(0.1))
print(0.1 + 0.1 + 0.1)

print(type(100))

print(0.1*8 + 0.7/0.2)

hit_point = 2000
attack_point = 800
defence_point = 500

remain = hit_point - attack_point
remain2 = hit_point - attack_point*(1 - defence_point / 1000)

print(f"remain of hit_point is {remain}.:{type(remain)}:{id(remain)}")

print(f"remain of hit_point is {remain2}.:{type(remain2)}:{id(remain2)}")
