# modelo/cliente.py
from modelo.factura import Factura

class Cliente:
    def __init__(self, nombre, cedula):
        self._nombre = nombre
        self._cedula = cedula
        self._facturas = []

    def agregar_factura(self, factura):
        self._facturas.append(factura)

    def obtener_nombre(self):
        return self._nombre

    def obtener_cedula(self):
        return self._cedula

    def obtener_facturas(self):
        return self._facturas
