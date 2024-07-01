"""
Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información
al respecto.
"""

def verificar(n):
    lista = []
    for num in n:
        num = int(num)
        new_num = num**len(n)
        lista.append(new_num)
    return lista

def es_narcisita(lista, n):
    n = int(n)
    suma = 0
    for num in lista:
        suma += num
    if suma == n:
        print("Es narcisista")
    else:
        print("No es narcisista")


num = (input("Ingrese un numero: "))
x = verificar(num)
es_narcisita(x, num)

#Números narcisistas de ejemplo: 370 , 1634, 407, 153, 54748, 8208.

