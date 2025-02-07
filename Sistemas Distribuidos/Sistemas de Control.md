Es muy común que los sistemas de control sean a su vez, [[Sistemas de Tiempo Real]]. Un sistema de control son escenario donde un sistema busca controlar de forma manual o automática, algún elemento del medio físico.

Por ejemplo, en la industria podemos encontrar:

- Esquemas de irrigación.
- Procesos de transferencia térmica.
- Procesos químicos.
- Líneas de producción.

En la vida cotidiana, podemos encontrar:

- Termostatos.
- Ascensores.
- Expendedoers de líquidos.
- Control de luminosidad.
- Aire Acondicionado

## Nociones Básicas

El **control** es la capacidad de actuar para garantizar el comportamiento de un suceso.

Un **proceso** es toda sucesión de operaciones que se desea controlar.

Una **planta** a cualquier sistema físico que se desea controlar.

El **controlador** es el sistema encargado de determinar la actuación para conseguir cierto objetivo o proceso. El **actuador** es el elemento físico que frente a señales del controlador opera sobre el proceso.

Hay dos tipos de variables:

- **Variable controlada**: Es la variable que se mide o se controla, y es la variable de salida del sistema. Por ejemplo, la temperatura en un sistema de aire acondicionado.
- **Variable manipulada**: Es la variable que podemos modificar, y afecta el valor de la variable controlada. Por ejemplo, la velocidad del ventilador en un sistema de aire acondicionado.

Una **perturbación** es una señal que afecta negativamente el valor de la salida del sistema. Por ejemplo, abrir una ventana en un sistema de aire acondicionado.

## Control a Lazo Abierto

En un sistema de lazo abierto, la salida no afecta la acción de control. Por ejemplo, los aires acondicionados antiguos sin control de temperatura.

![[Sistemas de Control 1738888270.png]]

## Control a Lazo Cerrado

En un control a lazo cerrado o realimentado (*feedback*), se utiliza la información sobre el estado del sistema para actuar sobre el sistema, y llevar la salida del mismo a los valores deseados. Por ejemplo, un aire acondicionado moderno, que analiza la temperatura y decide como actuar para llegar al objetivo.

![[Sistemas de Control 1738888363.png]]
