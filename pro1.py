# Convert radians into degrees.
# Sort a list. ...
# Convert a decimal number into binary. ...
# Count the vowels in a string. ...
# Create a calculator function. ...
# Write a Python program that calculates the area of a circle
# based on the radius entered by the user
# Write a Python program that accepts the user's first and last name and prints them in reverse order
# with a space between them.
# Write a Python program that accepts a sequence of comma-separated numbers from the user
# and generates a list and a tuple of those numbers.
# Write a Python program that accepts
# a filename from the user and prints the extension of the file.
# Write a Python program to display the
# first and last colors from the following list
# color_list = ["Red","Green","White" ,"Black"]
# Write a Python program that accepts an
# integer (n) and computes the value of n+nn+nnn.

# Write a Python program to print the sum of two numbers entered by the user.

# x = int(input("Enter a number : "))
# y = int(input("Enter a number : "))
# print(x+y)

# Write a Python program to check if a given number is even or odd.

# x = int(input("Enter a number : "))
# if x%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")

# Write a Python program to print the factorial of a given number.

# x = int(input("Enter a number : "))
# def fac(x):
#     if x==1:
#         return 1
#     else:
#         return x*fac(x-1)
# print(fac(x))
    
# Write a Python program to print the Fibonacci sequence up to a given number.

# n = int(input("Enter a number : "))
# def fib(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(n))      

# Write a Python program to find the largest number in a given list.

# l = [23,56,87,21,67,74]
# print(max(l))

# Write a Python program to check if a given string is a palindrome or not.

# x = input("Enter a string : ")
# if x==x[::-1]:
#     print("String is a palindrome")
# else:
#     print("String is not a palindrome")

# Write a Python program to check if a given number is a prime number or not.
# x = int(input("Enter a number : "))
# for i in range(1,x):
#     if x%i==0:
#         print(x,"is not a prime number")
#         break
#     else:
#         print(x,"is a prime number")

# Write a Python program to convert a given temperature in Fahrenheit to Celsius.
# x = int(input("Enter a number : "))
# if x>=0 and x<=100:
#     print("Temperature in Celsius is :",x-32,"C")
# else:
#     print("Enter a valid temperature")


#Write a Python program to reverse a given string.
# str = input("Enter string : ")
# print(str[::-1])

# Write a Python program to count the number of occurrences of a given character in a given string
# x = input("Enter a string : ")
# y = input("Enter a character : ")
# count = 0
# for i in range(len(x)):
#     if x[i] == y:
#         count += 1
# print(count)

# Write a Python program to find the second largest number in a given list.

# Write a Python program to check if a given year is a leap year or not.
# year = int(input("Enter a year : "))
# if year % 4 == 0:
#     print("Leap Year")
# else:
#     print("Not Leap")    
# Write a Python program to remove duplicates from a given list.
l = [2,6,4,3,4,2]
for i in l:
    if l[i] == l:
        del(i)
# Write a Python program to check if two given strings are anagrams or not.

# Write a Python program to check if a given number is a perfect square or not.

# Write a Python program to convert a given binary number to decimal.

# Write a Python program to find the length of the longest word in a given sentence.

# Write a Python program to find the sum of all the multiples of 3 or 5 below a given number.

# Write a Python program to find the GCD (Greatest Common Divisor) of two given numbers.

# Write a Python program to find the LCM (Least Common Multiple) of two given numbers


# pi = 3.14
# x = float(input("Input : "))
# deg = x * (180/pi)
# print(deg)

# l = []
# for i in range(5):
#    ele = input("Enter list member : ")
#    l.append(ele)
# print(l)   
# l.sort()
# print(l)

# def DtoB(n):
#    if n > 1:
#       DtoB(n // 2)
#    print(n % 2,end="")
# x = int(input("Enter a decimal number :"))
# DtoB(x)


# count = 0
# x = input("Enter a string : ")
# for i in x:
#    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#       count = count + 1
# print(count)

# r = float(input("Enter radius : "))
# area = 3.14*r**2
# print(area)

# fn = input("Enter fist name : ")
# ln = input("Enter last name : ")
# print(ln," ",fn)

# l = []
# for i in range(5):
#    ele = int(input("Enter number : "))
#    l.append(ele)
#    t = tuple(l)
# print(l)
# print(t) 

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0]," ",color_list[3])

# lcolor = []
# n = int(input("Enter range : "))
# for i in range(n):
#    color = input("Enter number : ")
#    lcolor.append(color)
# print(lcolor[0]," ",lcolor[n-1])

# n = int(input("Enter range : "))
# print(n+n**2+n**3)









