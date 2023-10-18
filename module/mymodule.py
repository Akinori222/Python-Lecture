my_variable = "This is global variable"

def my_func():
    print("This is my function.")

def another_func():  # _関数名：外から使うことを想定していない意思表示

    print("This is another function.")


print("This is mymodule")
if __name__ == "__main__":
    print(f"mymodule.__name__:{__name__}")