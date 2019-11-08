# import the random package so we can generate a random AI choice
from random import randint
from gameFunction import winlose, gameVars

while gameVars.player is False:
	print("============================================")
	print("Computer Lives:", gameVars.computer_lives, "/5")
	print("Player Lives:", gameVars.player_lives, "/5")
	print("============================================")
	print("Choose your weapon!\n")
	player=input("choose rock, paper or scissors \n")

	
	#always check a breaking condition first
	if player == gameVars.computer:
		#we have a tie, no point in ging any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock":
		if gameVars.computer == "paper":
			print("You lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("You lose!", gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
	
	elif player == "scissors":
		if gameVars.computer == "rock":
			print("You lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
	
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")
	
	else:
		player = False
		gameVars.computer=gameVars.choices[randint(0,2)]