
n=int(input('Введите натуральное число n: '))

for i in range(10,n+1):
	a=i
	min=9
	while i!=0:
		if i%10<min:
			min=i%10
		i=i//10
	print('Наименьшая цифра числа ',a,'-',min)

		
		
