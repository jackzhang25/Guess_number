
first_name = raw_input('What is your name?')

	
from random import randrange
number = randrange(1,20)
while True:	
	guess = raw_input (first_name + "pick a number between 1 and 20 :")
	try:
		guess = int(guess)
	except:
		print "PLEASE PICK A NUMBER!!!"
		continue
	if number < guess: 
		print 'your guess  is to high'
	elif number > guess: 
		print 'your guess is to low' 
	elif number == guess: 
		print 'yay you guessed the right number'
		break
     