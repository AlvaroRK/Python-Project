DB = {}

# Creamos la funcion de register
def register():
  name = input("Ingrese su nombre de usuario: ")
  password = input("Ingrese su contraseña: ")
  if password.lower() == name.lower():
    print("Error: tu contraseña no puede ser igual a tu nombre")
  else:
    DB.update({name: password})

# Creamos la funcion para leer los registers
def readData(DB):
  for key,value in zip(DB,DB.values()):
    print(f"Tu nombre es: {key} y tu contraseña es: {value}")

# Guardamos la data en un archivo .txt
def saveData(DB):
    rute = 'D:/programación/CursosPy/CoderHouse Python/Pre-entregas'
    with open(rute+'/mostrarDatos.txt','w', encoding="UTF-8") as file:
        for key,value in zip(DB,DB.values()):
            clients = [f"{key}: {value}\n"]
            file.writelines(clients)

# Hacemos un sistema de login en base a los usuarios que esten registrados
def login(DB):
    print("Iniciando sesión...")
    nameLogin = input("Ingrese su nombre de usuario: ")
    passwordLogin = input("Ingrese su contraseña: ")
    try:
        if nameLogin and passwordLogin == DB[nameLogin]:
            print(f"Usuario y contraseña correctos\nBienvenido {nameLogin}")
        else:
            print("Error: tu contraseña es incorrecta")
    except:
        print("Error: no existe el usuario")