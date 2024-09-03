Hay muchos formatos para enviar mensajes entre procesos.

## Binario

El rendimiento es alto debido al tamaño de los mensajes. En teoría, el tamaño de los mensajes es mínimo. La comprensión puede no ser necesaria.

Se puede autogenerar código para serializar. Algunos ejemplos son: Google Protobuf, Thrift, ASN.1. No todos los lenguajes tienen soporte. En general no es óptimo para el caso particular.

Un esquema típico es TLV: Tipo, Longitud, Valor. El valor admite tipos internos.

## Texto Plano

El rendimiento es bajo debido a que el tamaño de los mensajes es mayor. Se le puede agregar comprensión para reducir el tamaño, pero esto agrega overhead.

Se pueden utilizar formatos existentes como JSON, XML, HTTP. Es fácil de debuggear, ya que existen aplicaciones existentes con soporte para estos casos (CURL).

## Longitud de Paquete

Se pueden utilizar delimitadores para definir el fin del paquete, o utilizar tamaños fijos. Cada uno tiene sus ventajas y desventajas. En un esquema mixto, se pueden utilizar el que mejor se adapte para cada mensaje.
