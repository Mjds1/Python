"""Desarrollar un programa que imprima en pantalla la Sucesión de Fibonacci desde el número 0 hasta
el número 1597, de manera horizontal

REQUERIMIENTOS INDISPENSABLES:
El programa deberá tener un máximo de 7 líneas de código
"""

num_uno, num_dos, = 0, 1
while num_dos <= 1597:
    print(num_uno, num_dos, end=" ")
    num_uno = num_uno + num_dos
    num_dos = num_uno + num_dos
 

