def validar_credenciales(login, clave):
    with open("login.txt", "r") as file_login, open("clave.txt", "r") as file_clave:
        logins = file_login.read().splitlines()
        claves = file_clave.read().splitlines()
        if login in logins and clave in claves:
            return True
        else:
            return False

def listar_personas():
    try:
        with open("dni.txt", "r") as file_dni, open("nombre.txt", "r") as file_nombre, open("apellido.txt", "r") as file_apellido:
            dni = file_dni.read().splitlines()
            nombres = file_nombre.read().splitlines()
            apellidos = file_apellido.read().splitlines()
            if len(dni) == len(nombres) == len(apellidos):
                print("Datos de las personas:")
                print("DNI\t\tNombre\t\tApellido")
                for i in range(len(dni)):
                    print(f"{dni[i]}\t\t{nombres[i].ljust(15)}\t\t{apellidos[i].ljust(15)}")
            else:
                print("Error: Los archivos de datos no tienen la misma cantidad de registros.")
    except FileNotFoundError:
        print("Error: No se encontraron los archivos necesarios.")

def agregar_persona(dni, nombre, apellido):
    try:
        # Si el nombre no está presente, agregar la nueva persona
        with open("dni.txt", "a") as file_dni, open("nombre.txt", "a") as file_nombre, open("apellido.txt", "a") as file_apellido:
            file_dni.write(dni + "\n")
            file_nombre.write(nombre + "\n")
            file_apellido.write(apellido + "\n")
        print("Persona agregada exitosamente.")
    except IOError:
        print("Error al escribir en los archivos.")


intentos = 0
while intentos < 2:
    login = input("Ingrese su login: ")
    clave = input("Ingrese su clave: ")
    if validar_credenciales(login, clave):
        print("Bienvenido al programa.")
        while True:
            print("Menú:")
            print("1. Listar personas")
            print("2. Agregar personas")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                listar_personas()
            elif opcion == "2":
                dni = input("Ingrese el DNI: ")
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                agregar_persona(dni, nombre, apellido)
            elif opcion == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
    else:
        print("Login o clave incorrectos. Intente nuevamente.")
        intentos += 1
else:
    print("Ha excedido el número de intentos permitidos. El programa terminará.")
