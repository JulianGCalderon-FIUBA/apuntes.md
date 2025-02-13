l consenso es un procedimiento para un conjunto de procesos distribuidos acuerden en el mismo valor dado un punto de decisión. Implica coordinación y establecer un algoritmo de acuerdo.

Al ser un problema complejo, se suelen tomar suposiciones, por ejemplo:

- Los canales de comunicación son *reliables*.
- Todos los procesos pueden comunicarse entre sí: no hay particionamiento de redes.
- La única falla a considerar es la caída de un proceso.
- La caída de un proceso no puede ocasionar la caída de otro. Esto no ocurre si los sistemas se encuentran en la misma computadora.

## Objetivos

Algunos de los objetivos a lograr son:

- Lograr que un conjunto de procesos pueda realizar ciertas tareas siguiendo una secuencia.
- Permitir la replicación de información.
- Evitar los puntos únicos de fallo.

Algunos de los problemas que se pueden resolver, son:

 - Sincronización entre diferentes procesos: un proceso debe esperar a otro para continuar, o se requiere acceso exclusivo a un recurso compartido.
 - Elección de un proceso coordinación líder.
 - Determinación del valor correcto de una propiedad.

## Definición General

Se tienen un conjunto de $N$ procesos $P_i$ que desean llegar a un acuerdo:

- Cada proceso comienza en el estado `undecided`.
- Cada proceso $p_i$ posee una variable de decisión $d_i$.
- Cada proceso propone un valor $v_i$.

Luego de haber recibido mensaje de otros procesos, el proceso $p_i$ establece su variable de decisión $d_i$ y cambia su estado a `decided`.

Se denota como $f$ como la cantidad de nodos que pueden fallar bizantina, y $N$ con la cantidad de nodos del sistema. Luego la fórmula de quorum, indica la cantidad de nodos necesarios para que el sistema pueda llegar a un consenso. Por ejemplo, si se requiere mayoría: $N >= 2f + 1$.

## Requerimientos

Algunos requerimientos necesarios de los algoritmos de consenso, son:

- **Agreement**: El valor de la variable de decisión $d_i$ es el mismo en todos los procesos correctos.
- **Integrity**: Si los procesos correctos propusieron el mismo valor $v$, entonces el valor de su variable de decisión es la misma. Esto implica que no solo se llega a un acuerdo, sino que el acuerdo es correcto.
- **Termination**: Eventualmente, todos los procesos activos establecen su variable de decisión.

![[Algoritmos de Consenso 1738452241.png]]

En el gráfico podemos ver como `P1` y `P2` propusieron el mismo valor `proceed`, y como son mayoría se conveirte en el valor de la variable de decisión del proceso `P3`

## Algoritmo Sincrónico

Cada proceso $p_i$ tiene la variable `state(x,y)` que almacena la información de cada proceso `x` en el instante de tiempo `y`.

Al iniciar el proceso:

```
set state(i, 0) = {}
set state(i, 1) = { v }
```

En cada ronda, los procesos envían los valores computados en esa ronda a todo el resto de procesos. Cada proceso recibe los datos del resto de procesos y los almacena.

```
For each round r, with 1 < r <= f+1:
	broadcast state(i, r) - state(i, r-1)
	set state(i, r+1) = state(i, r)
	For each process j:
		receive state from j into state(j, r)
		set state(i, r+1) += state(j, r)
```

Tras `f+1` rondas, se aplica una función de agregación sobre el estado, y como la información total es la misma (ya que todos los procesos compartían los datos computados en cada ronda), entonces la decisión será determinística.

```
decide d = aggregate over state(i, f+1)
```

La función de agregación puede ser, por ejemplo, una votación.

> [!note] Elección de Líder
> El algoritmo es genérico y puede ser utilizado para implementar una elección de líder si, por ejemplo, `v_i` representa el identificador del proceso `i`, y la función de agregación es `max`.
