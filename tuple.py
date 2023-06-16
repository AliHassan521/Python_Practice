#tuple can't be mainpulate
#any data ype can be fixed in tuple or concatinate
#slicing but return new tuple
#immutable
tup = (1,2,3,4,"Ali")
print(len(tup), tup)
print(tup[0])
print(tup[2])
print(tup[-3])
print(tup[1:])
#if we change tuple firstly
#we change it into list
countries = ("pak","ind","aus","afg")
temp = list(countries)
temp.append("sa")
temp.pop(2)
temp[1] = "eng"
countries = tuple(temp)
print(countries)