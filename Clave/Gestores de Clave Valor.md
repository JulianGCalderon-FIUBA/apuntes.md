Almacenan vectores asociativos o diccionarios, es decir, conjuntos formados por pares de elementos de la forma `(clave, valor)`.

Las claves son únicas, y el único requisito sobre su dominio es que sea comparable por igual. Algunos ejemplos son:

- **Berkeley DB**
- **Dynamo**
- **Redis**

Este tipo de bases de datos tiene cuatro operaciones elementales:

- Insertar un nuevo par: `put`
- Eliminar un par existente: `delete`
- Actualizar el valor de un par: `update`
- Encontrar un par asociado a una clave particular: `get`

Sus ventajas son:

- **Simplicidad**
	- No se define un esquema, [[Lenguajes#Data-Definition Language|DDL]], restricciones de integridad, ni dominios.
	- El agregado es mínimo, y está limitado al par.
	- El objetivo es guardar y consultar grandes cantidades de datos, pero no de interrelaciones entre los datos.
- **Velocidad:** Ya que prioriza la eficiencia de acceso, por sobre la integridad de los datos.
- **Escalabilidad:** Generalmente, proveen replicación (ya sea maestro-esclavo o distribuida), y permiten repartir las consultas entre los nodos.

## Dynamo

Dynamo es el *key-value store* de Amazon. Está diseñado siguiendo una arquitectura orientada a servicio, la base de datos está distribuida en un *server cluster* que posee servidores web, routers de agregación, y nodos de procesamiento.

Utiliza un método de lookup denominado [[Hashing Consistente]] que reduce la cantidad de movimientos de pares necesarios cuando cambia la cantidad de nodos $S$.

Utiliza un modelo de consistencia denominado [[Consistencia Eventual]], que tolera pequeñas inconsistencias en los valores almacenados en distintas réplicas.

Es totalmente descentralizado, los nodos son pares entre sí. Esto implica que carece de un punto único de falla.
