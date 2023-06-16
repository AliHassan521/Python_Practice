#else statement execute when for loop ends not break
for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("Hello World")
    
print()


for i in range(5):
    print(i)
else:
    print("Hello World")
