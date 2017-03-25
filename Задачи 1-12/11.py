
print('Введите строку')

str=input()

words=1
i=0
for i in range(len(str)):
	if str[i]==' ':
		words+=1

print('Количество слов в строке:',words)