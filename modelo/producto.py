# modelo/producto.py
from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"
