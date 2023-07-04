"""La compañia multinacional Rappi, solicita un sistema que determine los dias de vacaciones a los que tiene derecho un trabajador, tomando en cuenta las siguientes caracteristicas. Existen tres departamentos dentro de la compañia con sus respectivas claves:

1.Departamento de Atención al cliente(Clave 1)
  -Con un 1 año de servicio, reciben 6 dias de vacaciones.
  -Con 2 a 6 años de servicio, reciben 14 dias de vacaciones
  -A partir de 7 años de servicio, reciben 20 dias de vacaciones 
2.Departamento de Logistica(Clave 2)
  -Con 1 año de servicio, reciben 7 dias de vacaciones
  -Con 2 a 6 años de servicio, reciben 15 dias de vacaciones
  -A partir de 7 años de servicio, reciben 22 dias de vacaciones
3.Gerencias(Clave 3)
  -Con 1 año de servicio, reciben 10 dias de vacaciones
  -Con 2 a 6 años de servicio, reciben 20 dias de vacaciones
  -A partir de 7 años de servicio, reciben 30 dias de vacaciones

Requerimientos indispensables:

El sistema debe solicitar el "Nombre", "Clave del departamento" y "Antiguedad" del trabajador desde teclado
Posteriormente el programa debe mostrar un mensaje de pantalla, que contenga el nombre del trabajador y los dias de vacaciones a los que tiene derecho
"""
print("*************************************")
print("*Sistema de control vacacional Rappi*")
print("************************************* \n")

nombre_empleado = input("Por favor introduce el nombre del empleado: ")
clave_departamento = int(input("Por favor introduce la clave del departamento: "))
antiguedad_empleado = float(input("Por favor introduce la años laborados del empleado: "))

if clave_departamento == 1:
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, "tiene derecho a 6 dias de vacaciones.")
    elif antiguedad_empleado >=2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado,"tiene derecho a 14 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El trabajador", nombre_empleado,"tiene derecho a 20 dias de vacaciones.")
    else:
        print("El trabajador", nombre_empleado,"aún no tiene derecho a vacaciones.")

elif clave_departamento == 2:
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, "tiene derecho a 7 dias de vacaciones.")
    elif antiguedad_empleado >=2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado,"tiene derecho a 15 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El trabajador", nombre_empleado,"tiene derecho a 22 dias de vacaciones.")
    else:
        print("El trabajador", nombre_empleado,"aún no tiene derecho a vacaciones.")

elif clave_departamento == 3:
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado,"tiene derecho a 10 dias de vacaciones.")
    elif antiguedad_empleado >=2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado,"tiene derecho a 20 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El trabajador", nombre_empleado,"tiene derecho a 30 dias de vacaciones.")
    else:
        print("El trabajador", nombre_empleado,"aún no tiene derecho a vacaciones.")

else:
    print("La clave de departamento no exite, vuelve a intentarlo.")







































