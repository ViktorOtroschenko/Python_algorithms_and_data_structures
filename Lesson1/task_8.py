# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три числа: ')
a = int(input('1 число: '))
b = int(input('2 число: '))
c = int(input('3 число: '))

mean = a + b + c - max(a, b, c) - min(a, b, c)

print(f'Среднее число: {mean}')