from persona import Persona
from bicicleta import Bicicleta

class Mecanico(Persona):
    def __init__(self, nombre, rut, telefono, especialidad, sueldo):
        super().__init__(nombre, rut, telefono)
        self.especialidad = especialidad
        self.sueldo = sueldo
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Especialidad: {self.especialidad}"
              f"\nSueldo: {self.sueldo}")
    
    def reparar_bicicletas(self, bicicleta):
        return f"{self.nombre} está reparando la bicicleta {bicicleta.numero_serie}"