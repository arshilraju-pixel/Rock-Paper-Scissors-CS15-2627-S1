import random

def get_cpu_choice():
   cpu_choice = random.choice(["rock", "paper", "scissors"])
   return cpu_choice

def get_player_choice():
   while True:
       player_choice = input("Choose (rock, paper, scissors): ").lower()
       if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
           return player_choice
       else:
            print("Invalid choice. Try again.")

def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
        winner = "tie"

    elif cpu_choice == "rock":
        if player_choice == "paper":
            winner = "Player wins"
        else:
            winner = "Computer wins"
    elif cpu_choice == "paper":
        if player_choice == "scissors":
            winner = "Player wins"
        else:
            winner = "Computer wins"


    elif cpu_choice == "scissors":
        if player_choice == "rock":
            winner = "Player wins"
        else:
            winner = "Computer wins"

    return winner

def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()

    print("CPU chose", cpu_choice)
    print("You chose", player_choice)

    winner = check_winner(cpu_choice, player_choice)


    print("Round winner", winner)

    return winner

player_wins = 0
cpu_wins = 0
ties = 0

while player_wins < 3 and cpu_wins < 3:
    winner = play_round()

    if winner == "PlYER":
        player_wins += 1
    elif winner == "CPU":
        cpu_wins += 1
    else:
        ties += 1

    print()
    print("Current Score:")
    print("player:",player_wins)
    print("CPU:",cpu_wins)
    print("ties:",ties)
    print()

if player_wins == 3:
    print("Overall winner:Player!")
else:
    print("Overall winner:CPU!")


