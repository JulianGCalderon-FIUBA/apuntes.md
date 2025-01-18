Es un paradigma desarrollado por Google en 2004. La idea es identificar tareas que pueden ser ejecutados en paralelo, y grupos de datos que puedan ser procesados en paralelo.

Algunas implementaciones de este paradigma son: Apache Hadoop, Amazon EMR, Google MapReduce.

Está inspirado en las funciones `map` y `reduce` de los lenguajes funcionales.

## Arquitectura

En el caso ideal, no existe la dependencia entre los datos. Estos pueden ser partidos en *chunks* del mismo tamaño.

Cada proceso pueden trabajar con uno o múltiples chunks, de forma uniforme

El coordinador, o proceso **master**, es el encargado de:

- Dividir los datos en chunks.
- Enviar la ubicación de los chunks a los workers.
- Recibe la ubicación de los resultados de todos los workers.

Los workers, son los encargados de:

- Recibir la ubicación de los chunks del proceso master.
- Procesar los chunks de información.
- Envia la ubicación del resultado del procesamiento al master.

La ca

## Logica de Negocio

La logica de negocio, provista por el usuario, son las funciones `map` y `reduce`.

La función `map` recibe un chunk y devuelve un resultado intermedio como un conjunto de pares clave-valor.

La función `reduce` recibe un conjunto de pares clave-valor. Esta función es llamada por cada clave única. 
