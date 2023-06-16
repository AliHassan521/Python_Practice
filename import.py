#import use to laod all the functions of a module
import math
res = math.sqrt(9)
print(res)
#From use to run specific functions of a module
from math import sqrt,pi
x = sqrt(9)*pi
print(x)
#As reduce the name of module as your own choice
import math as m
res = m.sqrt(9)
print(res)
#dir tells all the functions in a module
import math
print(dir(math))

