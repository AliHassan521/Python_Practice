#order collection of data iteams 
#there is a key value for particular iteam
#way of mapping
# dic = {521:"Ali Hassan",537:"Azhar",516:"Usman"}
# print(dic[521])
# print(dic.get(521))
# print(dic.keys())
# print(dic.values())
# s = {}
# print(type(s))
# for key in dic.keys():
#     print(f"The value corresponding to the key {key} is {dic[key]}")
# for key,value in dic.items():
#     print(f"The value corresponding to the key {key} is {value}")


emp1 = {511:67,513:73,516:82,518:59,521:91,537:89}
emp2 = {543:77,519:62}

#emp1.update(emp2)
#emp1.clear()
emp1.pop(513)
emp1.popitem()
print(emp1)





