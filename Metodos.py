#Titulo Programa: Metodos.
#Fecha: 30-Diciembre-2022
#Autor: Renteria Arriaga Josue

"""Estructura:
class nombre de la clase:
    def nombre del metodo (self):

# Nos referimos y llamamos al objeto.
self.nombre de la variable = ALGORITMO 

self se refiere al objeto
"""

# Escribimos la clase.
class Matematicas:
    # Definimos el metodo de Suma.
    def suma(self):
        self.n1 = 2
        self.n2 = 1
        # return (self.n1 + self.n2)

# Hacemos nuestro objeto.
s = Matematicas()

# Llamamos a los metodos.
s.suma()
print(s.n1 + s.n2)
