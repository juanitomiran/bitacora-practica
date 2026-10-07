# Ejercicio 3 · Que no se pierdan los datos

## Objetivo
Ahora mismo, cuando cierras `ejercicio1.py`, el inventario se borra porque la lista vive solo en memoria. Tu tarea es que el inventario se guarde en un archivo `equipos.json` y se recupere al abrir el programa.

## Requisitos
- Al abrir el programa, carga lo que había en `equipos.json`.
- Al agregar un equipo, guarda en el archivo.
- Si el archivo no existe todavía, el programa **no debe reventar**: parte con la lista vacía.

## Antes de empezar
1. Trabaja en una copia: `cp ejercicio1.py ejercicio3.py` y edita `ejercicio3.py`.
2. Borra el `equipos.json` que está en la carpeta (está vacío). Tu programa lo creará solo.
3. Revisa la opción 1 de tu menú: hay un error. `lista_equipo.append(lista_equipo)` agrega la lista dentro de sí misma. Piensa qué debería agregarse en su lugar y corrígelo antes de guardar nada.

## Pasos

### Paso 1: importar `json`
Al inicio del archivo, agrega `import json`. Es el módulo de Python que convierte listas y diccionarios a texto y de vuelta.

### Paso 2: función `cargar()`
Crea una función que:
- abra `equipos.json` en modo lectura (`"r"`) con `with open(...) as f`,
- devuelva `json.load(f)`,
- si el archivo no existe, devuelva `[]`.

Pista: usa `try` / `except FileNotFoundError`.

### Paso 3: función `guardar(lista)`
Crea una función que:
- abra `equipos.json` en modo escritura (`"w"`),
- escriba la lista con `json.dump(lista, f, indent=2)`.

Ojo: `"w"` reemplaza todo el archivo, por eso se guarda **la lista completa**, no solo el equipo nuevo.

### Paso 4: conectarlo al programa
- Reemplaza la línea `lista_equipo = [...]` del inicio por `lista_equipo = cargar()`.
- En la opción 1, justo después de agregar el equipo, llama a `guardar(lista_equipo)`.

## Cómo probar (hazlo en este orden)
1. Borra `equipos.json` y ejecuta el programa. **No debe dar error** y la lista debe estar vacía.
2. Agrega 2 equipos con la opción 1 y sal con la opción 4.
3. Abre `equipos.json` y comprueba que los equipos están ahí.
4. Ejecuta el programa de nuevo y usa la opción 2. Los equipos deben seguir apareciendo.

## Preguntas para pensar
- ¿Qué pasa si `equipos.json` existe pero está vacío (0 bytes)? Pruébalo con `touch equipos.json`. ¿Qué error aparece y cómo lo manejarías?
- ¿Por qué `guardar()` se llama después de agregar y no antes?
- ¿Qué pasaría con `lista_marca`? ¿También debería guardarse? ¿Cómo lo harías?

## Entrega
Haz commit de `ejercicio3.py` con un mensaje claro (por ejemplo `feat: inventario persistente en equipos.json`) y anota en tu bitácora qué problemas encontraste.
