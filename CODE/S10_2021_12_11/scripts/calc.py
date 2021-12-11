# build script a calc.py 
# python calc.py + 1 2   >>> 3
# python calc.py - 1 2   >>> -1
# python calc.py * 1 2   >>> 2
# python calc.py / 1 2   >>> 0.5
# python calc.py + 1 -4A
import sys
#print(sys.argv)

if (len(sys.argv)== 4) :
    op=sys.argv[1]
    v1=sys.argv[2]
    v2=sys.argv[3]
    try:     
 #   if(v1.isdigit() && v2.isdigit()):
        v2=int(sys.argv[3])
        v1=int(sys.argv[2])
        if op == '+' :
           print(v1+v2)
        elif op == '-' :
           print(v1-v2)
        elif op == '*' :
           print(v1*v2)
        elif op == '/' :
           print(v1/v2)
        else : print("enter valid operator")
    except ValueError:
     print("Please enter numbers")
else : 
     print("Pass valid arguments")


- whenever user gives a wrong operator.. print a message telling which operators are supported
 (keep in mind.. that later our code might support new operators as well)
 
 python calc.py % 1 2
 % not supported. Supported list .. (+,-,...)

- --help option
  1. how the command can be used.
  2. wht all operator it supports

- instead of "Pass valid arguments"
    give a message based on user's mistake and tell how to use it
    

- Improve code.. use functions etc.