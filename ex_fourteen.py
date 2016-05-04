"""program for maps a list of words into a list of integers representing the lengths of the correponding words."""
def words_mapp(value):
	result={}
	for i in value:
		num = len(i)
		if result.get(num,0):
			result[num].append(i);
		else:
			result[num]=[i]
	print result

if __name__ == "__main__":
	n = int(raw_input("----> Enter elements here <----- "))
	a = []
	for i in range(0,n):
		m = raw_input("Enter"+str(i+1)+" : ")
		a.append(m)	
words_mapp(a)



