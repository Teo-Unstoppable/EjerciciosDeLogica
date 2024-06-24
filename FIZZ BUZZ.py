"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""

numbers = range(1,101)
for num in numbers:

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        continue
    if num % 3 == 0:
        print("Fizz")
        continue
    if num % 5 == 0:
        print("Buzz")
        continue
    else:
        print(num)
