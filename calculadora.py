"""Desarrollar una calculadora con los siguientes caracteristicas:

1.La calculadora deberá ser capaz de calcular las operaciones de suma, resta, multiplicacion, division,
division entera, exponente y modulo o resto.

2.La calculadora deberá tener un menú de opciones donde el usuario pueda elegir cual es operacion
que desea ejecutar.

3.La calculadora deberá socilicitar únicamente dos valores por cada operación

REQUERIMIENTOS INDESPENSABLES:

El código de este programa deberá funcionar con una única variable que se llamará "numero", 
es decir, no se permite la implementacion de otra variable."""

print("Calculadora de una sola variable \n")

print("********************")
print("* Menú de opciones *")
print("********************")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo o resto \n")


numero = int(input("Introduce la opción deseada: "))

if numero == 1:
    print("Elegiste suma \n")
    numero = int(input("Introduce el primer numero: "))
    numero += int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ", numero)

elif numero == 2:

    print("Elegiste resta \n")
    numero = int(input("Introduce el primer numero: "))
    numero -= int(input("Introduce el segundo numero: "))
    print("El resultado de la resta es: ", numero)

elif numero == 3:

    print("Elegiste multiplicación \n")
    numero = int(input("Introduce el primer numero: "))
    numero *= int(input("Introduce el segundo numero: "))
    print("El resultado de la multiplicación es: ", numero)

elif numero == 4:

    print("Elegiste división \n")
    numero = int(input("Introduce el primer numero: "))
    numero /= float(input("Introduce el segundo numero: "))
    print("El resultado de la división es: ", round(numero, 2))

elif numero == 5:

    print("Elegiste división entera \n")
    numero = int(input("Introduce el primer numero: "))
    numero //= float(input("Introduce el segundo numero: "))
    print("El resultado de la división entera es: ", numero)

elif numero == 6:

    print("Elegiste exponente \n")
    numero = int(input("Introduce el primer numero: "))
    numero **= float(input("Introduce el segundo numero: "))
    print("El resultado de la exponente es: ", numero)

elif numero == 7:

    print("Elegiste modulo o resto \n")
    numero = int(input("Introduce el primer numero: "))
    numero %= float(input("Introduce el segundo numero: "))
    print("El modulo o resto es: ", numero)

else:
    print("La opción elgida no existe, vuelve a intentarlo.")









































