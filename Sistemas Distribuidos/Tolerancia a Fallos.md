La tolerancia a fallos estudia las necesidades de los sistemas confiables (*dependable systems*):

- Busca garantizar que se ejecuten y comporten de acuerdo a lo esperado por el usuario en distintas condiciones.
- Busca prevenir la aparición de fallas de cara al usuario, tanto normales como excepcionales.
- Hay distintas alternativas para prevenir o tolerar cada situación.

La idea es que el sistema nunca salga de estados definidos. Todo escenario debe estar contemplado, y debe haber una forma para volver al flujo habitual.

Se permite definir la inversión y el nivel de tolerancia para cada tipo de sistema.

Algunas herramientas para lograr esto son:

- Recuperación.
- Redundancia (ej. replicación).
- Consenso (ej. esquema de votación)

> En presencia de fallos, el sistema distribuidos continúa operando de forma aceptable

## Generación de Fallos

Un **fallo** o *fault* causa la ocurrencia de un estado de **error** en el sistema. Esto eventualmente desencadena en un comportamiento incorrecto: falla o **avería** (*failure*). Se busca que todos los fallos (o errores) se encapsulen y que nunca se llegue a una avería.

Un fallo parcial ocurre cuando un componente de un sistema distribuido incurre en error. Es una característica distintiva de los sistemas distribuidos, y puede generar una reacción encadena que afecta al comportamiento del sistema completo.

Por ejemplo:

- Un rayo cósmico cambia el estado de un bit en memoria: esto es un **fallo**.
- Esto causa que un puntero apunte a una dirección inválida: hay un **error** en el estado del sistema.
- Eventualmente, el programa accede a esta dirección de memoria inválida y morirá: esto es una falla o una **avería**.

Otro ejemplo:

- Un programa `Y` no puede comunicarse con el programa `X` debido a un fallo en la comunicación.
- El programa `Y` hace un *polling* infinito con un timeout pequeño a programa `X`, dejando conexiones abiertas.
- El programa `Y` llega al límite de conexiones abiertas, y muere.

## Clasificación de Fallos

Los fallos se clasifican en:

- **Transientes**: ocurren una vez y luego desaparecen; si se repite la operación, el fallo desaparece. Es un ello esporádico.
- **Intermitentes**: Ocurren de forma intermitente; son difíciles de diagnosticar.
- **Permanentes**: Existen hasta que los componentes defectuosos se reemplaza: se rompe el disco.

Es importante entender la diferencia entre fallos **improbables**, y fallos **imposibles**: ¿Es imposible que una lluvia solar altere el estado de un sistema?

Otra forma de clasificar los fallos es:

- **Crash**: se detiene el servicio por completo.
- **Timing**: Se da una respuesta fuera de los tiempos aceptables.
- **Omisión**: El servicio falla al responder solicitudes entrantes.
- **Respuesta**: La respuesta es incorrecta.
- **Bizantina**: Es arbitraria en tiempos y respuesta; la información es diferente para distintos consumidores. A veces lo hace por motivos maliciosos.

## Condiciones de Trabajo

Para definir el nivel de tolerancia a fallos de un sistema, es necesario indicar en que condiciones opera el sistema.

Las condiciones se pueden separar en dos tipos:

- **Condiciones del entorno**:
	- Entorno físico del hardware, como temperatura, polvo, etc.
	- Interferencia y ruido.
	- *Drift* del reloj.
- **Condiciones operacionales**:
	- Especificaciones, valores límite y tiempos de respuesta.
	- Ancho de banda, latencia
	- Protocolos soportado

## Estrategias de Manejo de Fallos

Hay distintas estrategias para manejar los fallos:

- **Fault removal**: Eliminar los errores antes de que sucedan. Por ejemplo: estrategias de *code correction* para evitar cambios de bits.
- **Fault prevention:** Evitar las condiciones que llevan a los errores. Por ejemplo: con componentes que impidan que haya fallos (relojes atómicos, componentes de grado militar).
- **Fault forecasting:** Determinar la probabilidad de que un componente pueda fallar, y reemplazarlo. Por ejemplo: reemplazar componentes cada cierta cantidad de horas de uso.
- **Fault tolerance:** Procesas los errores del sistema, en lugar de evitar que sucedan. Es la estrategia más común en software.

