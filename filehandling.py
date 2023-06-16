#To open a file we need a function open() with two arguments first file name and second what you want (read,write,append) r,w and a means read,write and append if file exist
# f = open('myfile.txt','r')
# text = f.read()
# print(text)
# f.close() 
# f = open('myfile.txt','w')
# text = f.write("At this time I started the series 100 days of coding in python by codewithHarry")
# print(text)
# f.close()
# # In these methods file closed is compulsory

# with open('myfile.txt','a') as f:
#     f.write("Ali Hassan")
#Read line method to read lines in a file
# f = open('myfile.txt','r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         print(line,type(line))
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student {i} in OS : {m1}")
#     print(f"Marks of student {i} in DBS : {m2}")
#     print(f"Marks of student {i} in AOA : {m3}")
#     print(line)  
f = open('myfile.txt','w')
lines = ["line 1\n","line 2\n","line 3\n"]
line = f.writelines(lines)