#This program is use to find the largest number 
def max_of_three(num1,num2,num3):
	if num1>num2 and num1>num3:
		print "The largest number is: " + str(num1)
	elif num2>num1 and num2>num3: 
		print "The largest number is: " + str(num2)
	else:
		print "The largest number is: " + str(num3)	 

#This is main function. 
if __name__ == "__main__": 
	#n1,n2,n3 are three variables that take input from the user
	n1 = int(raw_input("Enetr fist argument: "))
	n2 = int(raw_input("Enter second argument: "))
	n3 = int(raw_input("Enter third argument: "))
	max_of_three(n1,n2,n3) 