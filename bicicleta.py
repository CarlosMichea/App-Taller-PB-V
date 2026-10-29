class Bicicleta:
    def __init__(self, marca: str, tipo: str, numero_serie: str):
        self.marca = marca
        self.tipo = tipo
        self.numero_serie = numero_serie
    
    def mostrar_informacion(self):
        print("\n======="
              f"\nMarca: {self.marca}"
              f"\nTipo: {self.tipo}"
              f"\nNumero de Serie: {self.numero_serie}")
    
    def obtener_marca(self):
        return self.marca