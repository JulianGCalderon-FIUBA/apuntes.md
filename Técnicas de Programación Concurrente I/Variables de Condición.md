Un variable de condición es un mecanismo de sincronización que no guarda ningún valor, sino que tiene asociado una cola.

Una variable de condición `C` consta de tres operaciones atómicas:

- La operación de `waitC(C)` siempre bloquea el proceso hasta que sea desbloqueado con `signalC(C)`. El proceso es agregado a una cola.
- La operación `signalC(C)` desbloquea el último proceso de la cola. Si está vacía, no tiene ningún efecto.
- La operación `empty(C)` nos permite verificar si cola de procesos está vacía.

Las variables de condición suelen ser utilizadas junto a los [[Monitores]].

Es recomendable verificar el estado de la condición luego de ser despertado, ya que a veces el sistema operativo realiza un *spurious wakeup*. Esto quiere decir que a veces el sistema operativo despierta a nuestro hilo esperando en la variable de condición sin ser señalizado.
