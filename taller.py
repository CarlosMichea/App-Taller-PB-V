from cliente import Cliente
from mecanico import Mecanico

class Taller:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.mecanicos = []
        self.clientes = []
    
    def contratar_mecanico(self, mecanico):
        self.mecanicos.append(mecanico)
        print(f"{mecanico.nombre} fue contratado como mecanico.")
    
    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"{cliente.nombre} fue registrado como cliente.")
    
    def mostrar_mecanicos(self):
        print(f"Mecanicos del Taller {self.nombre}:")
        for m in self.mecanicos:
            m.mostrar_informacion()
    
    def contar_clientes(self):
        return len(self.clientes)