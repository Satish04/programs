"""This program has a function is_palindrome, taht recognizes palindromes (i.e. words that look the same written backwards). 
For example, is_palindrome("radar") should return True."""

def is_palindrome(name):
    num = len(name)
    for i in range(num):
        if name[i]==name[-1-i]:
            return True
        return False

if __name__ == "__main__":
	n=str(raw_input("Enter the String:"))
	if is_palindrome(n) == True:
		print 'True'
	else:
		print 'False'
