En estos ambientes, una falla en una entidad que no conocemos puede ocasionar un error en nuestro sistema.

## Entidades

Una **entidad** de un ambiente distribuido es la unidad de cómputo de ambiente informático distribuido.

Cada entidad cuenta con las siguientes **capacidades**:

- Acceso de lectura y escritura a una memoria local, no compartida con otras entidades:
	- Registro de estado: `status(x)`.
	- Registro de valor de entrada: `value(x)`.
- Procesamiento local.
- Comunicación: preparación, transmisión, recepción de mensajes.
- Establecer y restablecer un reloj local.

### Eventos Externos

La entidad solamente responde a eventos externos (es reactiva). Los posibles eventos externos son:

- Llegada de un mensaje
- Activación del reloj
- Un impulso espontáneo.

A excepción del impulso espontáneo, los eventos se generan dentro de los límites del sistema.

## Reglas y Comportamientos
