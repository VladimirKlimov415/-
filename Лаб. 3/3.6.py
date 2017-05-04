from math import*

print('Вычисление суммы бесконечного ряда')

n=int(input('Введите количество членов ряда: '))
x=int(input('Введите число x'))
i=2
sum=0
while i<=n:
	sum=sum+sin((i+i-1)*(x**(i+i-1)))
	i+=1

sum=sum+sin(x)

print('Сумма ряда',sum)
