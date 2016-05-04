#This program is use to find the largest number 
def max(num1,num2):
	if num1 > num2:
	    print "This is largest: " + str(num1)
	else:
	    print "This is largest: " + str(num2)

if __name__ == "__main__":
	#Here n1 and n2 take user input 
	n1 = int(raw_input("Enetr fist argument: "))
	n2 = int(raw_input("Enter second argument: "))
	max(n1,n2) 