print("")

import json
from funciones import agregarUsuario, editarUsuario, eliminarUsuario, buscarUsuario
from reportes import generar_reporte_categorias

def cargarDatos():
    with open("biblioteca.json", mode="r") as archivoJson:
        return json.load(archivoJson)

def guardarDatos(datos):
    with open("biblioteca.json", mode="w") as archivoJson:
        json.dump(datos, archivoJson, indent=4)

def menuPrincipal():
    while True:
        print("\n**********************")
        print("*  Mundo libro     *")
        print("**********************")
        print("[1]- Mantenedor de usuarios")
        print("[2]- Reportes")
        print("[3]- Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            menuUsuarios()
        elif opcion == '2':
            generar_reporte_categorias()
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menuUsuarios():
    datos = cargarDatos()
    
    while True:
        print("\n********************************")
        print("*  Mantenedor de usuarios     *")
        print("********************************")
        print("[1]- Agregar usuario")
        print("[2]- Editar usuario")
        print("[3]- Eliminar usuario")
        print("[4]- Buscar usuario")
        print("[5]- Volver")

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregarUsuario(datos)
        elif opcion == '2':
            editarUsuario(datos)
        elif opcion == '3':
            eliminarUsuario(datos)
        elif opcion == '4':
            buscarUsuario(datos)
        elif opcion == '5':
            guardarDatos(datos)
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menuPrincipal()