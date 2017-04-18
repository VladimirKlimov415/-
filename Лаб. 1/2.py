from math import *

y=float(input("Введите y "))
p=float(input("Введите p "))

n=(3*y*y+sqrt(y+1))/(log(p+y)+exp(p))

print(n)