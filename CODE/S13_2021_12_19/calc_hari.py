import sys
try: 
    a=sys.argv[1]
    b=sys.argv[2]
    c=sys.argv[3]

    def calc(a,b,c):
                '''Calculator function based on opertor and values input. Supported operators are +,-,*,/'''
                d=0
                if a=='+':
                    d=b+c
                elif a=='-':
                    d=b-c
                elif a=='*':
                    d=b*c
                elif a=='/':
                    d=b/c
                else:
                    print(a, "is not a valid operator. Please enter valid operator('+','-','*','/')")
                return d 
                
    if a in ('+','-','*','/'):
        if b.isdigit():
            if c.isdigit():
                d=int(b)
                e=int(c)
                print(calc(a,d,e))
            else:
                print("Enter a valid number for number 2")
        else:
            print("Enter a valid number for number 1")
    else:
        print(a, "is not a valid operator. Supported operators are '+','-','*','/'")
except IndexError as error:
    print("Please enter operator 1st followed by number 1 and number 2")