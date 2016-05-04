def hello_program(hello):
	print hello

if __name__ == "__main__":
	hello = raw_input("Enter the TEXT: ").lower()
	hello_program(hello)