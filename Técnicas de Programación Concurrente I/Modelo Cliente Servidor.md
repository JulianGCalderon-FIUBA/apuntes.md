## Modelo Cliente Servidor

Tendremos un cliente y un servidor

- El cliente es activo porque inicia la interacción con el servidor.
- El servidor es pasivo, existe previo a la existencia del cliente y espera a recibir los pedidos de los clientes.

Tendremos dos tipos de arquitecturas

- Arquitectura de dos niveles: El cliente interactúa directamente con el servidor
- Arquitectura de tres niveles: Tendremos una capa intermedia *middleware*, ubicada entre el cliente y el servidor, y provee principalmente seguridad y balanceo de carga.

Existen dos tipos de servidor, según su forma de resolver pedidos:

- Iterativo: Atiende las peticiones de a una a la vez.
- Concurrente: Puede atender varias peticiones a la vez.
