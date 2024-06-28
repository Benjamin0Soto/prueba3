print("")

import json

""" def agregarUsuario(nombre:str,email:str,fechaRegistro:str):
    with open("biblioteca.json", mode="r") as archivoJson:
            leerJson = json.load(archivoJson)
            usuario = {
             "UsuarioID": len(leerJson["Usuario"])+1,
             "Nombre": "a",
             "Email": "a@b.com",
             "FechaRegistro": "1-2-3"
            }
            leerJson["Usuario"].append(usuario)

    with open("biblioteca.json", mode="w") as nuevoUsuarioJson:
        json.dump(leerJson, nuevoUsuarioJson, indent=4)


nombre = input(" ingrese nombre del usuario: \n")
email = input(" ingrese email del ususario: \n")
fechaRegistro = input(" ingrese la fecha de registro:")

agregarUsuario(nombre,email,fechaRegistro) """

def agregarUsuario(datos):
    nuevoUsuario = {
        "UsuarioID": len(datos['Usuario']) + 1,
        "Nombre": input("Nombre: "),
        "Email": input("Email: "),
        "FechaRegistro": input("Fecha de Registro (AAAA-MM-DD): ")
    }
    datos['Usuario'].append(nuevoUsuario)
    print("Usuario agregado exitosamente.")

def editarUsuario(datos):
    usuarioId = int(input("Ingrese el ID del usuario a editar: "))
    for usuario in datos['Usuario']:
        if usuario['UsuarioID'] == usuarioId:
            usuario['Nombre'] = input("Nombre: ")
            usuario['Email'] = input("Email: ")
            usuario['FechaRegistro'] = input("Fecha de Registro (AAAA-MM-DD): ")
            print("Usuario editado exitosamente.")
            return
    print("Usuario no encontrado.")

def eliminarUsuario(datos):
    usuarioId = int(input("Ingrese el ID del usuario a eliminar: "))
    for usuario in datos['Usuario']:
        if usuario['UsuarioID'] == usuarioId:
            datos['Usuario'].remove(usuario)
            print("Usuario eliminado exitosamente.")
            return
    print("Usuario no encontrado.")

def buscarUsuario(datos):
    usuarioId = int(input("Ingrese el ID del usuario a buscar: "))
    for usuario in datos['Usuario']:
        if usuario['UsuarioID'] == usuarioId:
            print(f"ID: {usuario['UsuarioID']}, Nombre: {usuario['Nombre']}, Email: {usuario['Email']}, FechaRegistro: {usuario['FechaRegistro']}")
            return
    print("Usuario no encontrado.")