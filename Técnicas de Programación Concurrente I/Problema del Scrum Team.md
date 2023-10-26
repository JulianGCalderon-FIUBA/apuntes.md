Un grupo de desarrolladores de *software* trabaja en un equipo de pares.

Dentro del equipo, uno de ellos ejerce el rol de **Scrum Master**. Los desarrolladores solicitan a este la tarea a realizar, y le informan a este cuando terminan.

Cada cierto tiempo, el **Scrum Master** se cansa de atender a su equipo, y decide tomar unas vacaciones sin previo aviso. Al ser un equipo de pares, cualquier otro desarrollador asume sus funciones.

## Solución con Algoritmo de [[Elección de Lider]]

Para resolver el problema, necesitaremos utilizar alguno de los algoritmos de elección de *lider*. El código a alto nivel será idéntico, independiente del algoritmo utilizado.

```Go
for online() {
	if is_leader() {
		if tired() {}
		peer := recv("request")
		send(peer, "task")
	} else {
		leader := get_leader()
		send(leader, "request")
		
		err != recv("task") // with timeout
		if err == "timeout" {
			find_new_leader()
		}
	}
}
```
