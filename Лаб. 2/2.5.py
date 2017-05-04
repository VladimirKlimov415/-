a=int(input('Введите число a '))
b=int(input('Введите число b '))
c=int(input('Введите число c '))

if ((a>=b) and (a>=c)):
	print('Наибольшее число ',a)
elif ((b>=a) and (b>=c)):
	print('Наибольшее число ',b)
elif ((c>=a) and (c>=b)):
	print('Наибольшее число ',c)