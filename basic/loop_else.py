fruits = ["apple", "Banana", "orange", "melon"]

# for else

# for fruit in fruits:
#     choice_fruits = input(f"Are you looking for {fruit}?\ny/n ")
#     if choice_fruits == "y":
#         print("I'll you give this.")
#         break
#     else:
#         print("sorry.")
#
# else: forの条件がfalseになったら実行
#     print("The fruit you were looking for was not found.")


# while else
# count = 0
# while count < 10:
#     print(count)
#     count += 1
#
# else:
#     print("Count is no longer less than 10 ")

balance = 1000
game_price = 200

# choice = input(f"""Would you like to participate in a ${game_price} game?
# Your balance is {balance}. (y/n)""")
#
# if choice == "y":
#     balance -= game_price
#     print(f"(Your balance is {balance}.)")
#
#     while True:
#         again_game = input("Would you like to play the game again? (y/n)")
#         if again_game == "y" and 199 < balance:
#             balance -= game_price
#             print(f"Your balance is {balance}.")
#         elif again_game == "n":
#             print("Let's play again. see you!")
#             break
#         else:
#             print("Insufficient balance!")
#             break
#
# elif choice == "n":
#     print("Let's play again.\n see you!")
#
# else:
#     print("Please enter [y] or [n].")
while balance >= game_price:
    choice = input(f"Would you like to participate in a ${game_price} game?\nYour balance is {balance}. (y/n)")
    if choice == "y":
        balance -= game_price
        print(f"Your balance is {balance}.")

    elif choice == "n":
        print("Let's play again. see you")
        break
    else:
        print("Please enter [y] or [n].")
else:
    print("Insufficient balance")
    