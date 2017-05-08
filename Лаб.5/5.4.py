import random;

n=int(input('Введите количество строк в матрице: '))
m=int(input('Введите количество столбцов в матрице: '))

l=[[random.randint(-100,100) for i in range(0,m)] for j in range(0,n)]



print('Исходная матрица: ',l)

count=0

for i in range(0,4):
	if l[i][1]>=0:
		count+=1

print('Количество неотрицательных элементов во втором столбце матрицы:',count)