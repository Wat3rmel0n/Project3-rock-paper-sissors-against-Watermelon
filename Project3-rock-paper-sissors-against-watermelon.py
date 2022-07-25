import random
import time
print("\nWatermelon has challenged you to play rock paper sissors with him.\n")
time.sleep(2)
print("Do you accept his challenge? (y/n)\n")

while True:
    answer = input()
    if answer == "y":
        break
    if answer == "n":
        time.sleep(1.5)
        print("\nWhat about now\n")
    else:
        print("\ny or n\n")
win_count = 0
del(answer)
while True:
    options = ["rock", "paper", "sissors"]
    watermelon_choice = random.choice(options)
    player_choice = input("\nChoose your weapon (rock, paper or sissors)\n\n")
    time.sleep(1)
    if player_choice == watermelon_choice:
        print("\nYou both chose " + (player_choice) + ". Its a draw")
    elif player_choice == "rock":
        if watermelon_choice == "sissors":
            print("\nYou chose " + (player_choice) + ", Watermelon chose " + (watermelon_choice) + ". Rock smashes sissors in pieces. You win, gg.")
            win_count += 1
        else:
            print("\nYou chose " + (player_choice) + ", Watermelon chose " + (watermelon_choice) + ". Paper covers your rock and it dissapears forever. You lose, gg.")
            win_count -= 1
    elif player_choice == "sissors":
        if watermelon_choice == "rock":
            print("\nYou chose " + (player_choice) + ", Watermelon chose " + (watermelon_choice) + ". Rock smashes sissors in pieces. You lose, gg.")
            win_count -= 1
        else:
            print("\nYou chose " + (player_choice) + ", Watermelon chose " + (watermelon_choice) + ". Sissors brutally cut paper in pieces. You win, gg.")
            win_count += 1
    elif player_choice == "paper":
        if watermelon_choice == "sissors":
            print("\nYou chose " + (player_choice) + ", Watermelon chose " + (watermelon_choice) + ". Rock smashes sissors in pieces. You win, gg.")
            win_count += 1
        else:
            print("\nYou chose " + (player_choice) + ", Watermelon chose " + (watermelon_choice) + ". Paper covers rock and it dissapears forever. You lose, gg.")
            win_count -= 1
    del(player_choice) 
    del(watermelon_choice)
    print("\nWin count: " + str(win_count) + "\n")
    time.sleep(2)
    while True:
        answer = input("Wanna play again?(y/n)\n\n")
        if answer == "y":
            print("\nWatermelon accepts your challenge.")
            break
        if answer == "n":
            print("\nOk, bye, gl.\n")
            quit()
        else: 
            print("\ny or n\n")