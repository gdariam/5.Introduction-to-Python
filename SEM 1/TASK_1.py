# Задача 1: по двум заданным числам проверить,
# является ли одно квадратом второго

a = int(input('a = '))
b = int(input('b = '))
if a == b**2:
    print(f'число {a} является квадратом числа {b}')
else:
    print(f'число {a} не является квадратом числа {b}')
