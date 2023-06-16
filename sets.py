#unorder 
#values not repeated
#unchangable
s = {2,3,4,5,3,6,4,1}
print(s)
a = {"ali",21,True,2.95,21}
print(a)
for i in a:
    print(i)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
print(s1, s2)
s1.update(s2)
print(s1, s2)
s2.update(s1)
print(s1, s2)
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1, s2)
s3 = s1.symmetric_difference(s2)
print(s3)

#for empty set
s = set()
print(type(s))