from producto import IProducto


class Copa(IProducto):
    def __init__(self, nombre: str, precio_publico: float, tipo_vaso: str, ingredientes: list):
        self._nombre = nombre
        self._precio = precio_publico
        self._tipo_vaso = tipo_vaso
        self.ingredientes = ingredientes  # Lista de 3 Ingrediente

    def calcular_costo(self) -> float:
        return sum(ing._precio for ing in self.ingredientes)
    
    def calcular_calorias(self) -> float:
        calorias = sum(ing._calorias for ing in self.ingredientes)
        return calorias
    

    def calcular_rentabilidad(self) -> float:
        return self._precio - self.calcular_costo()
    
    def ingredientes_producto(self) -> list:
        ingredientes = []
        for ingrediente in self.ingredientes:
            ingredientes.append(ingrediente)
        return ingredientes
    
    def consumir_ingredientes(self):
        print("Consumiendo los ingredientes de la Copa...")
        for ingrediente in self.ingredientes:
            ingrediente.consumir_ingrediente()
    