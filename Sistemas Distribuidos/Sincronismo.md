Un algoritmo es **sincrónico** si sus acciones pueden ser delimitadas en el tiempo

- **Sincronismo**: Entrega de un mensaje posee un *timeout* conocido.
- **Parcialmente sincrónico:** Entrega de un mensaje posee un *timeout* conocido o bien es el mismo.
- **Asincrónico**: Entrega de un mensaje no posee un *timeout* asociado.

## Propiedades

- **Timeout:** Todo mensaje enviado va a ser recibido antes de un $t$ conocido.
- **Tiempo:** Es el tiempo que tarda en ser recibido una vez enviado.
- **Steadiness:** Es la maxima diferencia entre el mínimo y el máximo tiempo de delivery de cualquier mensaje.
- **Tightness**: Es la maxima diferencia entre los tiempos de delivery
