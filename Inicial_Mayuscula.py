"""
Crea una función que reciba un String de cualquier tipo y se encargue de
poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que
lo resuelvan directamente.
"""

def inicial_mayuscula(string):
    count = -1
    lista = []
    for palabra in string.split(" "):
        letra_mayus = palabra[count + 1].upper()
        lista.append(letra_mayus + palabra[1:])

    return " ".join(lista)


inicial = input("Pon un texto: ")
x = inicial_mayuscula(inicial)
print(x)





