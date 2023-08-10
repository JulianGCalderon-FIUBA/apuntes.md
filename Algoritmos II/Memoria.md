## Estructura de un Programa

Un programa puede encontrarse en varias etapas:

- Edición
- Compilación
- Ejecución

En cada una de estas etapas el programa tiene una estructura distinta.

**Edición:** El programa es simplemente un archivo de texto editado en el lenguaje seleccionado.

**Compilación:** De esta etapa se encarga el compilador, su tarea es traducir el código fuente a una estructura que la computadora pueda ejecutar. No es un proceso sencillo.

**Ejecución:** Una vez compilado el programa, el programa toma un formato objeto, el cual se puede ejecutar en una computadora.

En esta etapa, el programa se divide en distintas secciones:

- **Código** (.code): En esta sección se almacena el código del programa, ya traducido por el compilador
- **Datos** (.data): En esta sección se almacena los datos de valores globales y literales
- **Pila de Ejecución** (.stack): Se almacenan las variables locales una vez se ejecuta el programa
- **Montículo** (.heap): Es la memoria dinámica, no existe hasta que el programa se ejecuta.

## Memoria

La memoria de la computadora puede ser vista como un arreglo de celdas, en las que cada celda tiene una dirección, cada celda tiene una dirección consecutiva a la anterior. Empezando del 0 hasta la cantidad de memoria que posea.

Cada celda de la memoria posee un byte, es tarea del programa leer la cantidad de bytes necesarios para entender la información.

## Memoria Dinámica

La memoria dinámica es aquella reservada durante la ejecución del programa, y se almacena en el **heap**.

Para manejar la memoria dinámica, usamos algunas funciones de la biblioteca estándar:

- **`malloc():`** Se encarga de reservar memoria y devuelve un puntero a la memoria reservada. La memoria no está inicializada, por lo que a veces es útil usar la alternativa `calloc()`, la cual reserva memoria y la inicializa con el valor `NULL`**.**
- **`free():`** Se encarga de liberar la memoria previamente reservada con el malloc.
- **`realloc():`** Se encarga de modificar el tamaño del bloque de memoria previamente reservado, La memoria antes almacenada permanecerá sin cambios hasta el último elemento de la memoria anterior, o el máximo del bloque.

El manejo de la memoria es responsabilidad del programador, toda memoria reservada debe liberarse. No liberar la memoria implica **SERIOS PROBLEMAS** en el **COMPORTAMIENTO del programa.**

> "¡La memoria dinámica no se conserva! ¡Siempre que se crea debe destruirse!
> **Dr. *Mariano Méndez***
