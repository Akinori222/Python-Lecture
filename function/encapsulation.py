# カプセル化 (encapsulation) : 外からアクセスできないようにする

def casino_entrance(age, min_age=20):
    if age < min_age:
        print("You cannot enter the casino")
        return

    def inner_casino_entrance():
        print("Welcome to the casino")

    return inner_casino_entrance()

casino_entrance(30)