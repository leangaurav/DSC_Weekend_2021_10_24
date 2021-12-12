import traceback

try:

	i = int(input("Enter number: "))
	a = [10,20,30]
	
	k = a[i]
	print("K", k)
	
	d = {10:100}
	v = d[k]
	
	print("V",v)
	
except LookupError as err:
	print("LookupError: ", str(err))
except ValueError as err:
    print("valueError", err)

print()
print("After handler")