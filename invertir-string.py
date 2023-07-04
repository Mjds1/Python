"""Desarrollar un programa que invierta una cadena de caracteres, y a su vez, esta
cadena de caracteres deberá ser ingresada por el usuario desde teclado.
REQUERIMIENTOS INDISPENSABLES:

- No se permite modificar la cadena de caracteres original.
- Utilizar el ciclo o bucle for."""

string = input("Introduce un string para invertirlo: ")
string_reversed = ""

for character in string:
    string_reversed = character + string_reversed

print(f"String invertido: {string_reversed}")
