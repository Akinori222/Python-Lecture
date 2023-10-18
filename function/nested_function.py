# 関数の中で関数を定義する　(nested_function)

# def outer():
#     def inner():
#         print("This is inner function.")
#     inner()
#
# outer()
# inner()

message = "I am global"

def outer():
#    global message
    message = "I am outer"

    def inner():
#        nonlocal message
        message = "I am inner"
        print(message)

    inner()
    print(message)

outer()
print(message)
