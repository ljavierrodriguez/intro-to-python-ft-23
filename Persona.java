class Persona {
    private String nombre = "";
    private String apellido = "";
    private String edad = "";

    Persona(String nombre, String apellido, String edad){
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    public void saludar(){
        System.out.println("Soy una persona");
    }

    public String nombreCompleto(){
        return this.nombre + " " + this.apellido;
    }
}