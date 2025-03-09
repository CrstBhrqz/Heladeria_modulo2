
from abc import ABC, abstractmethod


class IProducto(ABC):
    
    @abstractmethod
    def calcular_costo(self):
        pass
    
    @abstractmethod
    def calcular_rentabilidad(self):
        pass
    
    @abstractmethod
    def calcular_calorias(self):
        pass
    
    @abstractmethod
    def ingredientes_producto(self):
        pass
    
    @abstractmethod
    def consumir_ingredientes(self):
        pass
    
