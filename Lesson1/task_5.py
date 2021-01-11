# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

num = input('Введите номер буквы в алфавите (1..26): ')

letter = string.ascii_lowercase[int(num) - 1]

print(f'Под {num} номером буква: {letter}')
