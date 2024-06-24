import math
def twoinput():
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
    return a,b

def oneinput():
    a=float(input("Enter number:"))
    return a


while True:
    print("Calculator HomePage")
    print("Choose operations:")
    print("1:Addition")
    print("2:Subtraction")
    print("3:Multiplication")
    print("4:Division")
    print("5:Power")
    print("6:Square_root")
    print("7:sin(x)")
    print("8:cos(x)")
    print("9:tan(x)")
    print("10:Factorial(x)")
    print("11:Exit")

    choice=int(input("Enter your choice:"))
    if choice==11:
        print("Exiting")
        break


    match choice:
        case 1:
            a,b=twoinput()
            print(a,"+",b,"=",a+b)
            print("-------------------------------------------------------------------------")
            print("\n")
        case 2:
            a,b=twoinput()
            print(a,"-",b,"=",a-b)
            print("-------------------------------------------------------------------------")
            print("\n")
        case 3:
            a,b=twoinput()
            print(a,"*",b,"=",a*b)
            print("-------------------------------------------------------------------------")
            print("\n")
        case 4:
            a,b=twoinput()
            print(a,"/",b,"=",a/b)
            print("-------------------------------------------------------------------------")
            print("\n")
        case 5:
            a,b=twoinput()
            print(a,"^",b,"=",a**b)
            print("-------------------------------------------------------------------------")
            print("\n")
        case 6:
            a=oneinput()
            print("Square root of",a,"=",math.sqrt(a))
            print("-------------------------------------------------------------------------")
            print("\n")
        case 7:
            a=oneinput()
            print("Sin of",a,"=",math.sin(a))
            print("-------------------------------------------------------------------------")
            print("\n")
        case 8:
            a=oneinput()
            print("Cos of",a,"=",math.cos(a))
            print("-------------------------------------------------------------------------")
            print("\n")
        case 9:
            a=oneinput()
            print("Tan of",a,"=",math.tan(a))
            print("-------------------------------------------------------------------------")
            print("\n")
        case 10:
            a=oneinput()
            print("Factorial of",int(a),"=",math.factorial(int(a)))
            print("-------------------------------------------------------------------------")
            print("\n")
        case _:
            print("Invalid Choice")
            print("-------------------------------------------------------------------------")
            print("\n")




