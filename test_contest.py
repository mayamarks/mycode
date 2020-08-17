#!/usr/bin/env python3
from cheatdice import *
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
loaded_dice_2 = Cheat_Loaded_Dice_2()
swapper_score = 0
loaded_dice_score = 0
loaded_dice_2_score = 0
failed = 0
number_of_games = 100000
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
    swapper.roll()
    loaded_dice.roll()

    swapper.cheat()
    loaded_dice.cheat()
    loaded_dice_2.cheat()
    # Remove # before print statements to see simulation running
    # Simulation takes approximately one hour to run with print
    # statements or ten seconds with print statements
    # commented out

   #print("Cheater 1 rolled" + str(swapper.get_dice()))
   #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
    if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) and sum(loaded_dice_2.get_dice()) == (swapper.get_dice()):
       # print("Draw!")
        pass
    elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) > sum(loaded_dice_2.get_dice()):
       #print("Dice swapper wins!")
        swapper_score += 1

    elif sum(loaded_dice.get_dice()) > sum(swapper.get_dice()) and sum(loaded_dice.get_dice()) > sum(loaded_dice_2.get_dice()):
       #print("Loaded dice wins!")
        loaded_dice_score += 1

    elif sum(loaded_dice_2.get_dice()) > sum(loaded_dice.get_dice()) and sum(loaded_dice_2.get_dice()) > sum(swapper.get_dice()):
        loaded_dice_2_score += 1
    else:
        failed += 1

    game_number += 1

print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
print("Loaded dice 2 won: " + str(loaded_dice_2_score))
if swapper_score == loaded_dice_score and swapper_score == loaded_dice_2_score:
    print("Game was drawn")
elif swapper_score > loaded_dice_score and swapper_score > loaded_dice_2_score:
    print("Swapper won most games")
elif loaded_dice_score > swapper_score and loaded_dice_score > loaded_dice_2_score:
    print("Loaded dice won most games")
elif loaded_dice_2_score > swapper_score and loaded_dice_2_score > loaded_dice_score:
    print("Loaded dice (3 to 6) won most games")
else:
    print("smth is wrong")
