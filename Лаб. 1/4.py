from math import *

x=float(input("Введите x "))

y=float(input("Введите y "))

a=(x*x*x+y*y*y)/2

b=sqrt(abs(x)*abs(y))
print("Среднее арифметическое кубов чисел: ",a)
print("Среднее геометрическое модулей чисел: ",b)
