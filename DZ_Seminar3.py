# Урок 3. Данные, функции и модули в Python
# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
# print ('Введите несколько чисел через пробел и нажмите кнопку ENTER')
# num = input()
# array = num.split(" ")
# sum = 0
# print (f'{array} -> на нечетных позициях элементы ', end= ' ')
# for i in range (1, len(array)):
#     if (i % 2 != 0):
#         print (f"{array[i]}", end= ', ')
#         sum = sum + int(array[i])
# print(f"ответ {sum}")

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# print ('Введите несколько чисел через пробел и нажмите кнопку ENTER')
# num = input()
# array = num.split(" ")
# comp = 0
# j = 0
# count = len(array)
# if ((count % 2) > 0):
#     count = int(count/2 +1)
# else:
#     count = int(count/2)
# print (f'{array} => [', end= '')
# for i in range (count - 1):
#     j = j - 1
#     comp = int(array[i]) * int(array[j])
#
#     print(f"{comp}", end= ', ')
# i = i+1
# j = j - 1
# comp = int(array[i]) * int(array[j])
# print(f"{comp}", end= '] ')

# 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# print ('Введите несколько вещественных чисел через пробел и нажмите кнопку ENTER')
# num = input()
# array = num.split(" ")
# print (f'{array} => ', end= '')
# for i in range (len(array)):
#     array [i] = float (array [i])
#     array[i] = round(array [i] - int(array [i]), 2)
# min = array[i]
# max = array[i]
# for i in range(len(array)):
#     if (array[i] < min):
#         min = array[i]
#     elif (array[i]>max):
#         max = array[i]
# print(f"{max - min}")

4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10

print('Введите число')
num = int(input())
numbul = 0
while (num != 0):
    if ((num % 2) > 0):
        numbul  = str(numbul) + str(1)
        num = num // 2
    else:
        numbul  = str(numbul) + str(0)
        num = num // 2
print (numbul)

