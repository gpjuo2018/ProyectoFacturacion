from crud.cliente_crud import crear_cliente, leer_clientes, actualizar_cliente, eliminar_cliente
from crud.factura_crud import crear_factura, agregar_producto_a_factura, leer_facturas
from crud.producto_crud import crear_producto, leer_productos
from datetime import date

def mostrar_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear cliente")
        print("2. Ver clientes")
        print("3. Crear factura para cliente")
        print("4. Ver facturas de un cliente")
        print("5. Buscar cliente por cédula")
        print("6. Gestionar productos")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            cedula = input("Ingrese la cédula del cliente: ")
            cliente = crear_cliente(nombre, cedula)
            print(f"Cliente creado: {cliente.nombre} ({cliente.cedula})")
        elif opcion == "2":
            clientes = leer_clientes()
            print("\n--- Lista de Clientes ---")
            for cliente in clientes:
                print(f"Nombre: {cliente.nombre}, Cédula: {cliente.cedula}")
        elif opcion == "3":
            clientes = leer_clientes()
            print("\n--- Seleccione un Cliente ---")
            for i, cliente in enumerate(clientes):
                print(f"{i}. {cliente.nombre} ({cliente.cedula})")
            cliente_id = int(input("Seleccione el índice del cliente: "))
            if 0 <= cliente_id < len(clientes):
                cliente = clientes[cliente_id]
                factura = crear_factura(date.today())
                cliente.agregar_factura(factura)
                print(f"Factura creada para {cliente.nombre} con fecha: {factura.fecha}")
            else:
                print("Cliente no encontrado.")
        elif opcion == "4":
            clientes = leer_clientes()
            print("\n--- Seleccione un Cliente ---")
            for i, cliente in enumerate(clientes):
                print(f"{i}. {cliente.nombre} ({cliente.cedula})")
            cliente_id = int(input("Seleccione el índice del cliente: "))
            if 0 <= cliente_id < len(clientes):
                cliente = clientes[cliente_id]
                print(f"\n--- Facturas de {cliente.nombre} ---")
                for factura in cliente.facturas:
                    print(f"Fecha: {factura.fecha}, Total: {factura.calcular_total()}")
            else:
                print("Cliente no encontrado.")
        elif opcion == "5":
            buscar_por_cedula()
        elif opcion == "6":
            gestionar_productos()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_productos():
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Crear producto")
        print("2. Ver productos")
        print("3. Agregar producto a factura")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo_producto = input("Ingrese el tipo de producto (Plaguicida/Fertilizante/Antibiotico): ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            if tipo_producto == "Antibiotico":
                dosis = int(input("Ingrese la dosis: "))
                tipo_animal = input("Ingrese el tipo de animal: ")
                crear_producto(tipo_producto, nombre, precio, dosis, tipo_animal)
            else:
                registro_ica = input("Ingrese el registro ICA: ")
                cantidad = int(input("Ingrese la cantidad: "))
                if tipo_producto == "Plaguicida":
                    periodo_carencia = int(input("Ingrese el periodo de carencia: "))
                    crear_producto(tipo_producto, nombre, precio, registro_ica, cantidad, periodo_carencia)
                elif tipo_producto == "Fertilizante":
                    fecha_aplicacion = date.fromisoformat(input("Ingrese la fecha de última aplicación (YYYY-MM-DD): "))
                    crear_producto(tipo_producto, nombre, precio, registro_ica, cantidad, fecha_aplicacion)
            print("Producto creado exitosamente.")
        elif opcion == "2":
            productos = leer_productos()
            print("\n--- Lista de Productos ---")
            for producto in productos:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}")
        elif opcion == "3":
            facturas = leer_facturas()
            print("\n--- Seleccione una Factura ---")
            for i, factura in enumerate(facturas):
                print(f"{i}. Fecha: {factura.fecha}")
            factura_id = int(input("Seleccione el índice de la factura: "))
            if 0 <= factura_id < len(facturas):
                factura = facturas[factura_id]
                productos = leer_productos()
                print("\n--- Seleccione un Producto ---")
                for i, producto in enumerate(productos):
                    print(f"{i}. {producto.nombre} (Precio: {producto.precio})")
                producto_id = int(input("Seleccione el índice del producto: "))
                if 0 <= producto_id < len(productos):
                    producto = productos[producto_id]
                    agregar_producto_a_factura(factura, producto)
                    print("Producto agregado a la factura.")
                else:
                    print("Producto no encontrado.")
            else:
                print("Factura no encontrada.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def buscar_por_cedula():
    cedula = input("Ingrese la cédula del cliente: ")
    clientes = leer_clientes()
    cliente_encontrado = next((cliente for cliente in clientes if cliente.cedula == cedula), None)

    if cliente_encontrado:
        print(f"\n--- Facturas de {cliente_encontrado.nombre} ({cliente_encontrado.cedula}) ---")
        if cliente_encontrado.facturas:
            for factura in cliente_encontrado.facturas:
                print(f"\nFactura del {factura.fecha} - Total: ${factura.calcular_total():.2f}")
                print("Productos vendidos:")
                for producto in factura.mostrar_productos():
                    print(f"- {producto}")
        else:
            print("Este cliente no tiene facturas registradas.")
    else:
        print("Cliente no encontrado.")

if __name__ == "__main__":
    mostrar_menu()