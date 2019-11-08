from random import randint

def winorlose(status):
	print("called win or lose function", status, "\n")
	print("You", status, "! would you like to play again?")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer
		# reset the game and start all over again
		player_lives = 1
		computer_lives = 1
		player = False
		computer = choices[randit(0, 2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice. Yes or no!")
		# recursion => calling a function from inside itself
		winorlose(status)