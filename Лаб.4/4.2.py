s=input("Введите строку ")

print('После sin,cos,log стоит скобка:')

s=s.replace('sin','sin(')
s=s.replace('cos','cos(')
s=s.replace('log','log(')

print(s)