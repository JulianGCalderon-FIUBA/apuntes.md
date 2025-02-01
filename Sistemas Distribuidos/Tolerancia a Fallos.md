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
- Espera hasta que todos los procesos le den permiso de ingresar a la sección (`OK`)
- Entra la sección crítica.

Cuando un proceso recibe una consulta, entonces:

- Si no está interesado en entrar a la sección crítica, devuelve `OK`.
- Si posee la sección crítica, no responde y encola el mensaje. Una vez sale, devuelve `OK` a todos los mensajes encolados.
- Si envió previamente un mensaje para acceder a la sección crítica, entonces compara el timestamp del mensaje enviado y el mensaje recibido. Aquel que tenga un menor timestamp gana:
	- Si el receptor es el perdedor, entonces envía un `OK`.
	- Si el receptor es el ganador, entonces encola la consulta.

Este algoritmo tiene la ventaja de que no requiere de un coordinador, pero tiene otras desventajas:

- Se requiere de una malla de conexiones. Todos los procesos deben conocerse.
- La cantidad de mensajes enviados es muy alta.
- Es imposible detectar entre un proceso caído o un proceso en una sección crítica.
