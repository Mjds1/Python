print("Sistema para calcular el promedion de un alumno.")

nombre = input("Para comenzar, ¿Cúal es tu nombre?: ")

matematicas = int(input(nombre +  " ¿Cúal es tu calificación es matematicas?: "))
quimica = int(input(nombre + " ¿Cúal es tu calificación en quimica?:"))
biologia = int (input(nombre + " ¿Cúal es tu calificación en biologia?:"))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 6:
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)

print("Fin.")
