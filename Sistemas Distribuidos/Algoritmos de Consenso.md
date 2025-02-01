El consenso es un procedimiento para un conjunto de procesos distribuidos acuerden en el mismo valor dado un punto de decisión. Implica coordinación y establecer un algoritmo de acuerdo.

Al ser un problema complejo, se suelen tomar suposiciones, por ejemplo:

- Los canales de comunicación son *reliables*.
- Todos los procesos pueden comunicarse entre sí: no hay particionamiento de redes.
- La única falla a considerar es la caída de un proceso.
- La caída de un proceso no puede ocasionar la caída de otro. Esto no ocurre si los sistemas se encuentran en la misma computadora.

## Coordinación y Acuerdo

Algunos de los objetivos a lograr son:

- Lograr que un conjunto de procesos pueda realizar ciertas tareas siguiendo una secuencia.
- Permitir la replicación de información.
- Evitar los puntos únicos de fallo.

Se busca resolver los siguientes problemas:

 - Sincronización entre diferentes procesos: un proceso debe esperar a otro para continuar, o se requiere acceso exclusivo a un recurso compartido.
 - Elección de un proceso coordinación líder.
 - Determinación del valor correcto de una propiedad.

## Algoritmo de Consenso Simple
