""" Functions """
""" 

def functionName():
    sentences


functionName = lambda args: sentence


"""

def sumar(a, b):
    return a + b


restar = lambda a, b: a - b


numeros = [1, 2, 3]

def cuadrado(valor):
    return valor**2

resultados = list(map(lambda valor: valor**2, numeros))
resultados = list(map(cuadrado, numeros))


def nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"

nombre_completo("Luis", "apellido")

# Parametros Keywords
nombre_completo(apellido="Doe", nombre="John")


# Empaquetamiento de Parametros
def totalizar(*args):
    return sum(args)

print(totalizar(10, 20, 30, 40, 50))


# Empaquetamiento de Keywords
def lugar_de_estudio(**keys):
    return f"Hola, soy {keys['nombre']} y estudio en {keys['universidad']}"


print(lugar_de_estudio(nombre="Luis Rodriguez", universidad="Universidad de Caracas", edad=40))