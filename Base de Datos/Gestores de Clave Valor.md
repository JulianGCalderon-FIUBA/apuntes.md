Las bases de datos de clave-valor almacenan vectores asociativos o diccionarios, es decir, conjuntos formados por pares de elementos de la forma `(clave, valor)`

> [!example] Ejemplo
> ("nombre", "Luis Poretti"), ("saldo", 5100)

Las claves son únicas (no puede haber dos pares que posean la misma clave), y el único requisito sobre su dominio es que sea comparable por igual ($=$). Algunos ejemplos son:

- Berkeley DB (Oracle)
- [[Dynamo]] (Amazon)
- Redis

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
