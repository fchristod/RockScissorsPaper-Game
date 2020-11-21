from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

choice = ["petra", "psalidi", "xarti"]
round = 0
player_choices = []
pc_choices = []
score = [0, 0]
draws = 0
history = []

while (score[0] < 3) & (score[1] < 3):
    round += 1
    print("Round " +str(round))
    #player
    player_choice = input("Petra, Psalidi, Xarti: ").lower()
    for i in choice:
        if player_choice not in choice:
            player_choice = input("Petra, Psalidi h Xarti: ").lower()
        else:
            if player_choice == "petra":
                player_move = 0
            elif player_choice == "psalidi":
                player_move = 1
            else:
                player_move = 2
            player_choices.append(player_choice)
    #computer
    pc_move = randrange(3)
    if pc_move == 0:
        pc_choice = "petra"
    elif pc_move == 1:
        pc_choice = "psalidi"
    else:
        pc_choice = "xarti"
    pc_choices.append(pc_choice)
    print("Computer: " +pc_choice)

    #result
    if (player_choice == "petra" and pc_choice == "psalidi") or (player_choice == "psalidi" and pc_choice == "xarti") or (player_choice == "xarti" and pc_choice == "petra"):
        score[0] += 1
        winner = "Player"
        print("Player won this round")
    elif (pc_choice == "petra" and player_choice == "psalidi") or (pc_choice == "psalidi" and player_choice == "xarti") or (pc_choice == "xarti" and player_choice == "petra"):
        score[1] += 1
        winner = "PC"
        print("PC won this round")
    else:
        draws += 1
        print("Draw")
        winner = "No Winner"
    print("====================")
    history.append("->Round " +str(round)+ " || Player vs PC: " +player_choice+ " - " +pc_choice+ " || Winner: " +winner)
if score[0] == 3:
    print("Congrats,you've won! Player vs PC: " +str(score[0])+ " - " +str(score[1])+ "\n")
    print("-----------------HISTORY--------------------")
    for k in history:
        print(k)
elif score[1] == 3:
    print("Sorry,you've lost! Player vs PC: " +str(score[0])+ " - " +str(score[1])+ "\n")
    print("-----------------HISTORY--------------------")
    for k in history:
        print(k)








