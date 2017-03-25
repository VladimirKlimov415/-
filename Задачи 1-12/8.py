print('Введите 4 элемента массива')

a=input()
b=input()
c=input()
d=input()

list=[a,b,c,d]

flag=0;
for sign in range(len(list)-1):
	if list[sign]==list[sign+1]:
		print('Есть два соседних элемента с одинаковым знаком')
		flag=1
		break
if flag==0:
	print('Нет двух соседних элементов с одинаковым знаком')	