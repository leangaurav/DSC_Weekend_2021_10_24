
try:
    x = input("Enter a number: ")
    y = int(x)
    print("y", y)
    z = 4//y
    print("z", z)
    a = [1,2,3]
    print(a[z])
except ValueError:
    print("value error")
except ZeroDivisionError:
    print("ZeroDivisionError")
    
print("after the try/except block")