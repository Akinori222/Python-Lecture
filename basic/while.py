# while 条件を設定して、その条件がTrueの間ループする
# count = 0
# while count < 10:
#     print(count)
#     count += 1

# break と continue
# while True:
#     age = int(input("How old are you?"))
#     if not 0 <= age < 120:
#         print("The value entered is incorrect.")
#         continue  # 書かなくてもok
#     else:
#         print(f"Your age is {age}.")
#         break


# challenge
casino_age = 18
user_age = int(input("How old are you?"))
game_text = """Please select a game.
    1:Roulette
    2:Blackjack
    3:Pocker
    """

if user_age >= casino_age:
    print("Welcome to the casino.")

    while True:
        select_game = int(input(game_text))
        if select_game == 1:
            print(f"Let's play Roulette.")
            break
        elif select_game == 2:
            print("Let's play Blackjack.")
            break
        elif select_game == 3:
            print("Let's play Poker.")
            break
        else:
            print("Type it again.")
            continue

else:
    print("Can't enter the casino.")