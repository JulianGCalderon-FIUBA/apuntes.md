La replicaci es el proceso por el cual se almacenan múltiples copias de un mismo dato en distintos nodos del sistema. Nos brinda varias ventajas:

- **Es un mecanismo de backup**, permite recuperar el sistema en caso de fallas de disco o catastróficas.
- **Permite repartir la carga** de procesamiento si permitimos que las réplicas respondan consultas o actualizaciones.
- **Garantiza cierta disponibilidad** del sistema aun si se caen algunos nodos.

Cuando las réplicas solo funcionan como mecanismo de *backup* se denominan réplicas secundarias. Cuando también pueden hacer procesamiento, se las conoce como réplicas primarias.

La replicación nos genera un nuevo problema a resolver: la consistencia de los datos. Puede darse la situación de que distintas réplicas almacenen (al menos, temporalmente) distintos valores para un mismo dato.

