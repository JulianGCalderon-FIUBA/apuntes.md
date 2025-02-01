El consenso es un procedimiento para un conjunto de procesos distribuidos acuerden en el mismo valor dado un punto de decisión. Implica coordinación y establecer un algoritmo de acuerdo.

Al ser un problema complejo, se suelen tomar suposiciones, por ejemplo:

- Los canales de comunicación son *reliables*.
- Todos los procesos pueden comunicarse entre sí: no hay particionamiento de redes.
- La única falla a considerar es la caída de un proceso.
- La caída de un proceso no puede ocasionar la caída de otro. Esto no ocurre si los sistemas se encuentran en la misma computadora.

Algunas propiedades necesarias de los algoritmos de consenso, son:

- Agreement
- Integrity
- Termination

## Algoritmo de Consenso Simple

Dados $n$ procesos, se quiere llegar a un acuerdo sobre un valor particular. Cada proceso almacena, en cada instante de tiempo, el valor computado por todos los procesos.

En cada ronda, los procesos envían los valores computados en esa ronda a todo el resto de procesos. Cada proceso recibe los datos del resto de procesos y los almacena.

Tras $f$ rondas, se aplica una función de agregación sobre el estado, y como la información total es la misma (ya que todos los procesos compartían los datos computados en cada ronda), entonces la decisión será determinística.

La función de agregación puede ser, por ejemplo, una votación.
