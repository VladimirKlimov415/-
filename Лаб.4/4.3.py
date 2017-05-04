s=input("Введите строку ")

current_word=0

min_word=len(s)

for i in s:
	if ('a'<=i<='z' or 'A'<=i<='Z' or 'а'<=i<='я' or 'А'<=i<='Я'):
		current_word+=1
	else:
		if (current_word<min_word and current_word!=0):
			min_word=current_word
		current_word=0

min_word=current_word
print('Длина самого короткого слова:',min_word)


