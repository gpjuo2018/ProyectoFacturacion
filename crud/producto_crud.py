from modelo.plaguicida import Plaguicida
from modelo.fertilizante import Fertilizante
from modelo.antibiotico import Antibiotico

productos = []  # Lista para almacenar productos

def crear_producto(tipo: str, *args, **kwargs):
    if tipo == "Plaguicida":
        producto = Plaguicida(*args, **kwargs)
    elif tipo == "Fertilizante":
        producto = Fertilizante(*args, **kwargs)
    elif tipo == "Antibiotico":
        producto = Antibiotico(*args, **kwargs)
    else:
        raise ValueError("Tipo de producto no válido")
    productos.append(producto)
    return producto

def leer_productos() -> list:
    return productos

def eliminar_producto(producto) -> bool:
    global productos
    productos = [p for p in productos if p != producto]
    return True