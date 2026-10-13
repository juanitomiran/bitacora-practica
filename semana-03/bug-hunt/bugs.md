Bitácora de Errores (Bugs.md)
1. SyntaxError
Qué error era: SyntaxError: unexpected EOF while parsing al intentar ejecutar el último print().

Cómo me di cuenta: Python ni siquiera ejecutó el programa; la terminal lanzó un error rojo antes de correr.

Cómo lo arreglé: Agregué el paréntesis de cierre que faltaba al final de la línea.

2. NameError
Qué error era: NameError: name 'total_items' is not defined durante la función de estadísticas.

Cómo me di cuenta: El programa se cayó a la mitad al intentar hacer una división.

Cómo lo arreglé: Corregí el nombre de la variable y usé la función len() correctamente.

3. TypeError
Qué error era: TypeError: '>' not supported between instances of 'int' and 'str'.

Cómo me di cuenta: El programa falló al evaluar la condición del stock comparando un número con un texto entre comillas.

Cómo lo arreglé: Cambié el string por su valor numérico entero. "int(intput(...))

4. Error lógico (Desfase en el contador)
Qué error era: La lista en pantalla comenzaba a numerarse desde un número incorrecto, desfasando los elementos.

Cómo me di cuenta: El programa corrió sin lanzar errores en la terminal, pero al revisar la salida visual noté el desfase en la numeración.

Cómo lo arreglé: Ajusté la inicialización de la variable del contador.

5. KeyError
Qué error era: KeyError al procesar un diccionario que no tenía una clave específica.

Cómo me di cuenta: El código funcionó bien para los primeros elementos, pero se detuvo de golpe con uno en particular.

Cómo lo arreglé: Utilicé el método .get() para manejar claves faltantes de forma segura.

6. IndexError con lista vacía
Qué error era: IndexError: list index out of range al intentar leer índices de una lista sin elementos.

Cómo me di cuenta: Al hacer pruebas pasando una lista vacía [] como argumento.

Cómo lo arreglé: Agregué una validación previa (if not lista: return) para verificar que la lista tenga elementos antes de procesarla.