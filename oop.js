class Persona {
    nombre = null;
    apellido = null;
    edad = null;

    constructor(nombre, apellido, edad){
        //console.log("Creando una instancia de la clase Persona");
        //console.log(nombre)
        //console.log(apellido)
        //console.log(edad)

        this.nombre = nombre
        this.apellido = apellido
        this.edad = edad
    }

    saludar(){
        console.log("Soy una persona")
    }
}

let p1 = new Persona("John", "Doe", "Unknown"); // creando una instacia de la clase persona
let p2 = new Persona("Jane", "Doe", "Unknown"); // creando una instacia de la clase persona

console.log(p1)
console.log(p2)


const saludar = () => {
    console.log("Hola mundo")
}

console.log(saludar())

class Estudiante extends Persona {
    grado = null;
    constructor(nombre, apellido, edad, grado){
        super(nombre, apellido, edad);
        this.grado = grado
    }
}

const e1 = new Estudiante("John", "Doe", "Unknown", "1er")
e1.nombre = "Luis"
console.log(e1)
console.log(e1.saludar())