Un estado se comparte entre varios procesos. Algunos procesos necesitan actualizar dicho estado, mientras que otros solo necesitan leerlo.

Mientras que un proceso está leyendo, otros también pueden leerlo. Mientras que un proceso está modificando, ningún otro puede leerlo ni modificarlo.

## Solución con [[Variables de Condición]]

Tenemos una variable de condición asociada a un *lock*. Este lock mantendrá un contador, indicando la cantidad de escritores, y una bandera, indicando si hay un escritor.

En cuanto un proceso quiere escribir, realiza un `wait_while` de la variable de condición, esperando a que no haya ningún escritor. Si la condición se cumple, aumenta en uno la cantidad de lectores y libera el *lock*.

Una vez finaliza de escribir, accede al *lock* nuevamente 
