Existen dos enfoques posibles a la configuración de las *forwarding* y *flow tables:*

- **Per-router Control:** Un algoritmo de ruteo es ejecutado en cada router, realizando tanto funciones de envío como de ruteo. Los routers tienen un componente que se comunica con otros routers para computar los valores de la tabla
- **Logically Centralized Control:** Existen un controlador lógico y centrado que computa y distribuye las tablas de envío para cada router. El controlador interactúa con el **control agent** (CA) de cada router a través de un protocolo definido. Este *control agent* tiene funcionalidad mínima, su trabajo es comunicarse con el **controller**.

	El controlador es accedido como si fuese un único punto central de servicio, aunque probablemente esté implementado a través de múltiples servidores por seguridad y escalabilidad.
