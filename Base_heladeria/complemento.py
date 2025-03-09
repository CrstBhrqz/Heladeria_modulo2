from ingredientes import Ingredientes

class Complemento(Ingredientes):
    def __init__(self, nombre: str, precio: float, num_calorias_porc: float, vegetariano: bool):
        super().__init__(nombre, precio, num_calorias_porc, vegetariano)
        
    def abasteser(self):
        self._inventario += 10
    
    def renovar_inventario(self):
        self._inventario = 0
        
            
    def consumir_ingrediente(self):
        self._inventario -= 1
        