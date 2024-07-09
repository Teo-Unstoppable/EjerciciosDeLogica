"""
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se
lanzará una excepción.
"""

days = []
months = []
years = []

def iniciar():
    primera_fecha = input("Ingrese la fecha: ")
    segunda_fecha = input("Ingrese la segunda fecha: ")

    return fecha_1(primera_fecha), fecha_2(segunda_fecha)

def fecha_1(string):
    lista = []
    for dato in string.split("/"):
        lista.append(int(dato))
    days.append(lista[0])
    months.append(lista[1])
    years.append(lista[2])


def fecha_2(string):
    lista = []
    for dato in string.split("/"):
        lista.append(int(dato))
    days.append(lista[0])
    months.append(lista[1])
    years.append(lista[2])



def diferencia():

    days.sort()
    months.sort()
    years.sort()

    diferencia = years[1] - years[0]
    diferencia = diferencia * 365
    diferencia = diferencia - round(30.416666667*(months[1] - months[0]))
    diferencia = diferencia - (days[1] - days[0])
    biciestos = diferencia/365
    biciestos = round(biciestos/4)

    return diferencia + biciestos




iniciar()
diferencia = diferencia()
print(f"La diferencias de dias entre las fechas dadas es: {diferencia}")





