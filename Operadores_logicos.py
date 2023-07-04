#Conjución

print("Conjución (and)")

num_uno = int(input("Escriba un número mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno <5:
    print("El número ", num_uno, " cumple con la condicion. \n")
else:
    print("El número ", num_uno, "No cumple con la condición. \n")

#Disyunción
print("Disyunción (or)")

palabra = input("Para cumplir con la condición 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido.\n")
else:
    print("La condición NO se cumple.\n")


#Negación
print("Negación (not)")

num_uno = int(input("Introduce un número igual a 5: "))

if not num_uno == 5:
    print("\n El número es diferente a cinco y SI cumple la condición.\n")
else:
    print("\n El número es diferente a cinco y NO cumple la condición.\n")













