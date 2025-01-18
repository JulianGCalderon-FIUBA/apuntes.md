Es un paradigma desarrollado por Google en 2004. La idea es identificar tareas que pueden ser ejecutados en paralelo, y grupos de datos que puedan ser procesados en paralelo.

Algunas implementaciones de este paradigma son: Apache Hadoop, Amazon EMR, Google MapReduce.

Está inspirado en las funciones `map` y `reduce` de los lenguajes funcionales.

## Arquitectura

En el caso ideal, no existe la dependencia entre los datos. Estos pueden ser partidos en *chunks* del mismo tamaño.

Cada proceso pueden trabajar con uno o multiples chunks, de forma uniforme

El coordinador, o proceso **master**, es el encargado de:
- Dividir los datos en chunks
- Enviar la ubicación de los chunks a los workers
- Recibe la ubicación de los resultados de todos los workers

Los workers, son los encargados de:
- Recibir la ubicación de los chunks del proceso master
- Procesar l
