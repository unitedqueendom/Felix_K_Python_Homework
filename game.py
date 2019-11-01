# import the random package so we can generate a random AI choice
from random import randint

# "basket" of choices
choices=["rock", "paper", "scissors"]

# adding lives -> when one or the other gets to 0, win/ lose
player_lives = 5
computer_lives =5

# let the AI make choice
computer=choices[randint(0,2)]

# set up a game loop here so we don't have to keep restarting
player = False

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
		player_lives = 5
		computer_lives = 5
		player = False
		computer = choices[randit(0, 2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice. Yes or no!")




while player is False:
	print("============================================")
	print("Computer Lives:", computer_lives, "/5")
	print("Player Lives:", player_lives, "/5")
	print("============================================")
	print("Choose your weapon!\n")
	player=input("choose rock, paper or scisors \n")

	#start doing some logic and condition checking
	#print("computer: ", computer, "player: ", player)

	#always check a breaking condition first
	if player == computer:
		#we have a tie, no point in ging any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "smashes", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "covers", computer, "\n")
			computer_lives = computer_lives -1
	
	elif player == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "cuts", computer, "\n")
			computer_lives = computer_lives -1
	
	if player_lives is 0:
		winorlose("lost")
		# print("You lost! Loser. WOuld you like to play again?")
		# choice = input("Y / N?")

		# if choice == "Y" or choice "y":
		#   #reset the game and start all over again
		#   player_lives = 1
		#   computer_lives = 1
		#   player = False
		#   computer = choices[randit(0, 2)]

		#elif choice == "N" or choice == "n":
		#   print("You chose to quit. Better luck next time!")
		#   exit()
		# else:
		#   print("Make a valid choice. Yes or no!")

	elif computer_lives is 0:
		winorlose("won")
		# print("You won! Would you like tp play again?")
		# choice = input("Y / N")

		# if chice == "Y" or choice == "y":
		#   #reset the game and start all over again
		#   player_lives = 1   
		#   computer_lives = 1
		#   player = False
		#   computer = choices[randit(0, 2)] 

		#elif choice == "N" or choice == "n":
		#   print("You chose to quit. Better luck next time!")
		#   exit()
		# else:
		#   print("Make a valid choice. Yes or no!")
		#   #choice = input ("Y or N")

	else:
		player = False
		computer=choices[randint(0,2)]