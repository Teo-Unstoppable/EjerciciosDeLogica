"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

x = 0
y = 1

num_list = []
actual_num = 0
anterior_num = 0

while len(num_list) < 51:
    actual_num = x + y
    anterior_num = x
    x = actual_num
    y = anterior_num
    num_list.append(actual_num)

print(list(enumerate(num_list)))