print('Перевод из 10-ой в 16-ую систему счисления')
decimal=int(input("Введите целое число в 10-ой системе счисления: "))

n=decimal

hexadecimal=''

while decimal>0:
	digit=decimal%16
	if digit==10:
		character='A'
	elif digit==11:
		character='B'
	elif digit==12:
		character='C'
	elif digit==13:
		character='D'
	elif digit==14:
		character='E'
	elif digit==15:
		character='F'
	else:
		character=str(digit)
	hexadecimal=character+hexadecimal
	decimal=decimal//16	

print('Число',n,'в 16-ой системе счисления: '+hexadecimal)		