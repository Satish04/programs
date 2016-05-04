"""This programe computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I" """ 
def reverse(name):
	num = 0
	for i in name:
		num +=1
		num2 = num-1
	for i in range(num2,-1,-1):
		print name[i],

if __name__ == "__main__":
	st_name = str(raw_input("Enter the string : ")).lower()
	reverse(st_name)
	


