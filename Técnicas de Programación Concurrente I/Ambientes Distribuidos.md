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
