from base import Base
from complemento import Complemento
from heladeria import Heladeria

from copa import Copa
from malteada import Malteada


# Crear una Base (es un tipo de Ingrediente)
base_fresa = Base(nombre="Helado de Fresa",precio=1200,num_calorias_porc=150,vegetariano=True,sabor_extra="fresa")
complemento_chispas = Complemento(nombre="Chispas de chocolate",precio=500,num_calorias_porc=200,vegetariano=False)
complemento_mani = Complemento(nombre="Mani",precio=500,num_calorias_porc=200,vegetariano=False)    

base_fresa.abasteser()
complemento_chispas.abasteser()
complemento_mani.abasteser()   

print(base_fresa._inventario)
print(complemento_chispas._inventario)
print(complemento_mani._inventario) 


copa_samurai_fresa = Copa(
    nombre="Samurai de Fresas",
    precio_publico=7500,
    tipo_vaso="Vaso de cartón",
    ingredientes=[base_fresa, complemento_chispas, complemento_mani]  # Lista de 3 objetos Ingrediente
)



# Ingredientes de la Copa (Base + 2 Complementos)
base_mandarina = Base(nombre="Helado de Mandarina", precio=1500, num_calorias_porc=130, vegetariano=True, sabor_extra="mandarina")
complemento_galleta = Complemento(nombre="Galleta", precio=300, num_calorias_porc=80, vegetariano=True)
complemento_sirope = Complemento(nombre="Sirope de Mango", precio=200, num_calorias_porc=50, vegetariano=True)

base_mandarina.abasteser()
complemento_galleta.abasteser()
complemento_sirope.abasteser()

print(base_mandarina._inventario)
print(complemento_galleta._inventario)
print(complemento_sirope._inventario)


copa_samurai_mandarina = Copa(
    nombre="Samurai de mandarinas",
    precio_publico=4500,  # Precio al público
    tipo_vaso="Vaso de cartón",
    ingredientes=[base_mandarina, complemento_galleta, complemento_sirope]
)



base_chocolate = Base(nombre="Helado de Chocolate",precio=1800, num_calorias_porc=200,vegetariano=False,sabor_extra="chocolate")
complemento_chispas = Complemento(nombre="Chispas de Chocolate",precio=500,num_calorias_porc=150,vegetariano=False)
complemento_crema = Complemento(nombre="Crema Chantilly", precio=600,num_calorias_porc=300,vegetariano=True)


base_chocolate.abasteser()
complemento_chispas.abasteser()
complemento_crema.abasteser()




malteada_choco = Malteada(
    nombre="Malteada Choco Espacial",
    precio_publico=7500,
    volumen=12,  # Volumen en onzas (atributo específico de Malteada)
    ingredientes=[base_chocolate, complemento_chispas, complemento_crema]
)



base_vainilla = Base(nombre="Helado de Vainilla", precio=1700, num_calorias_porc=180, vegetariano=True, sabor_extra="vainilla")
complemento_fresas = Complemento(nombre="Fresas", precio=700, num_calorias_porc=50, vegetariano=True)
complemento_miel = Complemento(nombre="Miel", precio=400, num_calorias_porc=120, vegetariano=True)

malteada_vainilla = Malteada(
    nombre="Malteada Vainilla Delicia",
    precio_publico=7200,
    volumen=12,
    ingredientes=[base_vainilla, complemento_fresas, complemento_miel]
)




# Crear la Heladería con los 4 productos
heladeria = Heladeria(productos=[copa_samurai_fresa, copa_samurai_mandarina, malteada_choco, malteada_vainilla])

heladeria.ventas_dia = 1000

print("-----Producto mas rentable.-----------------")
print(heladeria.producto_mas_rentable())


print("-----Vender.-----------------")
print(heladeria.vender("Samurai de Fresas"))


# print(base_fresa._inventario)
# print(complemento_chispas._inventario)
# print(complemento_mani._inventario) 