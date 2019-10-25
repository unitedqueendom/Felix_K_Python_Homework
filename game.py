# import the random package so we can generate a random AI choice
from random import randint

# "basket" of choices
choices=["rock", "paper", "scissors"]

# let the AI make choice
computer=choices[randint(0,2)]

# set up a game loop here so we don't have to keep restarting
player = False

while player is False:
	player=input("choose rock, paper or scisors \n")

	#start doing some logic and condition checking
	print("computer: ", computer, "player: ", player)

	#always check a breaking condition first
	if player == computer:
		#we have a tie, no point in ging any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()

	else:
		print("Not a tie. Now we can check other conditions")
		if player == "rock":
			print("check and see what the computer is, and win or lose")

	player = False
	computer=choices[randint(0,2)]