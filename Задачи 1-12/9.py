print('Введите количеcтво элементов в массиве')

n=int(input())

list=[]

for i in range(n):
	a=int(input())
	list.append(a)
	
print('Наибольший элемента массива: ',max(list))