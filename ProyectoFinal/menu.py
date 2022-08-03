import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print("  Bienvenido al gestor  ")
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print("[1] Listar los clientes")
        print("[2] Buscar un cliente")
        print("[3] Añadir un cliente")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente")
        print("[6] Salir")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == "1":
            print("Listando los clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)
        elif opcion == "2":
            print("Buscando al cliente...\n")
            dni = helpers.leer_texto("Ingrese DNI", 3, 3).upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado")
        elif opcion == "3":
            print("Añadiendo al cliente...\n")
            dni = None
            while True:
                dni = helpers.leer_texto("Ingrese DNI", 3, 3).upper()
                if helpers.validar_dni(dni, db.Clientes.lista):
                    break
            nombre = helpers.leer_texto("Ingrese Nombre", 2, 30).capitalize()
            apellido = helpers.leer_texto("Ingrese Apellido", 2, 30).capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadadido correctamente")
        elif opcion == "4":
            print("Modificando al cliente...\n")
            dni = helpers.leer_texto("Ingrese DNI", 3, 3).upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(f"Ingrese Nombre [{cliente.nombre}]", 2, 30).capitalize()
                apellido = helpers.leer_texto(f"Ingrese Apellido [{cliente.apellido}]", 2, 30).capitalize()
                db.Clientes.modificar(cliente.dni, nombre, apellido)
                print("Cliente modificado correctamente")
            else:
                print("Cliente no encontrado")
        elif opcion == "5":
            print("Borrando al cliente...\n")
            dni = helpers.leer_texto("Ingrese DNI", 3, 3).upper()
            cliente = db.Clientes.buscar(dni)
            print("Cliente borrado correctamente") if db.Clientes.borrar(dni) else print("Cliente no encontrado")
        elif opcion == "6":
            print("Saliendo...\n")
            break
            
        input("\nPresiona ENTER para continuar...")


