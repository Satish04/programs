#Find the length of string without using len() function
def string_length(name):
	num = 0
	for i in name:
		num +=1
	print "the length of string is: " + str(num)

#This is main function 
if __name__ == "__main__":
	name = str(raw_input("Enter any type of STRING : ")).lower()
	string_length(name)