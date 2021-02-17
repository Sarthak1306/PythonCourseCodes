import random

random_number = random.randint(1,10)  # numbers 1 - 10
user_input = None
# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!




while True:
	user_input = int(input("Guess the number!"))
	if(user_input > random_number):
		print('Ehh, Too High!')
	elif user_input< random_number:
		print('Too Low')
	else: 
		print(f'You Won! The Number Was {random_number}')
		play_again = input('Do you want to play again? (y/n)')
		if play_again == "y":
			random_number=random.randint(1,10)
			user_input = None
		else:
			print('Thankyou for playing')
			break


