La redundancia es una forma de tolerar los fallos, y puede ser de varios tipos:

- **Física**: Replicación de componentes.
- **Información**: Se guarda información de más. Los sistemas de *code correction* utilizan este tipo de redundancia.
- **Tiempo**: Se utilizan reintentos ante un error.

## Replicación

Ante situaciones donde hay un único punto de fallo, debemos tratar de replicarlo.

Podemos utilizar algoritmos de consenso para obtener el estado real cuando hay discrepancias. Si la red se particiona, es muy difícil reconciliar el estado.

Hay distintos tipos de replicación:

- **Pasiva**: Hay una réplica primaria que procesa la información, y varias secundarias (o de respaldo) que reciben actualizaciones del líder
	![[Redundancía 1739405165.png]]
- **Activa**: Hay múltiples réplicas de la misma máquina de estado, que ejecutan las mismas operaciones en el mismo orden (total). Por ejemplo: blockchain.
	![[Redundancía 1739405156.png]]
- **Semi-activa** (*leader-follower*): Todas las réplicas ejecutan los comandos, pero una sola (el líder) toma las decisiones no determinísticas.
	![[Redundancía 1739405148.png]]
