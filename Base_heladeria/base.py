from ingredientes import Ingredientes

class Base(Ingredientes):
    def __init__(self, nombre: str,  precio: float, num_calorias_porc: float,  vegetariano: bool,sabor_extra : str):
      
        super().__init__(nombre,  precio, num_calorias_porc, vegetariano)
        self._sabor_extra = sabor_extra
    
    # ------------------------------->Getters<--------------------------------
    @property
    def sabor_extra(self) -> str:
        return self._sabor_extra    
    
    # ------------------------------->Setters<--------------------------------
    
    @sabor_extra.setter
    def sabor_extra(self, value: str):
        if not value:
            raise ValueError("El nombre no puede estar vacío")
        self.sabor_extra = value
    
    #----------------------------->Metodos<---------------------------------
    def abasteser(self ):
        self._inventario += 5
    
    def renovar_inventario(self):
        self._inventario = 0
    
    def consumir_ingrediente(self):
        self._inventario -= 1
        
    