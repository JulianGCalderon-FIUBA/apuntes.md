---
title: Wireless Links and Network Characteristics
---

Podemos encontrar numerosas diferencias importantes entre un enlace y uno inalámbrico:

- **Decreasing Signal Strength:** La radiación electromagnética es atenuada a medida que atraviesa materia (por ejemplo, una pared). Esta reducción en la fuerza de la señal se conoce como **path loss**
- **Interference from Other Sources:** Las centrales de radio que transiten a la misma frecuencia interfieren unas con otras. Además, el ruido electromagnético del ambiente (un microondas, un motor) también puede ocasionar interferencia.
- **Multipath Propagation:** Esta ocurre cuando porciones de ondas electromagnéticas son reflejadas en distintos objetos, causando que tomen caminos distintos entre el remitente y el receptor.

Esto sugiere que la corrupción de paquetes es frecuente en las redes inalámbricas. Debido a esto, los protocolos inalámbricos de capa de enlace emplean no solo poderosas técnicas de corrección de errores, sino también envío confiable a nivel de enlace.

Desde el lado del receptor, un host recibirá una combinación de una vieron degradada de la señal transmitida originalmente y ruido de fondo del ambiente. La medida **signal-to-noise (SNR)** es utilizada para medir la fuerza relativa de la señal recibida. La unidad de medida más frecuente es la de decibeles (dB). La medida **bit-error-rate (BER)** es utilizada para medir la probabilidad de un error de bit. Analizaremos ambas medidas en conjunto:

- **For a given modulation scheme, the higher the SNR, the lower the BER.** El remitente puede incrementar el SNR al incrementar la fuerza de transmisión. Luego, puede reducir el BER al incrementar la fuerza de transmisión. Esta técnica pierde la utilidad a partir de cierto límite, ya que también hay desventajas asociadas a incrementar la potencia: se debe utilizar más energía para enviar información, y la señal enviada puede interferir con otras señales.
- **For a given SNR, a modulation technique with a higher bit transmission rate will have a higher BER**. La decisión de la técnica de modulación dependerá de la máxima tasa de errores permitida. Esta característica dio surgimiento a la siguiente y final.
- **Dynamic selection of the physica-layer modulation technique can be used to adapt the modulation technique to channel conditions.** Para los casos de dispositivos móviles, el SNR (y entonces el BER) puede cambiar en respuesta al desplazamiento o cambios en el entorno. Se utiliza una selección dinámica de técnicas de modulación para adaptarse mejor a las condiciones dadas.

Existen múltiples diferencias más entre las conexiones alámbricas y las inalámbricas. El llamado **hidden terminal problem** ocurre cuando dos estaciones $A, B$ no se escuchan entre sí debido a la obstrucción de, por ejemplo, una montaña. Pero sus transmisiones hacia una estación compartida $C$ si interfieren. Las estaciones no estarán al tanto de la interferencia. Esta es una colisión indetectable.

Otro escenario de colisiones indetectables es el de la atenuación de las señales a medida que se propagan por el medio. La señal de dos estaciones $A, B$ pueden dispersarse antes de llegar a la otra estación, pero interferir en el envío a una estación intermedia $C$

## 1. CDMA

El protocolo **code division multiple access (CDMA)** pertenece a la familia de protocolos de partición de canales, prevalece en las redes inalámbricas LAN y las tecnologías de celular.

En este protocolo, cada byte multiplicado por una señal (el código) antes de ser enviada. La señal varía a una tasa mucho más rápida que la de la secuencia original de bits, (conocida como *chipping rate*).

Representando el bit 0 con un valor de -1, y el bit 1 con un valor de 1, el protocolo funciona bajo la suposición de que las interferencias son aditivas. Si tres señales transmiten un 1, y una señal transmite un -1, la señal resultante será de 2. En la realidad, las señales se atenúan y puede ser difícil de alcanzar los escenarios mostrados.

Sorprendentemente, si se seleccionan los códigos de entrada de forma cuidadosa, el receptor puede recuperar los cuatro valores enviados a partir de la señal resultante.
