"""This program has a function find_longest_word() that takes a list of words and returns the length of the longest one."""

def find_longest_word(value):
	index = 0
	result = ''
	for i in value:
		num = len(i)
		if num > index:
			index = num
			result = i
			print result
	
if __name__ == "__main__":

	n = int(raw_input("----> Enter elements here <----- "))
	a = []
	for i in range(0,n):
		m = raw_input("Enter"+str(i+1)+" : ")
		a.append(m)	
	find_longest_word(a)
