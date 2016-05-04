"""This program has function generate_n_chars() that takes an integer n and a character c and returns a string,
 n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". """

def generate_n_chars(num,char):
	char_val =" "
	if num == 0 and num < 1 :
		print "Invalid"
	else:
		for i in range(num):
			char_val += char
		print char_val


if __name__ == "__main__" :
	a = int(raw_input("Enter the numeric value : "))
	b = str(raw_input("Eneter the charcter ")).lower()
	generate_n_chars(a,b)
