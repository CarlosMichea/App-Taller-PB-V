from persona import Persona
from bicicleta import Bicicleta

class Cliente(Persona):
    
    def __init__(self, nombre, rut, telefono, direccion: str):
        
        super().__init__(nombre, rut, telefono)
        self.direccion = direccion
        self.bicicletas = []
    
    def agregar_bicicleta(self, bicicleta):
        self.bicicletas.append(bicicleta)
        print(f"Bicicleta {bicicleta.numero_serie} registrada.")
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"\nDireccion: {self.direccion}") 
    
    def contar_bicicletas(self):
        return len(self.bicicletas)