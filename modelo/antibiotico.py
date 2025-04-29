# modelo/antibiotico.py
from modelo.producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre: str, precio: float, dosis: int, tipo_animal: str):
        super().__init__(nombre, precio)
        if not (400 <= dosis <= 600):
            raise ValueError("La dosis debe estar entre 400 y 600 kg.")
        self.dosis = dosis
        self.tipo_animal = tipo_animal

    def __str__(self):
        return f"{super().__str__()} | Dosis: {self.dosis}kg | Animal: {self.tipo_animal}"
