import random
import timeit


start_time = timeit.default_timer()
first_number = int(input("Please enter the smaller number you have determined in the range:"))
second_number = int(input("Please enter the bigger number you have determined in the range:"))
computuer_choice = random.randint(first_number, second_number)
#print(computuer_choice)
attempt = 0
while True:
	guess = int(input("Guess a number: "))
	attempt += 1
	if computuer_choice > guess:
		print("You should try a bigger number:")
	elif computuer_choice < guess:
		print("You should try a smaller number.")
	else:
		end = timeit.default_timer()
		time_end = int(end-start_time)
		print("Congratulations,correct number is", computuer_choice)
		print(f"Your elapsed time is", time_end, "seconds.\n")
		





        
        
	


		






		