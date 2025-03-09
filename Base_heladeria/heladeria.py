class Heladeria:
    def __init__(self, productos: list):
        if len(productos) != 4:
            raise ValueError("Debe tener 4 productos")
        self.productos = productos
        self.ventas_dia = 0
    
    def producto_mas_rentable(self):
        rentabilidades = {p._nombre: p.calcular_rentabilidad() for p in self.productos}
        return max(rentabilidades, key=rentabilidades.get)
    
    def vender(self, producto):
        
        
        print(f'-----Vender.-----------------{producto}')
        
        encontrado = False
        
        # validar si existe el producto
        for p in self.productos:
            if p._nombre == producto:
                encontrado = True
                print(f"Se vendio {p._nombre}")
                producto_para_vender = p
                break
                
                
        if not encontrado:
            return print("Producto no encontrado")
            
        #validar disponibilidad de producto a vender
        
        print(producto_para_vender.ingredientes_producto())
        
        bases = 0
        complementos = 0

        for ingrediente in producto_para_vender.ingredientes_producto():

            if ingrediente._inventario == 0:
                return print(f'No hay inventario de {ingrediente._nombre} para el producto {producto_para_vender._nombre}')
            if type(ingrediente).__name__ == "Base":
                bases += 1
            if type(ingrediente).__name__ == "Complemento":
                complementos += 1


        if bases != 1 and complementos != 2:
            return print(f'Producto mal armado')

        
        
        producto_para_vender.consumir_ingredientes()

        self.ventas_dia += 1
        print("Ventas EXITOSA ")
        return True
            

        