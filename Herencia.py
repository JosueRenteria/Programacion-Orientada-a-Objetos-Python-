#Titulo Programa: Herencia.
#Fecha: 31-Diciembre-2022
#Autor: Renteria Arriaga Josue

# Una clase Dinamica (esta es la clase padre).
class pokemon:
    pass

    # Creamos el constructor.
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    # Creamos el Metodo Descripcion.
    def descripcion(self):
        return "{} es un pokemon de tipo: {}".format(self.nombre, self.tipo)

# Creamos una nueva clase (Clase hija).
class pikachu (pokemon):
    def ataque(self, ataque):
        return "{} tiene de ataque: {}".format(self.nombre, ataque)

# Creamos una nueva clase (Clase hija).
class charmander (pokemon):
    def ataque(self, ataque):
        return "{} tiene de ataque: {}".format(self.nombre, ataque)

# Creamos nuestro objeto.
nuevo_pokemon = pikachu("Josue", "Electrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("Golpe Galactico"))