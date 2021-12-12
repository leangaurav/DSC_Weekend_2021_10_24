import traceback

try:

	i = int(input("Enter number: "))
	a = [10,20,30]
	
	k = a[i]
	print("K", k)
	
	d = {10:100}
	v = d[k]
	
	print("V",v)
	
except KeyError as err:
	print("KeyError: ", err)
except LookupError as err:
	print("LookupError: ", err)
except Exception as err:
	print("Exception: ", type(err), err)

print()
print("After handler")