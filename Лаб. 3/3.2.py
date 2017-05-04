k=int(input('Введите значение k: '))

mul=1
sum=0
for j in range(1,k+1):
	if j==3 or j==4:
		continue
	mul=mul*(j-4)*j/(j-3)
	i=j
	for i in range (j,k+2):
		if i==1:
			continue
		sum=sum+((i+5)**(1/3))/(i-1)

a=mul*sum

print('Выражение А = ',a)
