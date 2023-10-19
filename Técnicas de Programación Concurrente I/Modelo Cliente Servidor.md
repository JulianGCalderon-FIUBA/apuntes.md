Tendremos un cliente y un servidor

- El cliente es activo porque inicia la interacción con el servidor.
- El servidor es pasivo, existe previo a la existencia del cliente y espera a recibir los pedidos de los clientes.

## Concurrencia

Existen dos tipos de servidor, según su forma de resolver pedidos:

- Iterativo: Atiende las peticiones de a una a la vez.
- Concurrente: Puede atender varias peticiones a la vez.

## Arquitecturas

Tendremos dos tipos de arquitecturas

- Arquitectura de dos niveles: El cliente interactúa directamente con el servidor
- Arquitectura de tres niveles: Tendremos una capa intermedia *middleware*, ubicada entre el cliente y el servidor, y provee principalmente seguridad y balanceo de carga.

## Modelo de Capas

Los protocolos de internet suelen ser ordenados en capas. Las capas le ofrecen servicios a sus capas superiores, y utilizan los servicios de las capas inferiores. Las capas de igual número en distintas computadoras se comunican virtualmente a partir del protocolo.

![[Sockets 1697723178.png|447]]

Este modelo se conoce como protocolo de capa $N$.
