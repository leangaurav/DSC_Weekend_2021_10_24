n1 = input("Enter a number:")
n2 = input("Enter a number:")

if n1.isdigit() and n2.isdigit():
    a=int(n1)
    b=int(n2)
    if b > a:
       print(b)
    else:
      print(a)
else: 
	print("please enter a number only")