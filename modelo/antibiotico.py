# modelo/antibiotico.py
class Antibiotico:
    def __init__(self, nombre: str, precio: float, dosis: int, tipo_animal: str):
        self._nombre = nombre
        self._precio = precio
        self._dosis = dosis
        self._tipo_animal = tipo_animal

    def __str__(self):
        return f"{self._nombre} - ${self._precio:.2f} | Dosis: {self._dosis}kg | Animal: {self._tipo_animal}"
