from gameFunction import gameVars

# need a function to run to compare the choices
# figure out what to pass into the function - hink => what are you comparing?
#
def compareChoices(player):
	#always check a breaking condition first
	if player == gameVars.computer:
		#we have a tie, no point in ging any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock":
		if gameVars.computer == "paper":
			print("\033[2;35;47m""You lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
			print("   +++   ")
			print("   +++   ")
			print("+++++++++")
			print("+++++++++")
			print("   +++   ")
			print("   +++   ")
			print("  (+++)  ")
			print(" (+++++) ")
			print("(+++++++)")


		else:
			print("\033[2;33;47m""You won!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
			print("     *     ")
			print("   *-|-*   ")
			print("   ..*..   ")
			print("  *******  ")
			print("\*********/")
			print("(((((0)))))")

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("\033[2;35;47m""You lose!", gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
			print("   +++   ")
			print("   +++   ")
			print("+++++++++")
			print("+++++++++")
			print("   +++   ")
			print("   +++   ")
			print("  (+++)  ")
			print(" (+++++) ")
			print("(+++++++)")
		else:
			print("\033[2;33;47m""You won!", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
			print("     *     ")
			print("   *-|-*   ")
			print("   ..*..   ")
			print("  *******  ")
			print("\*********/")
			print("(((((0)))))")
	
	elif player == "scissors":
		if gameVars.computer == "rock":
			print("\033[2;35;47m""You lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
			print("   +++   ")
			print("   +++   ")
			print("+++++++++")
			print("+++++++++")
			print("   +++   ")
			print("   +++   ")
			print("  (+++)  ")
			print(" (+++++) ")
			print("(+++++++)")
		else:
			print("\033[2;33;47m""You won!", player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
			print("     *     ")
			print("   *-|-*   ")
			print("   ..*..   ")
			print("  *******  ")
			print("\*********/")
			print("(((((0)))))")