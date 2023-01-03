#Titulo Programa: Herencia (Ejercicio 2).
#Fecha: 31-Diciembre-2022
#Autor: Renteria Arriaga Josue

# Creamos nuestra clase.
class Calculadora:
    # Definimos nuestro constructor.
    def __init__(self, numeros):
        self.n = numeros
        self.datos = [0 for i in range(numeros)]
    
    # Metodo Ingresar Datos.
    def ingresar_dato(self):
        self.datos = [int(input("Ingresa datos: "+str(i+1)+" = ")) for i in range(self.n)]

# Clase con herencia.
class Op_basicas(Calculadora):
    # Definimos nuestro constructor.
    def __init__(self):
        Calculadora.__init__(self, 2) # Limitamos los datos necesarios.

    # Metodo de Suma.
    def suma(self):
        a,b, = self.datos
        s = a + b
        print("El resultado es: ", s)

    # Metodo de Resta.
    def resta(self):
        a,b, = self.datos
        s = a - b
        print("El resultado es: ", s)

# Clase con herencia.
class Raiz(Calculadora):
    # Definimos nuestro constructor.
    def __init__(self):
        Calculadora.__init__(self, 1)
    
    # Metodo de Raiz Cuadrada.
    def cuadrada(self):
        import math
        a, = self.datos
        s = math.sqrt(a)
        print("El resultado es: ", s)

# Creamos nuestro objeto para la clase (herencia op_basicas).
ejemplo =  Op_basicas()
print("\nOPCION DE SUMA")
ejemplo.ingresar_dato()
ejemplo.suma()

# Creamos nuestro objeto para la clase (herencia op_basicas).
ejemplo =  Op_basicas()
print("\nOPCION DE RESTA")
ejemplo.ingresar_dato()
ejemplo.resta()

# Creamos nuestro objeto para la clase (Raiz).
ejemplo =  Raiz()
print("\nOPCION DE RAIZ CUADRADA")
ejemplo.ingresar_dato()
ejemplo.cuadrada()
