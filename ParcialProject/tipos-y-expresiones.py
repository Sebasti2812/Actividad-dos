#Conversion de tipos de datos
#enteros
numero_de_pasos= (29)
cantidad_de_libros=5
print(type(numero_de_pasos))

#decimales
Altura=85.5
Peso=78.5
Velocidad=120.5
print(type(Altura))

#Cadenas
Saludo ="bienvenido a Python"
descripcion ="lenguaje de programacion versatil"
aficion= "leer libros"
fruta_favorita= "Mango"
print(type(Saludo))

#Multilineas de cadena
cita_famosa = """“Los sexos opuestos no pueden ser amigos,
por eso ni mires a otros cuando estés conmigo.”
- Cristiano Ronaldo, 2008 Premier League"""
print(type(cita_famosa))

#Funcion len()
mensaje = "Hola, ¿cómo estás?"
longitud_mensaje = len(mensaje)
print(type(longitud_mensaje))

#obtener los primeros n caracteres de una cadena
frase = "Aprender a programar es emocionante"
n = 8
primeros_n = frase[:n]
print("sacando la primera frase:", primeros_n)

#obtener los caracteres de en medio de una cadena
oracion = "me la paso muy bien cuando estoy con mis compañeros de la u"
medio = oracion[15:45]
print("Caracteres de en medio (índices 15 a 45):", medio)

#obtener los últimos n caracteres
frase = "Explorar nuevas tecnologías es fascinante"
n = 10
ultimos_n = frase[-n:]
print("Últimos caracteres:", ultimos_n)

#Upper()
mensaje = "la vida es muy bella "
mayus = mensaje.upper()
print(mayus)

#Lower()
reflexion = "LA VIDA ES UN VIAJE LLENO DE APRENDIZAJES Y EXPERIENCIAS"
minusculas = reflexion.lower()
print(minusculas)

#multilinea de cadenas de caracteres
cadena_multilinea= """La robótica es una rama de la ingeniería
que se ocupa del diseño, construcción y operación de robots.
Estos sistemas automatizados pueden realizar tareas 
en entornos diversos, desde fábricas hasta hogares.
La robótica combina conocimientos de mecánica, electrónica
y programación para crear máquinas inteligentes."""

print(cadena_multilinea)

#Funcion strip
cadena_multilinea_futbol = """   El fútbol es un deporte emocionante.  
Se juega en equipos y se basa en marcar goles.   """
strip_futbol = cadena_multilinea_futbol.strip()
print("Cadena sin espacios:")
print(f"'{strip_futbol}'")

#Función replace()
cadena_multilinea_musica = """La música une a las personas.
Es una forma de expresión y emoción."""
remplazo = cadena_multilinea_musica.replace("música","arte sonoro")
print(remplazo)

#Función split()
cadena_multilinea_vida = """La vida es un regalo.
Cada día cuenta."""
lineas = cadena_multilinea_vida.splitlines()
print("Líneas divididas:")
for i, linea in enumerate(lineas):
    print(f"Línea {i + 1}: '{linea}'")

#Formato de cadenas F-String.
nombre = "Sebastian"
edad = 23

mensaje = f"{nombre} está por cumplir {edad} años en su próximo cumpleaños."

print(mensaje)






