# Задача 1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input(" Введите номер дня недели: "))

if 1 <= num <= 5:
    print(f' {num} -> нет')
elif 6 <= num <= 7:
    print(f' {num} -> да')
else:
    print(f' {num} -> такого дня недели не существует')