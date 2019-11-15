from random import randint
from gameFunction import gameVars

def winorlose(status):
	print("called win or lose function", status, "\n")
	print("You", status, "! would you like to play again?")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		# reset the game and start all over again
		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice. Yes or no!")
		# recursion => calling a function from inside itself
		winorlose(status)