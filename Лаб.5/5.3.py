import random;

list1=[random.randint(1,100) for i in range(3)]


print('Исходный массив:',list1)

binary=''
list2=[]
for i in range(0,3):
	while list1[i]>0:
		digit=list1[i]%2
		character=str(digit)
		binary=character+binary
		list1[i]=list1[i]//2

	list2.append(binary)
	binary=''

print('Массив в двоичной системе счисления',list2)

