import sys

if len(sys.argv) != 2:
	print("Invalid input.\n Usage: cat.py <file>")
	exit(-1)
	
file_name = sys.argv[1]

with open(file_name, 'r') as f:
	print(f.read())
	
