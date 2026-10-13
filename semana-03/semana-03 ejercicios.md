# Semana 3 — Desatorarte solo, y entender la web

**Objetivo:** que dejes de depender de otra persona para avanzar, y que entiendas qué pasa realmente cuando se abre una página web.

> Esta semana suele costar más que las anteriores. Es normal: la novedad se acabó y aparecen los errores. Que cueste significa que estás avanzando.

---

## Ejercicio 1 · Bug hunt ⭐

En la carpeta `bug-hunt/` está `inventario.py`, un programa de inventario con su archivo `equipos.json`. **Tiene 6 errores.** Algunos impiden que corra; otros no avisan.

**Tu tarea:** encuéntralos y arréglalos. Por cada uno, anota en un archivo `bugs.md`:
- qué error era,
- cómo te diste cuenta,
- cómo lo arreglaste.

**Reglas**
1. **Lee el error de abajo hacia arriba, en voz alta.** Antes de tocar el código.
2. **No arregles nada que no entiendas.** Si no sabes por qué tu cambio funcionó, todavía no está arreglado.
3. **No cambies cosas al azar** hasta que funcione.
4. Prueba cada opción del menú, y pruébalas también en situaciones raras (inventario vacío, datos incompletos).
5. Un programa que corre no es necesariamente un programa correcto: revisa que los números den.

**Herramientas:** `print()` para mirar valores, el debugger de VS Code (punto de interrupción y paso a paso), y bisección (cortar el programa por la mitad y ver de qué lado está el error).

**Formato de `bugs.md`:**
```
## Bug 1
- Error: (tipo de error y en qué línea)
- Cómo lo detecté:
- Cómo lo arreglé:
```

## Ejercicio 2 · La pregunta bien hecha

Escribe una pregunta técnica real sobre algo que te trabó (puede salir del bug hunt), con esta estructura:
- **Qué quiero lograr:**
- **Qué intenté:** (con el código)
- **Qué esperaba que pasara:**
- **Qué pasó:** (con el error completo)

Envíala por escrito. Esta estructura te va a servir toda tu carrera, y la mitad de las veces vas a encontrar la respuesta mientras la escribes.

## Ejercicio 3 · Arqueología de un sitio web

Abre DevTools (pestaña Network) en un sitio que uses a diario y responde en un documento:
1. ¿Cuántos requests hace al cargar?
2. Encuentra uno que devuelva JSON. Pega un pedazo.
3. ¿Qué verbo y qué código de estado tiene?
4. Encuentra un request que **falle** (rojo). ¿Qué código devuelve y qué significa?
5. ¿Cuánto pesa la página completa?

## Ejercicio 4 · Tu diagrama del request

Dibuja —a mano o en una herramienta— qué pasa desde que escribes una dirección hasta que ves la página. Debe incluir: navegador, DNS, servidor, base de datos y la respuesta de vuelta.

Este dibujo será la diapositiva 2 de tu presentación. Que se entienda solo.

## Ejercicio 5 · Solo con la terminal

Sin usar el mouse ni el explorador de archivos, crea esta estructura, escribe algo en cada archivo y muéstrala con `ls -R`:
```
practica-terminal/
├── documentos/notas.txt
├── codigo/hola.py
└── README.md
```

---

## Entregable de la semana

- [ ] `inventario.py` reparado + `bugs.md` con los 6 errores documentados.
- [ ] Una pregunta técnica bien estructurada.
- [ ] Documento de arqueología web.
- [ ] Diagrama del request, hecho por ti.
- [ ] Estructura `practica-terminal/` creada solo con la terminal.

## Tarea de mitad de semana *(1 hora)*

1. Armar tu presentación (30 min).
2. Terminar el diagrama del request en limpio (15 min).
3. Leer sobre códigos de estado HTTP y anotar qué significan 401 y 403, que **no** son lo mismo (15 min).

## Presentación — martes 13 de octubre

**"El viaje de un request: qué pasa cuando escribo una URL"**
- Diapositiva 2: tu diagrama del Ejercicio 4.
- Diapositiva 3: uno de los bugs del bug hunt — cuál era y cómo lo cazaste.

## Orden de consulta cuando te trabes

documentación oficial → el error textual en el buscador → IA → persona.
**Regla de los 30:** intenta 30 minutos por tu cuenta antes de preguntar; y si llevas toda la tarde sin avanzar, pregunta. Si usas IA, pídele que *explique*, no que resuelva, y dale el error completo, el código y lo que esperabas. **No entra al repositorio ninguna línea que no puedas explicar.**
