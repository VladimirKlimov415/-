print('Введите строку')

str=input()

flag=0
i=0


length=len(str)//2

while i<=length:	
	if str[i]!= str[len(str)-i-1]:
		
		print("Не палиндром")
		flag=1
		break
	i+=1
if flag==0:
	print('Палиндром')