## Recuperación

La recuperación consiste en tras un error, llevar el sistema a un estado correcto. Una forma de lograrlo es:

- **Almacenamiento estable**: En primer lugar, necesitamos un almacenamiento seguro.
- **Checkpoints**: Se guarda periódicamente el estado completo del sistema en almacenamiento estable. De esta forma, podemos volver a un escenario previo al fallo.
- **Message logging**: Se parte de un checkpoint válido y se repiten todos los mensajes intercambiados desde ese checkpoint.
- **Consenso**: En caso de ser necesario, se acuerda entre los componentes vivos el estado correcto.

Estos mecanismos son costosos, pero es mejor que no tener ninguna forma de restaurar el sistema.

## Redundancia

Consiste en tolerar los errores mediante a redundancia. Esta puede ser de varios tipos:

- **Física**: Replicación de componentes.
- **Información**: Se guarda información de más. Los sistemas de *code correction* utilizan este tipo de redundancia.
- **Tiempo**: Se utilizan reintentos ante un error.

## Replicación

Ante situaciones donde hay un único punto de fallo, debemos tratar de replicarlo.

Podemos utilizar algoritmos de consenso para obtener el estado real cuando hay discrepancias. Si la red se particiona, es muy difícil reconciliar el estado.

Hay distintos tipos de replicación:

- **Pasiva**: Hay una réplica primaria que procesa la información, y varias secundarias (o de respaldo) que reciben actualizaciones del líder
- **Activa**: Hay múltiples réplicas de la misma máquina de estado, que ejecutan las mismas operaciones en el mismo orden. Por ejemplo: blockchain.
- **Semi-activa** (*leader-follower*): Todas las réplicas ejecutan los comandos, pero una sola (el líder) toma las decisiones no determinísticas. Hay un balanceador de carga que envía las consultas a las réplicas.

## Resiliencia

La confianza (*dependability*) es la medida de la confianza en el sistema: Tiene distintos factores:

- **Disponibilidad**
- **Fiabilidad**
- **Mantenibilidad**
- **Seguridad**
- **Durabilidad**

La resiliencia consiste en la capacidad de mantener un nivel aceptable de servicio en presencia de fallos.

Se dice que un sistema tiene degradación suave (*graceful degradation*) cuando el comportamiento se degrada, pero continúa siendo aceptable.

## Disponibilidad y Fiabilidad

Son dos conceptos que estan relacionados:

- **Disponibilidad** (*availability*): La probabilidad de que el sistema esté operando.
- **Fiabilidad** (*reliability*): La capacidad del sistema para dar un servicio correcto de forma continúa. No solo tiene que estar disponible, sino que tiene que hacerlo de forma correcta.

La mejor estrategia depende de varios factores:

- Costos y presupuesto disponible.
- Necesidades de performance y escalabilidad.
- Necesidades heterogéneas de cada componente.

Para tomar las decisiones adecuadas, debemos pensar en el origen de los errores: no todos los errores son de hardware (20% aproximadamente). Hay muchos errores relacionados a errores de software, y errores de humanos (de configuración).

## Mantenibilidad

