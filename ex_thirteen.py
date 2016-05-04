""" This program has  max_in_list() function , that takes a list of numbers and returns the largest one."""
def max_in_list(value):
	maxm = value[0]
	for i in value:
		if maxm < i:
			maxm = i
	return maxm


if __name__ == "__main__":

	n = int(raw_input("----> Enter elements here <----- "))
	a = []
	for i in range(0,n):
		m = raw_input("Enter"+str(i+1)+" : ")
		a.append(m)	
	print max_in_list (a)