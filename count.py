string = "mi mamá me mima"
contador = 0

print(string.center(40, "="))

contador = string.count("M")
print(f"\nLa letra M se encontró {contador} veces en la cadena: {string}")


contador = string.count("m")
print(f"\nLa letra m se encontró {contador} veces en la cadena: {string}")


contador = string.count("mamá")
print(f"\nLa letra mamá se encontró {contador} veces en la cadena: {string}")


contador = string.count("me mima")
print(f"\nLa letra me mima se encontró {contador} veces en la cadena: {string}")


contador = string.count("ma")
print(f"\nLa letra ma se encontró {contador} veces en la cadena: {string}")


contador = string.count("m", 13)
print(f"\nLa letra m se encontró {contador} veces, desde la posición 13 en la cadena: {string}")


contador = string.count("m", 100)
print(f"\nLa letra m se encontró {contador} veces, desde la posición 100 en la cadena: {string}")


contador = string.count("m", -3)
print(f"\nLa letra m se encontró {contador} veces, desde la posición -3 en la cadena: {string}")


contador = string.count("m", 3, 7)
print(f"\nLa letra m se encontró {contador} veces, desde la posición 3 hasta la posición 7 en la cadena: {string}")


contador = string.count("m", 100, 100)
print(f"\nLa letra m se encontró {contador} veces, desde la posición 100 hasta la posición 100 en la cadena: {string}")


contador = string.count("m", -4, -1)
print(f"\nLa letra m se encontró {contador} veces, desde la posición 3 hasta la posición 7 en la cadena: {string}")


