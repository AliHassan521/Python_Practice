import os
print("Hello World...")
os.system("python --version")

x = int(input("Enter a number = "))
match x:
    case 0:
        print("case is zero")
    case 4:
        print("case is 4")
    case _:
        print("Invalid case")
        