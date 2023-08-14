Al igual que ***mobile IP***, ***GSM*** adopta un enfoque de ***indirect routing***. Primero, el llamado se envía a la red local del usuario, y luego a la red visitada. En terminología de ***GSM***, la red local se conoce como ***home public land mobile network (home PLMN)***. Las responsabilidades entre ambas redes son distintos:

- La red local mantiene una base de datos conocida como ***home location register (HLR)***, que contiene el teléfono celular permanente de un usuario, e información de perfil sobre sus subscriptores. Ademas, contiene la dirección actual de cada uno de sus suscriptores. El ***HLR*** tiene suficiente información para obtener una dirección en la red visitada. Un ***switch especial*** es contactado en la red local, conocido como ***Gateway Mobile Services Switching Center (GMSC)***. Nos referiremos a el como el home MSC.
- La red visitada mantiene una base de datos conocida como ***visitor location register (VLR).*** Esta contiene una entrada por cada móvil actualmente residente en la red. Esta base de datos es también localizada dentro del ***MSC de la red.***

![[Managing Mobility in Cellular Networks 1.png]]

## 1. Routing Calls to a Mobile User

Consideremos un escenario simple para el caso de un usuario móvil residiendo en una red extranjera:

1. El correspondiente llama al usuario móvil. Los digitos son suficientes para hallar la red local de forma global. La llamada es dirigida a través del **PSTN** al home ***MSC.***
2. El ***home MSC*** recibe el llamado e interroga al ***HRL*** para determinar la ubicación del usuario móvil. En el caso mas simple, devuelve el ***mobile station roaming number (MSRN),*** al cual llamaremos ***roaming number***. Si no conoce este numero, devolverá la dirección del ***VLR*** de la red visitada. Luego, consultará a la ***VLR*** para solicitar un ***roaming number*** para el usuario.
3. Una vez obtenido el **roaming number**, el ***home MSC*** configura la segunda parte de la llamada a través de la red con el ***MSC*** en la red visitada.

Cuando un dispositivo móvil entra a una red cubierta por un nuevo ***VLR***, este debe registrarse con la red visitada. El visited ***VLR*** envía una actualización de localización al ***HLR*** del móvil. Este informará la dirección de roaming del móvil, o la dirección del ***VLR.*** Ademas, el ***VLR*** obtiene información de subscripciones del ***HLR*** sobre el móvil para determinar que servicios deben ser acordados con el usuario.

## 2. Handoffs in GSM

Un ***handoff*** ocurre cuando una estación móvil cambia su asociación de una estación base a otra durante una llamada. Esto puede ocurrir por otras diversas razones, ademas de la movilidad de un nodo, incluyendo que la señal de la estación actual deterioro lo suficiente y esta en peligro de perderse, o una celda fue sobrecargada y debe delegar móviles a otras celdas cercanas.

![[Managing Mobility in Cellular Networks 2.png]]

Mientras esta asociado a una estación base, un móvil periódicamente mide la fuerza de de una ***beacon signal*** desde su propia estación base, y las cercanas. Basándose en esta métrica, puede iniciarse un ***handoff***. Este proceso, se da en los siguientes pasos:

1. La estación base anterior le informa a la ***visited MSC que ocurrirá un*** handoff, y el **BS** (o multiples) a los que se realizará el ***handoff***.
2. El ***visited MSC*** inicia un ***path setup*** al nuevo **BS,** reservando recursos necesarios para redireccionar la llamada, e indicándole al nuevo **BS** que esta por ocurrir un ***handoff***
3. El nuevo *BS* reserva los recursos y activa el canal de radio a utilizar
4. El nuevo **BS** envía una señal al ***visited MSC*** y al anterior **Bs** que ya es estableció el camino ***visited-MSC-to-new-BS***. Ademas, provee toda la información que necesitará el móvil para asociarse al nuevo **BS**.
5. El móvil es informado que debe realizar un *handoff*. Hasta este punto, el móvil no estaba al tanto de que la red estaba preparando un cambio.
6. El móvil y el nuevo **BS** intercambian uno o mas mensajes para activar el nuevo canal por completo
7. El móvil envía un mensaje de finalización de ***handoff*** al nuevo **BS**, el cual es enviado al ***visited MSC***. Este redirige la llamada al nuevo **BS**.
8. Los recursos reservados para el anterior **BS** son reservados.

Cuando hay multiples cambios de estación base, GSM define la noción de ***anchor MSC***. Este es el ***MSC*** visitado cuando comienza una llamada, y permanece constante durante la misma. La llamada siempre será dirigida al home MSC, luego al anchor MSC, y de ahi al visited MSC. Otra alternativa sería la de simplemente encadenar las ***MSC*** visitadas.
