"""This program has sum() function that sums  all the numbers in a list of numbers."""
def sum(numbers):
	total = 0
	#num1 = list(numbers)
	for number in numbers:
		total += int(number)
	print "sum is "+ str(total)

#The is multiply function that multiply  all the numbers in a list of numbers.
def multiply(numbers):
    total = 1
    #num1 = list(numbers) 
    for number in numbers:
        total = total * int(number)
    print "multiply is " + str(total)

if __name__ == "__main__":
	#"n" is limit of list number  
	#a is array type of variable that take n elements from the user
	n = int(raw_input("you can insert n number in the list : please enter range of the digit "))
	a = []
	for i in range(0,n):
		m = raw_input("Enter"+str(i+1)+" : ")
		r = a.append(m)	
		print a
	sum(a)
	multiply(a)