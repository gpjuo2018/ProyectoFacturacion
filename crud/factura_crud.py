from modelo.factura import Factura
from datetime import date

facturas = []  # Lista para almacenar facturas

def crear_factura(fecha: date) -> Factura:
    factura = Factura(fecha)
    facturas.append(factura)
    return factura

def leer_facturas() -> list:
    return facturas

def agregar_producto_a_factura(factura: Factura, producto) -> bool:
    if factura in facturas:
        factura.agregar_producto(producto)
        return True
    return False

def eliminar_factura(factura: Factura) -> bool:
    global facturas
    facturas = [f for f in facturas if f != factura]
    return True