a=int(input('Введите число a '))
b=int(input('Введите число b '))
c=int(input('Введите число c '))
d=int(input('Введите число d '))

if ((a%5==0 and b%2==0) or  (a%5==0 and c%2==0) or (a%5==0 and d%2==0) or (b%5==0 and a%2==0) or (b%5==0 and c%2==0) or (b%5==0 and d%2==0) or (c%5==0 and a%2==0)
or (c%5==0 and b%2==0) or  (c%5==0 and d%2==0) or (d%5==0 and a%2==0) or (d%5==0 and b%2==0) or  (d%5==0 and c%2==0)):
	print('Истина')
else:
	print('Ложь') 
