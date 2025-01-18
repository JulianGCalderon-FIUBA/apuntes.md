Un algoritmo es **sincrónico** si sus acciones pueden ser delimitadas en el tiempo

- **Sincronismo**: Entrega de un mensaje posee un _timeout_ conocido.
- **Parcialmente sincrónico:** Entrega de un mensaje no posee un _timeout_ conocido o bien el mismo es variable.
- **Asincrónico**: Entrega de un mensaje no posee un _timeout_ asociado.

## Propiedades

Esto se generaliza en dos propiedades: _steadiness_ y _tightness_.

Antes de definirlas, debemos definir dos conceptos auxiliares:

- **Tiempo de delivery** $t_D^P(m)$: Es el tiempo que tarda un mensaje $m$ en ser recibido por $p$, una vez enviado.
- **Timeout de delivery** $T_{D\max}(m)$: Es el tiempo de delivery máximo, para un mensaje $m$.

Luego, podemos definir el **steadiness** $\sigma$ como la máxima diferencia entre el mínimo y el máximo tiempo de delivery de cualquier mensaje recibido por un proceso.

$$
\sigma = \max(T_{D\max} - T_{D\min})
$$

Define la varianza con la cual un proceso observa que recibe los mensajes, y muestra que tan constante es la recepción de mensaje.

Por otro lado, el **tightness** como la máxima diferencia entre los tiempos de delivery para cualquier mensaje.

$$
\forall p,q : \tau = \max_{m,p,q}(t_D^p(m) - t_D^q(m))
$$

Define la simultaneidad con la cual un mensaje es recibido por múltiples procesos.

## Tipos de Protocolos

En un protocolo **Time-Driven**, las fases del protocolo están definidas por un factor de tiempo entre mensajes.

![[Sincronismo 1737235770.png]]

En este ejemplo, vemos que el proceso $P_1$ envía mensaje al resto de procesos. Al haber un timeout conocido (algoritmo sincrónico), si no le llega el $ack$ tras un tiempo $T_{D\max}$, entonces el mensaje se vuelve a enviar. No hay garantía de que a los procesos les llegue el mensaje al mismo tiempo.

En un protocolo **Clock-Driven**, las fases del protocolo están definidas por el reloj de cada proceso. Los mensajes se pueden recibir antes, pero el _delivery_ ocurre en una fracción de tiempo determinada.

![[Sincronismo 1737236049.png]]

En este ejemplo, vemos que el proceso $P_1$ envía un mensaje $m$ al resto de procesos, que incluye el timestamp de $P_1$. El delivery del mensaje solo se hará tras un tiempo $t+\Delta$. De esta forma, nos aseguramos un cierto _steadiness_ y _tightness_. Esto requiere que el [[Relojes|reloj]] de los procesos estén sincronizados.

![[Sincronismo 1737236672.png]]

En este otro ejemplo, vemos como los mensajes se envían en _time slots_ puntuales. Esto nuevamente nos asegura un cierto _steadiness_ y _tightness_, ya que el delivery de los mensajes se retrasa utilizando información del los relojes.
