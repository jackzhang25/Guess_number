

import random
number = random.choice('0123456789')
while True:	
	guess = raw_input ("pick a number between 1 and 9")
	if number < guess: 
		print 'your guess  is to high'
	elif number > guess: 
		print 'your guess is to low' 
	elif number == guess: 
		print 'yay you guessed the right number'
		break