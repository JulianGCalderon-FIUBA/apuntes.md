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

Define la simultaneidad con la cual un mensaje es recibido por múltiples procesos.

## Tipos de Protocolos

- **Time-Driven**: Las fases del protocolo están definidas por un factor de tiempo entre mensajes.
- **Clock-Driven**: Las fases del protocolo están definidas por el reloj de cada proceso. Los mensajes se pueden recibir antes, pero el delivery ocurre en una fracción de tiempo determinada.
