"""In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by guessing, and in return
receive two kinds of clues: 1) the characters that are fully correct, with respect to identity as well as to position, and 2) the characters 
that are indeed present in the word, but which are placed in the wrong position. Write a program with which one can play Lingo. Use square brackets 
to mark characters correct in the sense of 1), and ordinary parentheses to mark characters correct in the sense of 2). Assuming, for example, that the 
program conceals the word "tiger", you should be able to interact with it in the following way:

import lingo
snake
Clue: snak(e)
fiest
Clue: f[i](e)s(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]

"""

#import random

def lingo(lingo_word):
	guess_list = []
	word = list(lingo_word)


	while guess_list != word:
		#print word
		#print guess_list
		new_list = []
		guess  = raw_input("Enetr word: ")
		guess_list = list(guess)
		for i in guess_list:
			#print i
			if i in word:
				for u in word:
					if i == u:
						if word.index(u) == guess_list.index(i):
							if i not in new_list:
								#print new_list
								new_list.append("[%s]" %i)
						else:
							if i not in new_list:
								#print i
								new_list.append("(%s)"%i)

			else:
				if i not in new_list:
					new_list.append(i)
		print "".join(new_list)
	print("Congrats you win! The word was %s" %"".join(word))

if __name__ == "__main__":
	lingo_word = raw_input("Enter LINGO word: ")
	lingo(lingo_word)