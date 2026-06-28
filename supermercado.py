# ==========================================
# Sistema de Ventas para Supermercado
# Autor: Jhoan Burbano
# ==========================================

# Lista de productos
productos = {
    1: {"nombre": "Arroz", "precio": 1.50},
    2: {"nombre": "Leche", "precio": 0.95},
    3: {"nombre": "Pan", "precio": 0.50},
    4: {"nombre": "Huevos", "precio": 3.20},
    5: {"nombre": "Azúcar", "precio": 1.20}
}

# Carrito de compras
carrito = []


# ========= FUNCIONES =========

def mostrar_productos():
    print("\n====== PRODUCTOS DISPONIBLES ======")
    for codigo, producto in productos.items():
        print(f"{codigo}. {producto['nombre']} - ${producto['precio']:.2f}")

def agregar_producto():
    mostrar_productos()

    codigo = int(input("\nIngrese el código del producto: "))

    if codigo in productos:
        carrito.append(productos[codigo])
        print("Producto agregado correctamente.")
    else:
        print("Código inválido.")

def eliminar_producto():
    if len(carrito) == 0:
        print("\nEl carrito está vacío.")
        return

    print("\n======= CARRITO =======")

    for i, producto in enumerate(carrito, start=1):
        print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")

    opcion = int(input("\nIngrese el número del producto que desea eliminar: "))

    if 1 <= opcion <= len(carrito):
        eliminado = carrito.pop(opcion - 1)
        print(f"{eliminado['nombre']} eliminado del carrito.")
    else:
        print("Opción inválida.")

def calcular_total():

    if len(carrito) == 0:
        print("\nEl carrito está vacío.")
        return

    subtotal = 0

    for producto in carrito:
        subtotal += producto["precio"]

    iva = subtotal * 0.15
    total = subtotal + iva

    print("\n====== RESUMEN DE COMPRA ======")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA (15%): ${iva:.2f}")
    print(f"Total: ${total:.2f}")

def procesar_pago():

    if len(carrito) == 0:
        print("\nEl carrito está vacío.")
        return

    subtotal = 0

    for producto in carrito:
        subtotal += producto["precio"]

    iva = subtotal * 0.15
    total = subtotal + iva

    print(f"\nTotal a pagar: ${total:.2f}")

    dinero = float(input("Ingrese el dinero recibido: $"))

    if dinero < total:
        print("Dinero insuficiente.")
    else:
        cambio = dinero - total
        print(f"Cambio: ${cambio:.2f}")
        print("¡Compra realizada con éxito!")
        carrito.clear()

def menu():
    print("1. Mostrar productos")
    print("2. Agregar producto al carrito")
    print("3. Ver carrito")
    print("4. Eliminar producto del carrito")
    print("5. Calcular total")
    print("6. Procesar pago")
    print("7. Salir")   


# ========= PROGRAMA PRINCIPAL =========

while True:

    menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_productos()

    elif opcion == "2":
        agregar_producto()

    elif opcion == "3":

        if len(carrito) == 0:
            print("\nEl carrito está vacío.")

        else:
            print("\n======= CARRITO =======")

        total = 0

        for producto in carrito:
            print(f"{producto['nombre']} - ${producto['precio']:.2f}")
            total += producto["precio"]

        print("----------------------")
        print(f"Total: ${total:.2f}")
    
    elif opcion == "4":
        eliminar_producto()

    
    elif opcion == "5":
        calcular_total()

    elif opcion == "6":
        procesar_pago()

    elif opcion == "7":
        print("Gracias por utilizar el sistema.")
        break

    else:
        print("Opción inválida.")