from modelo.cliente import Cliente

clientes = []  # Lista para almacenar clientes

def crear_cliente(nombre: str, cedula: str) -> Cliente:
    cliente = Cliente(nombre, cedula)
    clientes.append(cliente)
    return cliente

def leer_clientes() -> list:
    return clientes

def buscar_cliente(cedula: str) -> Cliente:
    for cliente in clientes:
        if cliente.cedula == cedula:
            return cliente
    return None

def eliminar_cliente(cedula: str) -> bool:
    global clientes
    clientes = [c for c in clientes if c.cedula != cedula]
    return True
