En las bases de datos basadas en grafos, los elementos principales son **nodos** y **arcos (ejes)**.

Estas bases de datos resultan útiles para modelar interrelaciones complejas entre las entidades.

Para almacenar la información, cada nodo mantiene una referencia directa a sus nodos adyacentes *(matriz de adyacencias)*. Esto permita operaciones eficientes.

Una de las bases de datos orientadas a grafos más conocida es [[Neo4j]]

## Aplicaciones

Organizar nuestra base de datos de esta forma nos provee ventajas para resolver problemas clásicos de grafos, como:

- Encontrar patrones de nodos conectados entre sí.
- Encontrar caminos entre nodos.
- Encontrar la ruta más corta entre los nodos.
- Calcular medidas de centralidad asociadas a los nodos.

En general, es una buena idea utilizarlas cuando en nuestro modelo conceptual encontramos que las instancias de los tipos de entidad mantiene interrelaciones con otras instancias de su mismo tipo de entidad.
