# function

# 華氏から摂氏に変換
fahrenheit = 72
# celsius = (fahrenheit - 32) * 5/9
#
# print(celsius)


# celsius = fahrenheit_to celsius(fahrenheit)

def fahrenheit_to_celsius(fahrenheit):  # def 関数名(引数：parameter)※def内の引数fahrenheitと変数celsiusは、def外のfahrenheit,celsiusとは別
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


celsius = fahrenheit_to_celsius(fahrenheit)  # 引数に渡す値：argument
print(celsius)
