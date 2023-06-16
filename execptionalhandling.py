#Skip the error and execute remaining statements
x = input("Enter a number : ")
print(f"Table of {x} is")
try:
   for i in range(1,11):
      print(f"{x} X {i} = {int(x)*i}")
except:
  print("invalid input")

print("Important statements")
