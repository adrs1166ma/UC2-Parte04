
def validar_credenciales(login, clave):
    with open("login.txt", "r") as file_login, open("clave.txt", "r") as file_clave:
        logins = file_login.read().splitlines()
        claves = file_clave.read().splitlines()
        if login in logins and clave in claves:
            return True
        else:
            return False

intentos = 0
while intentos < 2:
    login = input("Ingrese su login: ")
    clave = input("Ingrese su clave: ")
    if validar_credenciales(login, clave):
        print("Bienvenido al programa.")
        print("Menú:")
        print("1. Listar personas")
        print("2. Agregar personas")
        print("3. Salir")
        break
    else:
        print("Login o clave incorrectos. Intente nuevamente.")
        intentos += 1
else:
    print("Ha excedido el número de intentos permitidos. El programa terminará.")