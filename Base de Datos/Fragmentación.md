## Fragmentación

La fragmentación es la tarea de dividir un conjunto de agregados entre un conjunto de nodos. Se realiza con dos objetivos:

- Almacenar conjuntos muy grandes de datos que de lo contrario no podrían caber en un único nodo.
- Paralelizar el procesamiento, permitiendo que cada nodo ejecute una parte de las consultas para luego integrar los resultados.

Según la manera de fragmentar, podemos distinguir entre:

- **Fragmentación horizontal:** Los agregados se reparten entre los nodos, de manera que cada nodo almacena un subconjunto de agregados. Generalmente, se asigna el nodo a partir del valor de alguno de los atributos del agregado.
- **Fragmentación vertical:** Distintos nodos guardan un subconjunto de atributos para cada agregado. Todos suelen compartir los atributos que conforman la clave.

Muchas veces, se utiliza una combinación de ambas.