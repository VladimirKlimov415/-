import random;


l=[round(random.uniform(-100, 100),1) for i in range(12)]

min=999999

print('Исходный массив: ',l)
for i in l:
	if i<min:
		min=i

index=l.index(min)

sum=min+index

print('Сумма минимального элемента и его индекса: ',sum)


