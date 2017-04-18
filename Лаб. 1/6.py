profitLastMonth=float(input('Введите прибыль за прошлый месяц: '))

costLastMonth=float(input('Введите рентабельность за прошлый месяц: '))

costCurrentMonth=costLastMonth* 0.95


efficiency=profitLastMonth/costCurrentMonth*100

print('Рентабельность предприятия: ',efficiency)