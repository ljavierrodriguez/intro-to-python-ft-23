class Persona:
    nombre = None
    apellido = None
    edad = None
    direccion = None
    
    def __init__(self, nombre, apellido, edad, direccion):
        print("Creando una instancia de la clase Persona")
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
    
    def saludar(self):
        print("Soy una persona")
        
    def __repr__(self):
        return f"<Persona nombre:{self.nombre} apellido: {self.apellido} edad: {self.edad}>"
    
    
p1 = Persona("John", "Doe", "Unknown")
p2 = Persona("Jane", "Doe", "Unknown")

print(p1)
print(p2)
print(p2.saludar())

class Estudiante(Persona):
    grado = None
    
    def __init__(self, nombre, apellido, edad, grado):
        super().__init__(nombre, apellido, edad)
        self.grado = grado
        
    def __repr__(self):
        return f"<Estudiante nombre:{self.nombre} apellido: {self.apellido} edad: {self.edad} grado: {self.grado}>"
    
    def saludar(self):
        print("Soy un Estudiante")

e1 = Estudiante("John", "Doe", "Unknown", "1er")
print(e1)
print(e1.saludar())