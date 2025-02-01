Un grupo de desarrolladores de *software* trabaja en un equipo de pares.

Dentro del equipo, uno de ellos ejerce el rol de **Scrum Master**. Los desarrolladores solicitan a este la tarea a realizar, y le informan a este cuando terminan.

Cada cierto tiempo, el **Scrum Master** se cansa de atender a su equipo, y decide tomar unas vacaciones sin previo aviso. Al ser un equipo de pares, cualquier otro desarrollador asume sus funciones.

## Solución con Algoritmo de [[Técnicas de Programación Concurrente I/Elección de Lider]]

Para resolver el problema, necesitaremos utilizar alguno de los algoritmos de elección de líder. El código a alto nivel será idéntico, independiente del algoritmo utilizado.

```Go
for online(...) {
	if is_leader(...) {
		peer := recv_request() // blocking
		send_task(peer)
		
		if tired(...) {
			disconnect(...)
		}
	} else {
		leader := get_leader(...) // blocks if election going
		send_request(leader)
		
		task, timeout := recv_task(leader) // with timeout
		if timeout {
			find_new_leader(...) // blocks until election
		} else {
			complete(task)
		}
	}
}
```

Ademas de implementar las funciones indicadas en el codigo de arriba, es necesario tener un hilo que constantemente escuche mensajes nuevos, para poder implementar el algoritmo.
