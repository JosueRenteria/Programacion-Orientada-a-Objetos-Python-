#Titulo Programa: Funciones para Atributos.
#Fecha: 30-Diciembre-2022
#Autor: Renteria Arriaga Josue

# Construccion de una clase.
class Persona:
    edad = 27
    nombre = "Victor"
    pais = "Mexico"

# Llamamos a los atributos.
doctor = Persona()

# Formas de llamar a los atributos
print("La edad es: ", doctor.edad)
print("La edad es: ", getattr(doctor,'edad')) # De forma directa.

# Para saber si un atributo existe.
print("El doctor tiene una edad?", hasattr(doctor,'edad'))

# Hacer cambios a los atributos.
print(doctor.edad)
setattr(doctor,'edad',29)
print(doctor.edad)

# Borrar un atributo de la clase.
print("Hay pais?", hasattr(doctor,'pais'))
delattr(Persona,'pais')
print("Hay pais?", hasattr(doctor,'pais'))