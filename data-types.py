""" Data Types """
""" 

String
Number => int y float
Boolean
None

dict


Array => List, Tuples, Sets

functions => def

"""

# Esto es un comentario

# String
nombre = "Luis"
apellido = 'Rodriguez'
nombre_completo = f"{nombre} {apellido}"

parrafo = """Lorem ipsum dolor sit amet consectetur 
adipisicing elit. Qui aspernatur cumque beatae 
provident nisi! Nostrum beatae dignissimos iure pariatur? 
Soluta nam sunt nostrum veniam possimus ad facilis temporibus
 id eveniet!"""
 
 
# int o float
edad = 40
temp = -10.5
precio = 10.5 

# Boolean
activo = True
abierto = False

# None
users = None
posts = None

# Dict
persona = {
    "nombre": "Catalina",
    "apellido": "Arroyo"
}

nombre = persona["nombre"] + " " + persona["apellido"]

# Array
# List []
valores = [1, 2, 3] # list
frutas = list("Pera", "Manzana", "Uva") # list 

# Tuples ()
estados = ("Activo", "Inactivo", "Supendido", "Cancelado", "Terminado")
generos = tuple("Femenino", "Masculino")

# Sets {}
frutas2 = {"Pera", "Manzana", "Uva"}