
def get_int():
	x = input("Enter a number: ")
	y = int(x)
	return y
	
def div():
    y = get_int()
    print("y", y)
    z = 4//y
    print("z", z)



try:
    print("before")
    div()
except ValueError:
    print("Handling value error !!")
else:
    print("No exception !!")
finally:
	print("finally block !!")

print("after")