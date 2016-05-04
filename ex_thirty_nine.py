"""
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:

>>> import guess_number
Hello! What is your name?
Torbjo	rn
Well, Torbjorn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjorn! You guessed my number in 3 guesses!

"""


import random

name = raw_input("Hello! What is your name?")
print "Well, %s I am thinking of a number between 1 to 20." %name

number  = random.randint(1,20)
input_number = int(raw_input("Take a guess."))
count  = 1

while input_number != number:
	if input_number < number:
		print "your guess is too low."
	elif input_number > number:
		print "your guess is too high."
	input_number = int(raw_input("Take a guess. ")) 
	count += 1
print "Good job, %s! you guessed my number in %d guesses!" %(name, count) 