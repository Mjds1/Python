"""Desarrollar un programa que elimine una palabra que forme parte de una cadena
de caracteres.
REQUERIMIENTOS INDISPENSABLES:
-La cadena de caracteres deberá ser solicitada desde teclado
-La palabra a eliminar deberá ser solicitada desde teclado
"""

string = input("Introduce una frase: ")
palabra = input("Introduce la palabra que deseas eliminar: ")
substring = ""

indice = string.find(palabra)
substring = string[0 : indice] + string[indice + len(palabra) + 1 : ]


print(f"Cadena resultante: {substring}")
