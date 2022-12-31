#Titulo Programa: Modificar Atributos.
#Fecha: 30-Diciembre-2022
#Autor: Renteria Arriaga Josue

# Creamos nuestra clase.
class Email:
    pass
    # Creamos nuestro constructor.
    def __init__(self):
        # Declaracion de nuestros atributos.
        self.enviado = False
    
    # Creacion de nuestro metodo enviar.
    def enviar_correo(self):
        self.enviado = True

# Creamos nuestro descriptor.
mi_correo =  Email()
print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)
