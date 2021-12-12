import traceback

try:

	i = int(input("Enter number: "))
	a = [10,20,30]
	
	k = a[i]
	print("K", k)
	
	d = {10:100}
	v = d[k]
	
	print("V",v)
	
except Exception as err:
	print("Something went wrong: ", str(err))
	print(traceback.format_exc())


print()
print("After handler")