#This program takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
def char_Input(char_IP):
	num = len(char_IP)
	if num > 1:
		print "try again:"
	elif char_IP == 'a' or char_IP == 'e' or char_IP=='i' or char_IP=='o' or char_IP =='u':
		print 'True'
	else:
		print 'False'

if __name__ == "__main__":
	ch = str(raw_input("Enter ONE character : ")).lower()
	char_Input(ch)
