# Developer: Eric Railef
# Curso: Programación Backend

# archivo main
from cliente import Cliente
from mecanico import Mecanico
from bicicleta import Bicicleta
from taller import Taller

def main():
    # Variables
    taller = Taller("Tallerín", "Av. Pasta 1337")
    cliente_1 = Cliente("Valeria Perez", "22333444-5", "+56911223344", "Av. Ravioli 444")
    bici_1 = Bicicleta("Hotwheels", "Montaña", "BIC0123")
    mecanico_1 = Mecanico("Jose Casas", "21222333-4", "+56922224444", "Bicicleta de velocidad", "800000")
    
    # Metodos
    
    # Registrar cliente y asociarlo a una bici
    cliente_1.agregar_bicicleta(bici_1)
    taller.registrar_cliente(cliente_1)
    
    # Contratar mecanico y emitir labor
    taller.contratar_mecanico(mecanico_1)
    print(mecanico_1.reparar_bicicletas(bici_1))
    
    # Mostrar info
    print("\n=== Bicicleta ===")
    bici_1.mostrar_informacion()
    
    
    print("\n=== Mecanicos ===")
    taller.mostrar_mecanicos()
    
    
    print("\n=== Clientes ===")
    print(f"Clientes actuales del taller: {taller.contar_clientes()}")
    
    # fin
    
if __name__ == "__main__":
    main()
