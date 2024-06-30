"""
Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar
la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras
o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en
https://es.wikipedia.org/wiki/Código_morse.
"""

lista_morse = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
    ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-",
    ".--", "-..-", "-.--", "--..", "/"
]
lista_normal = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

def to_morse(entrada):
    palabra = entrada.upper()
    lista_ayuda = []
    for letra in palabra:
        if letra in lista_normal:
            indice = lista_normal.index(letra)
            lista_ayuda.append(lista_morse[indice])
    return " ".join(lista_ayuda)

def to_text(entrada):
    lista_ayuda = []
    for letra in entrada.split(' '):
        if letra in lista_morse:
            indice = lista_morse.index(letra)
            lista_ayuda.append(lista_normal[indice])
    return ''.join(lista_ayuda)

def detectar_y_convertir(entrada):
    if set(entrada).issubset(set(".-/ ")):
        return to_text(entrada)
    else:
        return to_morse(entrada)

palabra = input("Put a word or morse text: ")
x = detectar_y_convertir(palabra)
print(x)

