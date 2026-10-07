

#Ejercicio 1: crear un menu de inventario
import json

def cargar_data():
    try:
        with open('equipos.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return []


def guardar(lista):
    with open('equipos.json', 'w', encoding='utf-8') as archivo:
        json.dump(lista, archivo, indent=2)










lista_marca= ["hp", "lenovo", "dell", "samsung", "apple"]
print("\n --- INVENTARIO ---")
lista_equipo = cargar_data()
while True:
     print("1. agregar equipo")
     print("2. listar equipo")
     print("3. buscar equipo por marca")
     print("4. salir del programa")
     print("5. cantidad total que hay de equipos en el inventario")
     print("6. cantidad total que hay de marca en el inventario")
     print("7. cual es la marca mas repetida en el inventario")
     #Esto es parte del ejercicio 2, las opciones 5, 6 y 7 son parte del ejercicio 2

     opcion = input("seleccione una opcion: ")
     if opcion == "1":
        nombre = input("Ingresa el nombre del equipo: ")
        
       
        if nombre in lista_equipo:
            print("El equipo ya existe en el inventario.")
        else:
            lista_equipo.append(nombre)
            guardar(lista_equipo)  
            print("¡Equipo agregado y guardado con éxito!")
            
     elif opcion == "2":
         print("equipos en inventario: ")
         for equipo in (lista_equipo):
             print(equipo)
     elif opcion == "3":
             marca = input("ingrese la marca del equipo para buscar:")
             if marca in lista_marca:
                 print("el equipo de la marca", [lista_marca], "se encuentra en el inventario")
             else:
                 print("el equipo de la marca no se encuentra en el inventario")
     elif opcion == "4":
             print("saliendo del programa...")
             break
            
     elif opcion == "5":
         print("la cantidad de equipos que hay en el inventario es:", len(lista_equipo))
     elif opcion == "6":
         print("la cantidad de marcas que hay en el inventario es:", len(lista_marca))
     elif opcion == "7":
       print("la marca mas repetida del inventario es", max(set(lista_marca), key=lista_marca.count))