La **mantenibilidad** (*maintainability*) es la cantidad de tiempo que se requiere para recuperar el sistema (ej. repararlo o actualizarlo.

Para garantizarla, se crea una imagen para cada cambio a desplegar. No se manejan con estados mutables. Esto permite automatizar los despliegues, sin que haya humanos realizándolo de forma directa. Esto reduce la probabilidad de errores humanos.

![[Tolerancia a Fallos 1738378604.png]]

Esta inmutabilidad nos permite realizar trazabilidad de las imágenes, para ver de donde vinieron.

Las actualizaciones son inmediatas, ya que únicamente implican ejecutar la imagen y configurar el balanceador de carga para que mueva las consultas al nuevo contenedor.

Los contenedores pueden ser replicados y relanzados ante errores, lo que aumenta la disponibilidad del sistema.

Al usar imágenes, puedo desacoplar el sistema de la infraestructura (IaaS) y de la plataforma (PaaS). Al especificar únicamente la imagen, no es necesario configurar la infraestructura completa.

Se puede realizar testing de imágenes antes del despliegue, ya que la configuración en el ambiente de testing es igual al ejecutado en producción.

Las imágenes viejas pueden ser almacenadas para un posible rollback.

## Durabilidad

La **durabilidad** (*durability*) es la probabilidad de que un dato persistido se pueda recuperar.

## Seguridad

La **seguridad** (*safety*) implica que en presencia de fallos, no ocurre nada catastrófico.

> El sistema debe poder ser recuperado automática o manualmente ante cualquier tipo de falla

Es necesario definir un **Disaster Recovery Process** para la infraestructura y los datos. Son situaciones improbables pero no imposibles, y debemos poder resolverlas.

El tiempo de restauración debe ser conocido para poder garantizar los SLA.

Los escenarios catastróficos deben ser testeados. En algunas situaciones se fuerza la caída de algunos componentes para ver como se comporta el sistema, o para ver si el protocolo funciona correctamente.

## Consenso

El consenso es un procedimiento para un conjunto de procesos distribuidos acuerden en el mismo valor dado un punto de decisión. Implica coordinación y establecer un algoritmo de acuerdo.

Al ser un problema complejo, se suelen tomar suposiciones, por ejemplo:

- Los canales de comunicación son *reliables*.
- Todos los procesos pueden comunicarse entre sí.
- La única falla a considerar es la caída de un proceso.
- La caída de un proceso no puede ocasionar la caída de otro.

### Coordinación y Acuerdo

Algunos de los objetivos a lograr son:

- Lograr que un conjunto de procesos pueda realizar ciertas tareas siguiendo una secuencia.
- Permitir la replicación de información.
- Evitar los puntos únicos de fallo.

Se busca resolver los siguientes problemas:

 - Sincronización entre diferentes procesos: un proceso debe esperar a otro para continuar, o se requiere acceso exclusivo a un recurso compartido.
 - Elección de un proceso coordinación líder.
 - Determinación del valor correcto de una propiedad.

### Algoritmo de Consenso Simple

### Exclusión Mutua Distribuida

El objetivo es crear un algoritmo que permita pedir y obtener acceso exclusivo a un recurso que se encuentra disponible en la red. Para lograr el objetivo, se utilizará **pasaje de mensajes**.

Recordemos que las propiedades que se buscan cumplir:

- **Safety**: Solo un proceso puede obtener el recurso en todo momento.
- **Liveness**: Si un proceso está listo para recibir un recurso, debe obtenerlo eventualmente.
- **Fairness**: El uso del recurso se distribuye de forma uniforme entre los procesos.

#### Servidor Central

Se designa alguno de por procesos del sistema como coordinación de la sección crítica.

Los procesos piden acceso a la sección crítica al servidor central, el cual se los otorga de a uno a la vez. Si un recurso se encuentra tomado, las consultas se encolan en modo FIFO.

Algunas ventajas de este esquema son:

- Las consultas son procesadas en orden.
- Es fácil de entender y de implementar.
- Los procesos solo necesitan conocer al servidor.
- La cantidad de conexiones y mensajes es mínima.

Por otro lado, tiene las siguientes desventajas:

- El servidor central es un único punto de falla.
- Los procesos no pueden distinguir entre sí el servidor está caído o no responsivo.
- Se produce un cuello de botella.

#### Token Ring

Se construye un anillo ordenando a todos los procesos por algún atributo. Luego se crea un token que circula alrededor del anillo.

Cuando un proceso recibe el token, accede a la sección crítica en caso de que sea necesario, y luego le pasa el *token* a su vecino. Puede haber múltiples *tokens*, uno por sección crítica.

Se debe implementar algún mecanismo de recuperación de token, en caso de que se caiga el nodo que lo tenía.

#### Ricart & Agrawala

Es un algoritmo distribuido que utiliza *reliable multicast* y relojes lógicos.

Cuando un proceso intenta acceder a una sección crítica, entonces:

- Crea un mensaje con un timestamp asociado al proceso, un identificador, y el nombre del recurso a acceder.
- Envía el mensaje a todos los procesos del grupo.
- Espera hasta que todos los procesos le den permiso de ingresar a la sección.
