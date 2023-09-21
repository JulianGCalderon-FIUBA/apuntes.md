Un estado se comparte entre varios procesos. Algunos procesos necesitan actualizar dicho estado, mientras que otros solo necesitan leerlo.

Mientras que un proceso está leyendo, otros también pueden leerlo. Mientras que un proceso está modificando, ningún otro puede leerlo ni modificarlo.

## Solución con [[Variables de Condición]]

Tenemos una variable de condición asociada a un *lock*. Este lock sincronizará un contador, indicando la cantidad de escritores, y una bandera, indicando si hay un escritor.

En cuanto un proceso quiere leer, realiza un `wait_while` de la variable de condición, esperando a que no haya ningún escritor. Si la condición se cumple, aumenta en uno la cantidad de lectores y libera el *lock*.

Una vez finaliza de leer, accede al *lock* nuevamente, decrementa en uno la cantidad de lectores y realiza un `notify_all` para indicarle a los hilos esperando que cambio el estado interno. Luego libera el *lock*.

En cuanto un proceso quiere escribir, realiza un `wait_while` de la variable de condición, esperando a que no haya ningún lector (ni escritor). Si la condición se cumple, establece la bandera indicando que hay un escritor y libera el lock.

Una vez finaliza de escribir, accede al *lock* nuevamente, establece la bandera indicando que no hay ningún escritor y realiza un `notify_all` para indicarle a los hilos esperando que cambio el estado interno. Luego libera el *lock*.

Si bien esta solución funciona, no es justa. Le da prioridad a los lectores.

### Prioridad al Escritor

Para darle prioridad al escritor, podemos agregar un contador de cantidad de escritores en espera. Mientras haya escritores en espera, los lectores en espera no podrán acceder al recurso.

Esta solución es la más práctica y la que más se usa.

### Escenario Justo

Para crear una solución justa debemos utilizar una cola. Una solución siempre involucraría agregar un contador de *cola*, indicando la última posición de la cola, y un contador de *siguiente*, indicando el número del próximo a atender.

Al entrar por primera vez a la cola obtendrán un número propio de cola basándose en el contador de cola, y aumentarán el contador.

Luego, continuaran verificando que su número propio sea igual al contador de siguiente. Si es el caso, acceden al recurso. Luego, incrementan el contador de cola.

Estas verificaciones deben estar acompañadas de las verificaciones del escenario simple, para asegurar el acceso concurrente entre lectores.
