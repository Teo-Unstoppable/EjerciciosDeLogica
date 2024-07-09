"""
Crea una función que imprima los 30 próximos años bisiestos
siguientes a uno dado.
- Utiliza el menor número de líneas para resolver el ejercicio.
"""


def bisiesto(year):
    lista = list(range(1, 31))
    year = int(year)
    for num in lista:
        year = year + 4
        print(year)


year = input("Pon un año: ")
bisiesto(year)

