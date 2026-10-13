# Inventario de equipos con persistencia en JSON.
import json

ARCHIVO = "equipos.json"


def cargar():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def guardar(equipos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(equipos, f, indent=2, ensure_ascii=False)


def agregar(equipos):
    nombre = input("Nombre del equipo: ")
    marca = input("Marca: ")
    cantidad = int(input("Cantidad: "))
    if cantidad > 0:
        equipos.append({"nombre": nombre, "marca": marca, "cantidad": int(cantidad)})
        guardar(equipos)
    else:
        print("La cantidad debe ser mayor que cero.")


def listar(equipos):
    print("\n--- Inventario ---")
    for e in equipos:
        print(f"- {e['nombre']} x{e['cantidad']}")
    print(f"Tipos de equipo: {len(equipos)}")


def buscar_por_marca(equipos):
    marca = input("Marca a buscar: ").lower()
    encontrados = [e for e in equipos if e["marca"].lower() == marca]
    if encontrados:
        for e in encontrados:
            print(f"- {e['nombre']} x{e['cantidad']}")
    else:
        print("No hay equipos de esa marca.")


def reporte(equipos):
    total_unidades = 0
    for e in equipos:
        total_unidades += e["cantidad"]

    if len(equipos) > 0:
        promedio = total_unidades / len(equipos)
    else:
        promedio = 0

    print(f"\nTotal de unidades: {total_unidades}")
    print(f"Promedio por tipo de equipo: {promedio:.1f}")


def main():
    equipos = cargar()
    while True:
        print("\n1. Agregar  2. Listar  3. Buscar por marca  4. Reporte  5. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            agregar(equipos)
        elif opcion == "2":
            listar(equipos)
        elif opcion == "3":
            buscar_por_marca(equipos)
        elif opcion == "4":
            reporte(equipos)
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")
if __name__ == "__main__": 
    main()
