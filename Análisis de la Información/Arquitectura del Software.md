## Atributos de Calidad

Hay dos tipos de atributos de calidad:

- **Funcionalidad:** Habilidades del sistema para hacer el trabajo para el que fue diseñado.
- **Atributos:** Características no funcionales que se consideran deseables en un sistema.

Muchas veces, estos atributos de calidad estarán implícitos y dependerán del equipo de desarrollo. A veces, debemos pensar que atributos de prioridad priorizar. Por ejemplo, seguridad empeorar la experiencia del usuario.

### Resiliencia

En las redes de computadora, resiliencia es la habilidad de proveer y mantener un nivel aceptable de servicio ante las fallas y desafíos que pueden surgir ante cualquier operación. Es necesario identificar estas posibles fallas y sus causas para poder garantizar esta cualidad.

Relacionado con minimizar el impacto que tienen las fallas, para que el sistema siga funcionando correctamente.

Si priorizamos la resiliencia, esto puede afectar la eficiencia del sistema, ya que estaremos destinando recursos a protegernos de las fallas, lo que puede añadir trabajo extra al sistema. Otro ejemplo puede ser la escalabilidad.

La disponibilidad y la confianza en sí solos no son suficientes para un sistema, no importa que tan bien diseñado esté un sistema, siempre podrá fallar.

## Arquitecturas y Patrones

**Pipe and Filter:** Componentes conectados a través de conectores que procesan información. Consiste en manipular los datos de forma secuencial aplicando múltiples funciones hasta llegar al resultado

***N-Tier:*** Consiste en una separación física de las distintas capas de una aplicación. Relacionado con la arquitectura de separación en capas.

### Orientación a Eventos

En una arquitectura P2P (punto a punto). Los componentes deben interactuar directamente con los otros servicios que utiliza. Si uno de sus componentes falla, el evento completo fallará.

En la arquitectura orientada a eventos, los eventos se colocan en una cola de eventos. Los sistemas estarán conectados a esta cola y registrarán los eventos en cuanto esté disponible.

### REST API

### Microservicios

Consiste en separar un sistema en múltiples sistemas independiente entre sí. Esto genera una arquitectura más resiliente. Los sistemas se pueden comunicar entre sí a través de sus interfaces públicas (no es una biblioteca). Esta separación no se realiza según su función, sino según el negocio.

El desarrollo es el de un producto, no el de un proyecto. El sistema se crea y se mantiene por el mismo equipo.

Los sistemas deben ser diseñados para que fallen, tendremos en cuenta estas posibilidades en el momento del desarrollo.

Los microservicios son productos que forman parte de una plataforma. Esto permite que miles de desarrolladores trabajen en un mismo proyecto, separando las responsabilidades y los servicios en distintos equipos. Se aíslan contextos de trabajos para los equipos.
