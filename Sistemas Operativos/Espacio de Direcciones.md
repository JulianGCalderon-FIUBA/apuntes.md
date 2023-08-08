Para generar la ilusión de que un programa tiene toda la memoria de la computadora, el sistema operativo debe virtualizar, generando un espacio de direcciones virtual perteneciente al usuario.

El espacio de direcciones de un proceso contiene toda la memoria del mismo: tanto el ***code***, como el ***stack y*** el ***heap***.

El ***heap*** y el ***stack*** son dos regiones que crecen en sentidos inversos, aunque el stack está predefinido y limitado.

Con la existencia de ***threads***, el espacio de memorias se complica.

Lo que se está describiendo es la abstracciones del mapa de memoria que provee el sistema operativo a un programa corriendo.

![[Espacio de Direcciones 1.png|Untitled]]

Cuando el usuario accede a cierta dirección de memoria virtual $\text A$, el sistema operativo ***mapea*** el valor a otra dirección de memoria $\text B$, una dirección de memoria real. Si el usuario accede a una dirección de memoria virtual que no le pertenece, entonces se lanza una excepción.

# Objetivos

Uno de los objetivos principales de la ***transparencia***, se busca que la memoria virtual sea invisible al usuario, de forma que el proceso se comporte como si fuese su propia memoria física.

Otro objetivo importante es el de la ***eficiencia***, tanto en términos de tiempo como espacio. Para que esto sea posible, el sistema operativo confía en el soporte del hardware para lograrlo, como las TLBs.

Por último, es importante la **protección.** El sistema operativo debe asegurarse que a pesar de tener un mapa de direcciones completo, el usuario solo pueda acceder a aquella memoria que le pertenece, que el sistema operativo le dio permiso de acceder.