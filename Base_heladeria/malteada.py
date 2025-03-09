from producto import IProducto


class Malteada(IProducto):
    def __init__(self, nombre: str, precio_publico: float, volumen: float, ingredientes: list):
        self._nombre = nombre
        self._precio = precio_publico
        self._volumen = volumen
        self.ingredientes = ingredientes  # Lista de 3 Ingrediente

    def calcular_costo(self) -> float:
        return sum(ing._precio for ing in self.ingredientes) + 500
    
    def calcular_calorias(self) -> float:
        return sum(ing._calorias for ing in self.ingredientes) + 200
    
    def calcular_rentabilidad(self) -> float:
        return self._precio - self.calcular_costo()
    
    def ingredientes_producto(self) -> list:
        ingredientes = []
        for ingrediente in self.ingredientes:
            ingredientes.append(ingrediente)
        return ingredientes
    
    
    def consumir_ingredientes(self):
        print("Consumiendo los ingredientes de la Malteada...")
        for ingrediente in self.ingredientes:
            ingrediente.consumir_ingrediente()