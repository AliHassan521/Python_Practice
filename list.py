list = [1,2,3,"Ali"]
#list can be mainpulate
#any data ype can be fixed in list or concatinate
#mutable
#slicing
print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[-3])
print(list[0:4])
print(list[0:3:2])
# list comprihension
lst = [i for i in range(6)]
print(lst)
lst = [i*i for i in range(6)]
print(lst)
lst = [i for i in range(6) if i%2==0]
print(lst)

#methods in list
l = [1,3,4,6]
l.append(5)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.insert(2,9)
print(l)
l.pop()
print(l)
l.reverse()
print(l)
m = ["Ali","Azhar","Usman"]
k = l + m
print(k)   #extend method
print(l.count(3))