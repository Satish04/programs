"""
An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up at least two 
other words. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every second 
letter is used will produce a four-letter word and a three-letter word. Here are two examples:

  "board": makes "bad" and "or".
  "waists": makes "wit" and "ass".

Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that goes through each word in the list and tries to make two smaller 
words using every second letter. The smaller words must also be members of the list. Print the words to the screen in the above fashion. 

"""

def alternade_word(word,setWord):
	setFirst = []
	setSecond = []
	length =  len(word)
	if length % 2:
		length +=1
		word = word + ""
	for i in range(0,len(word)-1,2):
		#print i
		setFirst.append(word[i])
		#print setFirst
		setSecond.append(word[i+1])
		#print setSecond
	newSetFirst = "".join(setFirst).strip()
	newSetSecond = "".join(setSecond).strip()
	if newSetFirst in setFirst and newSetSecond in setSecond:
		return (newSetFirst, newSetSecond)
	return None



if __name__ == "__main__":
	setWord = set([ "ass", "bad", "or", "wit", "dog",])
	word = raw_input("Enter word: ")
	print alternade_word(word, setWord)

