string = "0123456789"
substring = ""

print(f"Cadena principal: {string}")

substring = string[0]
print(f"\nSubcadena con indice en la posición [0] es: {substring}")

substring = string[5]
print(f"\nSubcadena con indice en la posición [5] es: {substring}")

substring = string[-4]
print(f"\nSubcadena con indice en la posición [-4] es: {substring}")

substring = string[0:3]
print(f"\nSubcadena con indices en las posición [0:3] es: {substring}")

substring = string[:3]
print(f"\nSubcadena con indices en las posiciónes [:3] es: {substring}")

substring = string[5:]
print(f"\nSubcadena con indices en las posiciónes [5:] es: {substring}")

substring = string[-4:-1]
print(f"\nSubcadena con indices en las posiciónes [-4:-1] es: {substring}")

substring = string[:]
print(f"\nSubcadena con indices en las posiciónes [:] es: {substring}")


print("****************************************************************")

substring = string[1:6:2]
print(f"\nSubcadena con indices en las posición [1:6:2] es: {substring}")

substring = string[::3]
print(f"\nSubcadena con indices en las posición [::3] es: {substring}")







