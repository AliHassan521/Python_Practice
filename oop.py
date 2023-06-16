class student():
    country = "Pakistan"
    def __init__(self,name,reg,gpa):
        self.name = name
        self.reg = reg
        self.gpa = gpa
std1 = student(name = "Ali Hassan",reg = "2021-cs-521",gpa = 3.2)
std2 = student(name = "Azhar Hayat",reg = "2021-cs-537",gpa = 3.4)
print(std2.name)
print(std1.gpa) 
std1.name = "Usman"
print(std1.name)
print(std2.country)     