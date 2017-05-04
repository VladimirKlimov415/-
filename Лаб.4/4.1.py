s=input("Введите строку ")

t=''

letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in s:
	if not(i in letters):
		t=t+i
			
print('Строка без латинских символов '+t) 
