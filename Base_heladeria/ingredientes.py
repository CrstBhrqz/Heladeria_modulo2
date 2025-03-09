from abc import ABC, abstractmethod

class Ingredientes(ABC):
    def __init__(self,nombre: str,  precio: float, num_calorias_porc: float, vegetariano: bool):
        self._nombre = nombre
        self._precio = precio
        self._num_calorias_porc = num_calorias_porc
        self._vegetariano = vegetariano
        self._inventario = 0


    # ------------------------------->Getters<--------------------------------
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def precio(self) -> float:
        return self._precio
    
    # Getter y Setter para num_calorias_porc
    @property
    def num_calorias_porc(self) -> float:
        return self._num_calorias_porc
    
    # Getter y Setter para inventario
    @property
    def inventario(self) -> float:
        return self._inventario
    
    # Getter y Setter para vegetariano
    @property
    def vegetariano(self) -> bool:
        return self._vegetariano
    
    # ------------------------------->Setters<--------------------------------
    @nombre.setter
    def nombre(self, value: str):
        if not value:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = value

    # Getter y Setter para precio

    @precio.setter
    def precio(self, value: float):
        if value < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = value



    @num_calorias_porc.setter
    def num_calorias_porc(self, value: float):
        if value < 0:
            raise ValueError("Las calorías no pueden ser negativas")
        self._num_calorias_porc = value



    @inventario.setter
    def cantidad(self, value: float):
        if value < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._inventario = value

    @vegetariano.setter
    def vegetariano(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("El valor de vegetariano debe ser True o False")
        self._vegetariano = value
    
    
    # ------------------------------->Metodos<--------------------------------
    
    def es_sano(self) -> bool:
        if self.num_calorias_porc <= 100 or self.vegetariano == True:
            return True
        return False
    
    @abstractmethod
    def abasteser(self):
        pass
    
    @abstractmethod
    def consumir_ingrediente(self):
        pass
    
    @abstractmethod
    def renovar_inventario(self):
        pass    