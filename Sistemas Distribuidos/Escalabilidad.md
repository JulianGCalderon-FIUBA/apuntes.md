El objetivo de escalabilidad es el crecimiento,

- **Respecto del tamaño**: Agregando usuarios o recursos a controlar.
- **Respecto de la distribución geográfica**: Permitiendo dispersión, y acceder a usuarios en lugares lejanos.
- **Respecto de los objetivos administrativos del sistema**: Nuevas sintaxis, semánticas y servicios ofrecidos.

Para escalar un servicio, podemos usar **plataformas** para alta concurrencia. Estas plataformas aplican patrones ya conocidos y probados, y ofrecen escalamiento automático (con cierto límite). Están fuertemente vinculadas con una infraestructura o producto, y no será tan simple migrarlo a otra plataforma.

Otra opción es utilizar arquitecturas ad hoc y **personalizadas**, aunque necesitan de configuración y soporte adicional, y el escalamiento es manual (o automatizado por humanos). Al ser una solución manual, tenemos la posibilidad de migraciones a distintas plataformas.

## Patrones de Carga

A partir de como evoluciona la carga en el sistema según el tiempo, se definen distintos patrones de carga:

- **Predictable Burst**: Se conoce que en cierto determinado momento, la carga en el sistema aumentará, como por ejemplo: Navidad.
- **Unpredictable Burst**: Fluctuaciones impredecibles en la carga del sistema. Ante estas situaciones, podemos realizar un análisis estadístico para poder predecir la carga del sistema, y anticiparnos a estos momentos.
- **Periodic Processing**: Durante un determinado intervalo de tiempo, la carga del sistema cesa, como por ejemplo: Transacciones en un sistema bancario.
- **Start Small, Grow Fast**: Está relacionado con las startups exitosas. A medida que el servicio toma tracción, la carga en el sistema aumenta. El sistema debe ser pensado desde el inicio con esto en mente, para poder escalarlo.

![[Escalabilidad 1737314465.png]]

## Limitantes

Al momento de escalar un sistema, hay algunos factores que limitaran la capacidad del sistema:

- **Arquitectura**: Si la arquitectura no está preparada para escalar el sistema, necesitaremos rediseñar la arquitectura.
- **Algoritmos**: A menor escala, los algoritmos utilizados también son un factor importante, y en situaciones necesitamos cambiar los algoritmos utilizados para poder mejorar la performance del sistema.
- **Red**: Si la cantidad de datos a manejar es mayor a la que el sistema puede soportar, tendremos que aumentar el ancho de banda, pero esto lleva a una limitación financiera.
- **Datos**: Si el volumen de los datos es mayor a la capacidad de sistema, tendremos que mejorar el *storage* del sistema, pero esto también lleva a una limitación financiera.
- **Presupuesto**: Relacionado con el resto de limitantes, es posible que no tengamos presupuesto suficiente como para resolver los otros limitantes.
- **Restricciones Legales**: En algunas situaciones, restricciones legales pueden limitar la escalabilidad, como por ejemplo: los datos no pueden atravesar otros países.

## Técnicas

Existen distintas técnicas para escalar sistemas:

- **Escalamiento vertical**: Cuando un nodo físico del sistema se encuentra siendo un cuello de botella, se puede agregar recursos al nodo.
- **Escalamiento horizontal**: Si la arquitectura está preparada para tener componentes redundantes, podremos agregar más nodos, balanceando la carga en el sistema. En esta caso, podemos tener en cuenta la proximidad geográfica de los componentes, llevando los componentes cerca de los usuarios.
- **Fragmentación de datos**: Los datos pueden ser particionados de forma que los datos con mayor afinidad entre sí estén más cercanos.
- **Componentización**: En lugar de tener un sistema monolítico, podremos separar el sistema en diferentes subservicios que se comunican entre sí. Esto permite escalar servicios específicos.
- **Optimizar algoritmos**: En caso de que se pueda mejorar, al mejorar los algoritmos podemos mejorar la capacidad de cómputo del sistema, o la carga en la red (si logramos que los mensajes sean más pequeños).
- **Asincronismo**: Al mantener sincrónico únicamente lo estrictamente necesario, mejoramos la velocidad de respuesta del sistema, aunque el procesamiento se realice de forma asincrónica. Esto está limitado por las reglas de negocio.
