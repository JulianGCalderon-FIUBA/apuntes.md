**Latencia:** La latencia es el retardo entre un estímulo y la respuesta. Es un valor conceptual

RTT: El RTT es una medida aproximada de la latencia, es el tiempo que le toma a un paquete ir a un host de destino y volver. Una forma de medirlo es a través del comando `ping`.

Tiene cuatro componentes principales:

- **Tiempo de Inserción:** Es el tiempo que tarda en introducirse el paquete en el canal del enlace. Depende del tamaño del paquete y la capacidad del enlace.
- **Tiempo de Propagación:** Es el tiempo que tarda en propagarse el paquete en el canal de enlace. Depende de la velocidad del enlace y de la distancia entre las interfaces.
- **Tiempo de Procesamiento:** Es el tiempo que tarda el router en procesar el paquete y decidir a qué puerto de salida enviarlo. Suele ser despreciable.
- **Tiempo de Encolado:** Es el tiempo que tarda un paquete desde que es introducido a la cola de salida hasta que es efectivamente transmitido. Depende del nivel de congestión de la red.

La latencia total se calculará como la sumatoria de los tiempos mencionados para cada nodo atravesado, tanto en la idea como en la vuelta.

Si despreciamos el tiempo de encolado y de procesamiento, entonces podremos calcular la latencia de la siguiente forma:

Sea $L$ el tamaño del paquete, $R$ el ancho de banda del enlace, $D$ la distancia entre los nodos (largo del enlace) y $c$ la velocidad de propagación del medio, entonces:

$$
T_{\text{inserción}} = \frac{L}{R}
$$

$$
T_{\text{propagación}} = \frac{D}{c}
$$

Nota: trabajar con las mismas unidades para evitar errores de cálculo

Luego, para cada enlace $i$ en los enlaces atravesados $E$, calculamos su tiempo total $T_i = T_{i,\text{inserción}} +T_{i,\text{propagación}}$, luego calcularemos el tiempo total como:

$$
T = \sum_{i\in\text{E}} T_i
$$
