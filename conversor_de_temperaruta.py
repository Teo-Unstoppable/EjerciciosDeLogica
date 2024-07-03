"""
Crea una función que transforme grados Celsius en Fahrenheit
y viceversa.
- Para que un dato de entrada sea correcto debe poseer un símbolo "°"
y su unidad ("C" o "F").
- En caso contrario retornará un error.
"""

def celsius_to_fahrenheit(temperatura):
    temp = int(temperatura)
    return f"{round((temp * 9 / 5) + 32, 2)} °F"

def fahrenheit_to_celsius(temperatura):
    temp = int(temperatura)
    return f"{round((temp - 32) * 5 / 9, 2)} °C"

def comprobar(temperatura):
    lista = []
    for dato in temperatura.split(" "):
        lista.append(dato)

    if len(lista) == 1:
        return "Error, Dato no valido"
    elif lista[1] == "°C":
        return celsius_to_fahrenheit(lista[0])
    elif lista[1] == "°F":
        return fahrenheit_to_celsius(lista[0])
    else:
        return "Error, Dato no valido"




temperatura = input("Ingrese la temperatura: ")
print(comprobar(temperatura))

