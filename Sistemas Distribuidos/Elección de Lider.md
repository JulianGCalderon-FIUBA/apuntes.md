El objetivo de la elección de líder es elegir a un proceso en un grupo para que desempeñe. Se deben permitir reelecciones en caso de que el proceso líder decida darse de baja, o se encuentre caído.

Cualquier proceso puede comenzar una nueva elección de líder, solo puede haber más de un líder a la vez, y el resultado de la elección de un nuevo líder debe ser única y repetible.

## Propiedades

Los siguientes algoritmos de elección de líder comparten las siguientes propiedades:

- Cada proceso tiene un identificador único.
- Todos los procesos poseen un arreglo que indica el estado del algoritmo de líder
- Los estados posibles son "definidos" (`elected == P`), o "indefinido" (`elected == @)`.
- El estado inicial de un proceso es indefinido.

Se deben garantizar:

- **Safety**: Un proceso participante posee uno de ambos estados posibles.
- **Liveness**: Todos los procesos participan de la elección de líder y bien terminan con estado "definido", o comienzan una nueva elección de líder.

### Algoritmo de Anillo
