#CLASE Persona
class Persona:
    
    def __init__(self, nombre: str, rut: str, telefono: str):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
    
    def mostrar_informacion(self):
        print(f"\nNombre: {self.nombre}"
              f"\nRut: {self.rut}"
              f"\nTelefono: {self.telefono}") 
    
    def obtener_nombre(self):
        return self.nombre