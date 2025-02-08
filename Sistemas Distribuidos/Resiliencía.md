La resiliencia o confianza (*dependability*) es la medida de la confianza en el sistema: Tiene distintos factores:

- **Disponibilidad**
- **Fiabilidad**
- **Mantenibilidad**
- **Seguridad**
- **Durabilidad**

La resiliencia consiste en la capacidad de mantener un nivel aceptable de servicio en presencia de fallos.

Se dice que un sistema tiene degradación suave (*graceful degradation*) cuando el comportamiento se degrada, pero continúa siendo aceptable.

## Disponibilidad y Fiabilidad

Son dos conceptos que estan relacionados:

- **Disponibilidad** (*availability*): La probabilidad de que el sistema esté operando cuando se lo precisa.
- **Fiabilidad** (*reliability*): La capacidad del sistema para dar un servicio correcto de forma continúa. No solo tiene que estar disponible, sino que tiene que hacerlo de forma correcta.

La mejor estrategia depende de varios factores:

- Costos y presupuesto disponible.
- Necesidades de performance y escalabilidad.
- Necesidades heterogéneas de cada componente.

Para tomar las decisiones adecuadas, debemos pensar en el origen de los errores: no todos los errores son de hardware (20% aproximadamente). Hay muchos errores relacionados a errores de software, y errores de humanos (de configuración).

## Mantenibilidad

La **mantenibilidad** (*maintainability*) es la cantidad de tiempo que se requiere para recuperar el sistema (ej. repararlo o actualizarlo.

Para garantizarla, se crea una imagen para cada cambio a desplegar. No se manejan con estados mutables. Esto permite automatizar los despliegues, sin que haya humanos realizándolo de forma directa. Esto reduce la probabilidad de errores humanos.

![[Tolerancia a Fallos 1738378604.png]]

Esta inmutabilidad nos permite realizar trazabilidad de las imágenes, para ver de donde vinieron.

Las actualizaciones son inmediatas, ya que únicamente implican ejecutar la imagen y configurar el balanceador de carga para que mueva las consultas al nuevo contenedor.

Los contenedores pueden ser replicados y relanzados ante errores, lo que aumenta la disponibilidad del sistema.

Al usar imágenes, puedo desacoplar el sistema de la infraestructura (IaaS) y de la plataforma (PaaS). Al especificar únicamente la imagen, no es necesario configurar la infraestructura completa.

Se puede realizar testing de imágenes antes del despliegue, ya que la configuración en el ambiente de testing es igual al ejecutado en producción.

Las imágenes viejas pueden ser almacenadas para un posible rollback.

## Durabilidad

La **durabilidad** (*durability*) es la probabilidad de que un dato persistido se pueda recuperar.

## Seguridad

La **seguridad** (*safety*) implica que en presencia de fallos, no ocurre nada catastrófico.

> El sistema debe poder ser recuperado automática o manualmente ante cualquier tipo de falla

Es necesario definir un **Disaster Recovery Process** para la infraestructura y los datos. Son situaciones improbables pero no imposibles, y debemos poder resolverlas.

El tiempo de restauración debe ser conocido para poder garantizar los SLA.

Los escenarios catastróficos deben ser testeados. Se puede forzar la caída de algunos componentes para ver como se comporta el sistema, o para ver si el protocolo funciona correctamente.
