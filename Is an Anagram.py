"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def Anagram(word_1,word_2):
    x = []
    y = []
    if word_1 == word_2:
        print("Not is an anagram")
    else:
        for letter in word_1:
            x.append(letter)
        for letter in word_2:
            y.append(letter)
        x.sort()
        y.sort()
        if x == y:
            print("Is an anagram")
        else:
            print("Not is an anagram")

word_1 = input("Put a word: ")
word_2 = input("Put another word: ")
Anagram(word_1,word_2)