"""This program has histogram() Function that takes a list of integers and prints a histogram to the screen.
 For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
"""

def histogram(list):
	num = len(list)
	for i in range(0,num):
		val = 'x' * int(list[i])
		print val
	 

if __name__ == "__main__" :

	#a is array type of variable that take n elements from the user
	n = int(raw_input("----> Enter elements here <----- "))
	a = []
	for i in range(0,n):
		m = raw_input("Enter"+str(i+1)+" : ")
		r = a.append(m)	
	histogram(a)
