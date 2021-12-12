
try:
	x = input("Enter a number: ")
	y = int(x)
	print("y", y)
	z = 4//y
	print("z", z)
except: # empty excepts should never be used
	print("something went wrong")
    
print("after the try/except block")