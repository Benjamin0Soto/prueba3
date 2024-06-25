print("")

import json

def agregarUsuario(nombre:str,email:str,fechaRegistro:str):
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

agregarUsuario(nombre,email,fechaRegistro)



def editarUsuario(nombre:str,email:str):
     with open("biblioteca.json", mode="w") as ArchivoJson:
        json.dump(ArchivoJson, indent=4)

nombre = input(" ingrese nuevo nombre del usuario: \n")
email = input(" ingrese nuevo email del ususario: \n")

editarUsuario(nombre,email)



def eliminarUsuario():
        with open("biblioteca.json", mode="w") as ArchivoJson:
         json.dump( ArchivoJson, indent=4)



def buscarUsuario():
     with open("biblioteca.json", mode="w") as ArchivoJson:
        json.dump( ArchivoJson, indent=4)



def volver():
     with open("biblioteca.json", mode="w") as ArchivoJson:
        json.dump( ArchivoJson, indent=4)

