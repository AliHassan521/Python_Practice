a = int(input("Enter a number = "))
op = str(input("Enter an operator = "))
b = int(input("Enter a number = "))
if (op=='+'):
    print(a+b)
elif (op=='-'):
    print(a-b)
elif (op=='*'):
    print(a*b)
elif (op=='/'):
    print(a/b)
else :
    print("In-valid operator...")  