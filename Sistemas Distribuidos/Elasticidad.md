La elasticidad es la capacidad de un sistema para poder modificar dinámicamente los recursos del sistema adaptándose a patrones de carga. Es un término utilizado en arquitecturas *cloud*, y requiere soporte de la infraestructura

## Componentes

Para que esto sea posible, es necesario al menos los siguientes componentes:

- **Application Load Balancer**: Esto permite que nuevas instancias reciban tráfico de forma instantáneo. Además debemos saber si el servicio está preparado para recibir dicho tráfico. De forma análoga, debe permitir que servicios degradados dejen de recibir tráfico.
- **Autoscaler**: Es un componente que tiene capacidad para incrementar (*scale in*) o decrementar (*scale out*) las instancias del sistema, a partir de métricas de su funcionamiento.
- **Monitoring Automático**: Permite ver métricas sobre CPU, memoria, I/O, networking, etc. por cada servicio y por cada instancia. Esta información puede ser utilizada por el *autoscaler*

## Amazon Web Services (AWS)

Es una plataforma de computación en la nube, ofrecida por Amazon.

- Como *application load balancer*, utiliza *Amazon Elastic Load Balancer*. Este redirecciona tráfico a instancias (EC2), incluso en diferentes zonas. Además, interactua con instancias para verificar su estado.
- Como *autoscaler*, utiliza *Amazon Autoscalling*. Este permite definir una cantidad minima, deseada, y máxima de instancias para un grupo de *autoscalling*. Soporta distintas políticas para lograr distintos objetivos (*scalling* dinámico vs. manual).
- Como *monitoring automático*, utiliza *Amazon CloudWatch*. Este ofrece métricas globales automatizadas, y además permite agregar métricas propias.

![[Elasticidad 1737317968.png]]
