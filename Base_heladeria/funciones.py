def esto_es_sano(ingrediente: dict):
    if ingrediente["num_calorias_porc"] <= 100 or ingrediente["vegetariano"] == True:
        return True

    return False

def calorias(ingredientes: list):
    calorias_totales = 0
    for ingrediente in ingredientes:
        calorias_totales += ingrediente["num_calorias_porc"]

    return round(calorias_totales*0.95, 2)

def costo(ingredientes: list):
    costo_total = 0
    for ingrediente in ingredientes:
        costo_total += ingrediente["precio"]

    return costo_total

def rentabilidad(ingredientes: list):
    return round( costo(ingredientes) / calorias(ingredientes), 2)

def mejor_producto(productos: list):
    pass
