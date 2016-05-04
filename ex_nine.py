"""This program has a function that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise."""
"""def is_Member(value, list):
	for element in list:
		if value ==  element :
			return True
		else:
			return False


if __name__ == "__main__" :
	a = []
	for i in range(0,6):
		m = raw_input("Enter"+str(i+1)+" : ")
		r = a.append(m)	
	val = raw_input("Enter the value : ")
	print(is_Member(val,a))
"""

def is_Member(value, list1):
	for element in range(len(list1)):
		if value ==  list1[element] :
			return True
		else:
			return False


if __name__ == "__main__" :
	a = []
	for i in range(0,6):
		m = raw_input("Enter"+str(i+1)+" : ")
		r = a.append(m)	
	val = raw_input("Enter the value : ")
if is_Member(val,a) == True:
	print "True"
else:
	print "False"
