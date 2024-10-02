## Nombre

Los nombres permiten inequívocamente a una entidad dentro de un sistema. Deben describir a la entidad. Abstraer al recurso de las propiedades que lo atan al mismo con el sistema (lugar geográfico, dirección de red)

## Direccionamiento

El direccionamiento, o *addressing*, es la relación entre un nombre y una dirección. La dirección puede cambiar, pero el nombre no.

## Atomicidad

Es cuando los mensajes deben entregarse a todos o a ninguno. En estos casos es necesario realizar ACK de los mensajes, demorar el delivery de los paquetes recibidos.

Se puede reintentar el renvio de los mensjaes para asegurar la entrega, o tener un mensaje de "rollback" para notificar al grupo que se debe enviar cierto mensaje.
