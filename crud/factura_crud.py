from modelo.factura import Factura
from datetime import date

facturas = []  # Lista para almacenar facturas

def crear_factura(fecha: date) -> Factura:
    factura = Factura(fecha)
    facturas.append(factura)
    return factura

def leer_facturas() -> list:
    return facturas

def buscar_factura(fecha: date) -> Factura:
    for factura in facturas:
        if factura.fecha == fecha:
            return factura
    return None

def eliminar_factura(factura: Factura) -> bool:
    global facturas
    facturas = [f for f in facturas if f != factura]
    return True

def agregar_producto_control(factura: Factura, producto_control) -> bool:
    factura._agregar_producto_control(producto_control)
    return True

def agregar_antibiotico(factura: Factura, antibiotico) -> bool:
    factura._agregar_antibiotico(antibiotico)
    return True

