def print_dict(input_dict):
    for key, value in input_dict.items():
        print(f"key:{key}, value:{value}")  # 値を返さない場合はNoneで返ってきている

number = {"one": 1, "two": 2}

print(number)
print_dict(number)

return_value = print_dict(number)

print(return_value)

def get_farst_last_word(text):
    text = text.replace(".", "")
    words = text.split()
    return words[0], words[-1]  # 複数の値を返す場合はタプルで返ってくる


text = "Hello. My name is Aki!"
first, last = get_farst_last_word(text)  # タプルで欲しくない場合は変数を複数用意して値を入れる
print(f"First word is {first}\nLast word is {last}")