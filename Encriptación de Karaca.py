"""
Crea una función que sea capaz de encriptar y desencriptar texto
utilizando el algoritmo de encriptación de Karaca
(debes buscar información sobre él).

Input: "apple"
Output: "1lpp0aca"
a => 0
e => 1
i => 2
o => 2
u => 3
"""

def encriptar(texto):
    new_text = texto[::-1]
    new_text = new_text.replace("a","0")
    new_text = new_text.replace("e","1")
    new_text = new_text.replace("i","2")
    new_text = new_text.replace("o","3")
    new_text = new_text.replace("u","4")
    return new_text + "aca"

def desencriptar(texto):
    new_text = texto
    new_text = new_text.replace("aca","")
    new_text = new_text[::-1]
    new_text = new_text.replace("0","a")
    new_text = new_text.replace("1","e")
    new_text = new_text.replace("2","i")
    new_text = new_text.replace("3","o")
    new_text = new_text.replace("4","u")
    return new_text


def comprobar(texto):

    if texto.endswith("aca") and len(texto)>3:
        return desencriptar(texto)
    else:
        return encriptar(texto)





texto = input("Ingrese el texto que desea encriptar o desencriptar: ")
print(comprobar(texto))


