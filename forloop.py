print("Square")
#print square
for i in range(5):
    for j in range(5):
     print("*",end=" ")

    print()

print("Triangle")
#print triangle
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")

    print()

print("Reverse triangle")
#print reverse trinagle
for i in range(5):
    for j in range(5-i):
        print("*",end=" ")

    print()

for i in range(1,6,1):
    for i in range(i,6,1):
        print(i,end=" ")

    print()