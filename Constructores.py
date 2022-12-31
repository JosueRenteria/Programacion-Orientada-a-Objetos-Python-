#Titulo Programa: Constructores.
#Fecha: 30-Diciembre-2022
#Autor: Renteria Arriaga Josue

# Si el metodo o funcion inicia con __ significa que esta funcion tiene una relacion especial.
# __init__(), es una funcion constructor.

# Creamos nuestra clase.
class Persona:
    pass
    # Creamos nuestro constructor.
    def __init__(self, nombre, edad, año):
        # Declaracion de nuestros atributos.
        self.edad = edad
        self.nombre = nombre
        self.año = año
    
    # Creacion de nuestros metodos.
    def descripcion(self):
        # Con la funcion .format() es una forma de imprimir tambie.
        return "{} tiene {}".format(self.nombre, self.año)
    
    # Creacion del metodo comentario.
    def comentario(self, frase):
        return "{} dijo: {}".format(self.nombre, frase)

# Creamos nuestro descriptor.
doctor = Persona("Juan", 28, 2022)
print(doctor.año)

# Mandar a llamar a los Metodos.
print(doctor.descripcion())
print(doctor.comentario("Hola"))