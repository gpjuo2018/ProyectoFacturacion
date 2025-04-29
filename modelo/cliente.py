# modelo/cliente.py
from modelo.factura import Factura

class Cliente:
    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
        self.facturas = []

    def agregar_factura(self, factura: Factura):
        self.facturas.append(factura)

    def calcular_total_compras(self):
        return sum(factura.valor_total for factura in self.facturas)
