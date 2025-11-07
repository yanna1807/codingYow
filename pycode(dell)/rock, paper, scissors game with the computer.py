#7/11/2024 & 7/12/2024
import random as r

instructions = "Please choose only the word 'rock, paper, or scissors' in this game! Enjoy! mwah :)"
print(instructions)

def winner(player, computer):
    if player == computer:
        winner = "It's a Tie!"
        return winner
    elif player == 'scissors':
        if computer == 'paper':
            winner = "You Win!"
            return winner
        else:
            winner = "Computer Wins!"
            return winner
    elif player == 'paper':
        if computer == 'rock':
            winner = "You Win!"
            return winner
        else:
            winner = "Computer Wins!"
            return winner
    elif player == 'rock':
        if computer == 'scissors':
            winner = "You Win!"
            return winner
        else:
            winner = "Computer Wins!"
            return winner
    else:
        return "Invalid Input. Please choose rock, paper or scissors in a small letter."

def playGame():
    player = input("\n rock, paper, scissors? ")
    choices = ['rock', 'paper', 'scissors']
    computer = r.choice(choices)

    print(f"\nYou chose: {player}")
    print(f"\nComputer chose: {computer}")
    print(f"\n",winner(player, computer))

playGame()

chancesTaken = 0

while chancesTaken <= 4:
    playGame()
    chancesTaken += 1
else:
    print("\nGAME OVER!")

y = 'yes'
n = 'no'

playAgain = input("Do you waish to play again: y or n? ")
if playAgain == y:
    playGame()
    chancesTaken = 0
    while chancesTaken <= 4:
        playGame()
        chancesTaken += 1
    else:
        print("\nGAME OVER!")
else:
    print("Play with you next time!")
