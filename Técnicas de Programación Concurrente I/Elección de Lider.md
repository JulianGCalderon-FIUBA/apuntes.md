Varios algoritmos distribuidos requieren de un coordinador con un rol especial. En general, no es importante cuál es el proceso, sino que debe cubrirse el rol.

Se asume que todos los procesos tienen un identificador único, se ejecuta un proceso por máquina y conocen el número de los demás procesos.

Al finalizar la elección, se debe concluir en un único lider, conocido por todos.

## Algoritmo Bully

Cuando un proceso $P$ nota que el coordinador no responde (no hay ninguno, u ocurrió un problema con el líder), inicia el proceso de elección:

1. $P$ envía el mensaje `ELECTION` a todos los proceso que tengan número mayor.
2. Si nadie responde, $P$ gana la elección y es el nuevo coordinador.
3. Si contesta algún proceso con número mayor, este continúa con el proceso y $P$ finaliza.
4. El nuevo coordinador se anuncia con un mensaje `COORDINATOR`.

En este algoritmo, siempre gana el proceso con mayor número.
