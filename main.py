import random

function get_cpu_choice():
    cpu_choice = randome choice from "rock, paper, and scissors"
    RETURN cpu_choice

FUNCTION get_player_choice():
    while True:
        input(player_choice)
            if player_choice == valid
                return player_choice

FUNCTION check_winner(cpu_choice, player_choice):
    IF player_choice == cpu_choice THEN:
        winner = "Tie"
    ELSE IF cpu_choice == "rock" THEN:
        IF player_choice == "paper" THEN:
            winner = "PLAYER"
        ELSE:
            winner = "CPU"
        END IF
    ELSE IF cpu_choice == "paper" THEN:
        IF player_choice == "scissors" THEN:
            winner = "PLAYER"
        ELSE:
            winner = "CPU"
        END IF
    ELSE IF player_choice == "paper" THEN:
        winner = "CPU"
    ELSE:
        winner = "PLAYER"
    END IF
    RETURN winner
END FUNCTION

cpu_choice = get_cpu_choice()

player_choice = get_player_choice()

winner = check_winner(cpu_choice, player_choice)

output winner

