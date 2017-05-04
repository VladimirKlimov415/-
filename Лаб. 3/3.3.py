n=int(input('Введите значение n: '))
n=int(input('Введите значение n: '))

sum=0
while m<=n:
	if m%2==0:
		sum=sum+m*m
	m=m+1

print('Сумма квадратов четных чисел в интервале ',sum)

