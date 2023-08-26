## Contadores Concurrentes

Una de las estructuras de datos más simples es un contador, podemos realizar un contador concurrente de forma simple utilizando lo visto en los capítulos anteriores.

Si bien esta solución es simple, no es escalable. El patrón más común para las estructuras de datos concurrentes es el de tener una serie de rutinas, dentro de ellas se puede encontrar la lógica de locks.

Para hallar un contador escalable, una técnica es utilizar el *approximate counter*. Para hacerlo, se utiliza un único *logical counter* a través de múltiples *local counters,* uno por CPU, y un *global counter.*

Cuando un hilo quiere incrementar un contador, incrementa su contador local. Para que el contador global se mantenga actualizado, los valores locales periódicamente se transfieren al contador global.

El tiempo entre actualizaciones se conoce como el **threshold S**, cuanto menor es este valor, más se aproxima a un contador común.

## Listas Enlazadas Concurrentes

El enfoque simple para solucionar esto sería utilizar un lock para todas las secciones críticas. Nuevamente, esto puede tener bajo rendimiento cuando tenemos muchos threads.

Una técnica frecuentemente utilizada para obtener listas enlazadas escalables es la técnica *hand-over-hand locking,* también conocida como *lock coupling*.

En lugar de tener un único lock para toda la lista, tenemos un lock para cada nodo de la lista. Cuando iteramos una lista, primero agarramos el próximo nodo, luego liberamos el actual.

Conceptualmente, esta técnica tiene sentido, aunque es la práctica, es difícil que tenga mejor rendimiento que una lista enlazada simple. Esto es debido a la cantidad de *locks* y *unlocks* que se necesitan.

## Colas Concurrentes

Un enfoque más complejo que el tradicional para las colas concurrentes consiste en tener dos locks, uno para el nodo inicial, y otro para el nodo final. Algunas implementaciones utilizan un *dummy node* para separar el nodo inicial del final.

## Tablas de Hash Concurrentes

Para construir esta tabla, utilizamos las listas enlazadas mencionadas anteriormente. En lugar de un lock para la estructura completa, tendremos un lock para cada *hash bucket.*
