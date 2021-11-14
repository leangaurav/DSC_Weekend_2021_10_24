n1 = input("Enter a number:")
if n1.isdigit():
    n1 = int(n1)
else:
    print("please eenter a number")
    exit()

n2 = input("Enter a number:")
if n2.isdigit():
    n2 = int(n2)
else:
    print("please eenter a number")
    exit()

if n2 > n1:
    print(n2)
else:
    print(n1)