# modelo/cliente.py
from modelo.factura import Factura

class Cliente:
    def __init__(self, nombre: str, cedula: str):
        self._nombre = nombre
        self._cedula = cedula
        self._facturas = []

    def _agregar_factura(self, factura: Factura):
        self.facturas.append(factura)

    def _calcular_total_compras(self):
        return sum(factura.valor_total for factura in self.facturas)
