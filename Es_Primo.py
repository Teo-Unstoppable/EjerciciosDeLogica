"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def es_primo(n_primo):
    if n_primo <= 1:
        return ("No es primo")

    if n_primo == 2:
        return ("Es primo")

    if n_primo % 2 == 0:
        return ("No es primo")

    raiz = round(n_primo ** 0.5)

    for num in range(3, raiz + 1, 2):
        if n_primo % num == 0:
            return ("No es primo")
    return ("Es primo")


for num in range(1,101):
    if es_primo(num) == "Es primo":
        print(num)
