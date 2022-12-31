#Titulo Programa: Metodos (__init__).
#Fecha: 30-Diciembre-2022
#Autor: Renteria Arriaga Josue

# __init__(seft). Esto es para iniciarlo.

# Creamios una clase ropa.
class Ropa:
    # Creamos el metodo de iniciar.
    def __init__(self):
        # Creamos las variables.
        self.marca = "Willow"
        self.talla = 'M'
        self.color = "Rosa"

# Creamos el objeto.
camisa = Ropa()
print(camisa.talla)

# Creamos una segunda clase.
class Calculadora:
    # Creamos el metodo de iniciar.
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2

operacion = Calculadora(2, 3)
print(operacion.suma)