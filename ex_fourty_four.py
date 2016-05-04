"""
 Your task in this exercise is as follows:

    Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
    Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest. 

Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK

"""

def string_generate(string):
	num = len(string)
	print num
	if num%2==0:
		half = num / 2
		first = '[' * half
		last = ']' * half
		if string[0:half] == first and string[half:num] == last:
			return 'OK'
		else:
			return 'NOT OK'

	else:
		return 'NOT OK'








if __name__ == "__main__":
	string_value = raw_input("Enter your STRING i.e. '[]' or '][' :   ")
	print string_generate(string_value)