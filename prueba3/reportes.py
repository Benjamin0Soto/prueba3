
import json

def generar_reporte_categorias():
    with open("biblioteca.json", mode="r") as file:
        datos = json.load(file)
    
    categorias = {categoria['CategoriaID']: categoria['Nombre'] for categoria in datos['Categoria']}
    conteo_categorias = {categoria: 0 for categoria in categorias.values()}
    
    for libro in datos['Libro']:
        categoria_nombre = categorias[libro['CategoriaID']]
        conteo_categorias[categoria_nombre] += 1
    
    with open("Reportes_biblioteca_mundo_libro.json", mode="w") as reporte_file:
        json.dump(conteo_categorias, reporte_file, indent=4)
    
    print("\n****************************************")
    print("*  categoria      -  cantidad de libros  *")
    print("****************************************")
    for categoria, cantidad in conteo_categorias.items():
        print(f"{categoria:<30} {cantidad}")

    print("Reporte generado exitosamente.")