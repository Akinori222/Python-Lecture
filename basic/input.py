# input(): ユーザーが入力した値（文字列）を取得する

# challenge 1
# age = int(input("How old are you?"))
# casino_age = 18
#
# if age >= casino_age:
#     print("You can enter the store.")
# else:
#     print("You can't enter the store.")


# challenge 2
# age = int(input("How old are you?"))
# casino_age = 18
#
# if age < casino_age:
#     print("You cannot enter the store.")
# else:
#     select_game = int(input("""please select a game.\n1:Roulette\n2:Blackjack\n3:Poker"""))  # ハードコードx
#     if select_game == 1:
#         print("You play Roulette.")
#     elif select_game == 2:
#         print("You play BlackJack.")
#     else:
#         print("You play Poker.")

age = int(input("How old are you?"))
casino_age = 18
game_text = """Please select a game.
1:Roulette.
2.BlackJack.
3:Poker.
"""

if age >= casino_age:
    print("Please come in.")
    game_select = input(game_text)
    if game_select == "1":
        print("You chose Roulette.")
    elif game_select == "2":
        print("You chose Blackjack.")
    elif game_select == "3":
        print("You chose Poker.")
    else:
        print("Please choose from 1 to 3!!")

else:
    print("You cannot enter the casino.")
