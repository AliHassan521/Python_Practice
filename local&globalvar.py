#Local variable access only within the function
#Global variable access at any place
x = 2
print("global",x)

def val():
    global x
    x = 5
    y = 3
    print("local",y)

val()
print(x)

