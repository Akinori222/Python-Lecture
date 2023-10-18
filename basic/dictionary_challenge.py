# casino_age = 18
# user_age = int(input("How old are you?"))
# game_text = """Please select a game.
#     1:Roulette
#     2:Blackjack
#     3:Pocker
#     """
#
# if user_age >= casino_age:
#     print("Welcome to the casino.")
#
#     while True:
#         select_game = int(input(game_text))
#         if select_game == 1:
#             print(f"Let's play Roulette.")
#             break
#         elif select_game == 2:
#             print("Let's play Blackjack.")
#             break
#         elif select_game == 3:
#             print("Let's play Poker.")
#             break
#         else:
#             print("Type it again.")
#             continue
#
# else:
#     print("Can't enter the casino.")

casino_age = 18
user_age = int(input("How old are you?"))
game = {1: "Roulette", 2: "Blackjack", 3: "Poker"}

if user_age >= casino_age:
    print("Welcome to the casino.")
    while True:
        print("Please choose a game.")
        for num, game_name in game.items():
            print(f"{num} : {game_name}")
        select_game = int(input(":"))

        if select_game in game:
            print(f"The game you chose is {game[select_game]}.")
            break
        else:
            print("<Choose from 3 games.>")
else:
    print("Can't enter the casino.")