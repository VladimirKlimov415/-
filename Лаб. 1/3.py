from math import *

x=float(input("Введите x "))

if 6*x*x<=1 and 6*x*x>=-1:

	k=sqrt(pow(3+x,6)-log(x))/(exp(0)+asin(6*x*x))
	print(k)
else: print("Некорректный ввод (arcsin должен принимать значение от -1 до 1 )")
