#Titulo Programa: Clases y Objetos (Ejemplo 2)
#Fecha: 29-Diciembre-2022
#Autor: Renteria Arriaga Josue

# Creacion de una clase (Persona).
class persona:
    doctor = "Victor"

# Mostramos los atributos.
print(persona.doctor)

# Creacion de una clase (Jugadores).
class jugadores_A:
    j1 = "Messi"
    j2 = "CR7"

# Mostramos los atributos.
print(jugadores_A.j2)

# Creacion de una clase (Jugadores).
class jugadores_B:
    j1 = "Marcelo"
    j2 = "Neymar"

# Mostramos los atributos.
print(jugadores_B.j2)

# Creacion de objetos y Metodos.
class nombre:
    # La palabra pass rompe para que no marque erro.
    pass

# Creacion de Objeto, para nuestra clase nombre.
victor = nombre()
maria = nombre()

# Creacion de Atributos (objeto.atributo = valor).
victor.edad = 17
victor.sexo = "Maculino"
victor.pais = "Mexico"

maria.edad = 25
maria.sexo = "Femenino"
maria.pais = "Colombia"

# Mostramos nuestros atributos.
print(victor.edad)
print(maria.edad)