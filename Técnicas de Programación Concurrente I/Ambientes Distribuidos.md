En estos ambientes, una falla en una entidad que no conocemos puede ocasionar un error en nuestro sistema.

## Entidades

Una **entidad** de un ambiente distribuido es la unidad de cómputo de ambiente informático distribuido.

Cada entidad cuenta con las siguientes **capacidades**:

- Acceso de lectura y escritura a una memoria local, no compartida con otras entidades:
	- Registro de estado: `status(x)`.
	- Registro de valor de entrada: `value(x)`.
- Procesamiento local.
- Comunicación: preparación, transmisión, recepción de mensajes.
- Establecer y restablecer un reloj local (temporizador).

### Eventos Externos

La entidad solamente responde a eventos externos (es reactiva). Los posibles eventos externos son:

- Llegada de un mensaje
- Activación del reloj
- Un impulso espontáneo.

A excepción del impulso espontáneo, los eventos se generan dentro de los límites del sistema.

### Comunicación

Una entidad se comunica con otras entidades mediante mensajes. Un mensaje es una secuencia finita de *bits*.

Puede ocurrir que una entidad solo pueda comunicarse con un subconjunto del resto de las entidades, definimos entonces:

- $N_{\text{out}}(x) \subseteq E:$ Es el conjunto de entidades a las cuales $x$ puede enviarles un mensaje directamente.
- $N_{\text{in}}(x) \subseteq E:$ Es el conjunto de entidades a las cuales $x$ puede enviarles un mensaje directamente.

## Reglas y Comportamientos

Una **acción** es una secuencia finita e indivisible de operaciones. Es atómica porque se ejecuta sin interrupciones.

Una **regla** es la relación entre el evento que ocurre y el estado en el que se encuentra la entidad cuando ocurre dicho evento, de modo tal que:

$$
\text{estado} \times \text{evento} \to \text{acción}
$$

Para cada posible evento y estado debe existir una única regla.

El **comportamiento**, o *behaviour* de una entidad El conjunto $B(x)$ de todas las reglas que obedece una entidad $x$. También es llamada **protocolo** o **algoritmo distribuido** de $x$.

El **comportamiento colectivo** del sistema se define como la unión de todos los comportamientos, tal que:

$$
B(E) = B(x): \forall x \in E
$$

El comportamiento colectivo es **homogéneo** si todas las entidades que lo componen tienen el mismo comportamiento, o sea:

$$
\forall x,y \in E, B(X) = B(Y)
$$

> [!note] Propiedad
> Todo comportamiento colectivo se puede transformar en homogéneo.

## Axiomas

Definimos los axiomas a partir de los cuales trabajaremos:

- **Retrasos finitos en la comunicación:** En la ausencia de fallas, los retrasos en la comunicación tienen una duración finita.
- **Orientación local:** Una entidad puede distinguir entre sus vecinos de salida $N_\text{out}$ y entre sus vecinos de entrada $N_\text{in}$.
	- Una entidad puede distinguir qué vecino le envía un mensaje.
	- Una entidad puede enviar un mensaje a un vecino específico.

### Restricciones de Confiabilidad

Algunas restricciones respecto a la confiabilidad que podremos asumir:

- La entrega es **garantizada**, cualquier mensaje enviado será recibido con su contenido intacto.
- Si hay confiabilidad **parcial**, no ocurrirán fallas.
- Si hay confiabilidad **total**, no han ocurrido ni ocurrirán fallas.

### Restricciones Temporales

Algunas restricciones temporales que podremos asumir:

- Los relojes están **sincronizados**. Esto implica que todos los relojes locales se incrementan simultáneamente, y el intervalo de incremento es constante.
- Si los **retardos** de comunicación son **acotados**, existe una constante $\Delta$ tal que en ausencia de fallas el retardo de cualquier mensaje en el enlace es a lo sumo $\Delta$.
- Si los **retardos** de comunicación son **unitarios**, en ausencia de fallas, el retardo de cualquier mensaje en un enlace es igual a una unidad de tiempo.

## Costo y Complejidad

Son las medidas de comparación de los algoritmos distribuidos:

- **Cantidad de actividades de comunicación:**
	- Cantidad de transmisiones o costo de mensajes, $M$.
	- Carga de trabajo por entidad, y carga de transmisión.
- **Tiempo:**
	- Tiempo total de ejecución del protocolo.
	- Tiempo ideal de ejecución: tiempo medido bajo ciertas condiciones, como retardos de comunicación unitarios y relojes sincronizados.

## Tiempo y Eventos

Los eventos desencadenan acciones en un tiempo futuro. Los distintos retardos resultan en distintas ejecuciones del protocolo con posibles resultados diferentes.

- Los eventos disparan acciones que pueden generar nuevos eventos
- Si suceden, los nuevos eventos ocurrirán en un tiempo futuro: `Future(t)`.
- Una ejecución se describe por la secuencia de eventos que ocurrieron.

## Estado y Configuraciones

El estado interno de $x$ en el instante $t$ se conoce como $\sigma(x, t)$. Este es el contenido de los registros de $x$, y el valor del reloj $c_x$ en el instante $t$.

El estado interno de una entidad cambia con la ocurrencia de eventos.

Sea una entidad $x$ que recibe el mismo evento en dos ejecuciones distintas, y $\sigma_1, \sigma_2$ los estados internos. Si $\sigma_1 = \sigma_2$, entonces el nuevo estado interno de $x$ será el mismo en ambas ejecuciones.

## Conocimiento

El conocimiento **local** es el contenido de la memoria local de $x$ y la información que se deriva. En ausencia de fallas, el conocimiento no puede perderse.

Los tipos de conocimiento son:

- **Información métrica:** Información numérica sobre la red. Esto puede ser el número de nodos del grafo, el número de arcos del grafo, el diámetro, etc.
- **Propiedades topológicas:** Conocimiento sobre propiedades de la topología. Ejemplo: el grafo es un anillo, el grafo es acíclico, demás.
- **Mapas topológicos:** Un mapa de la vecindad de la entidad hasta una distancia $d$. Por ejemplo, una matriz de adyacencia del grafo.
