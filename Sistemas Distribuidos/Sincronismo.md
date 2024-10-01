Un algoritmo es **sincrónico** si sus acciones pueden ser delimitadas en el tiempo

- **Sincronismo**: Entrega de un mensaje posee un *timeout* conocido.
- **Parcialmente sincrónico:** Entrega de un mensaje posee un *timeout* conocido o bien es el mismo.
- **Asincrónico**: Entrega de un mensaje no posee un *timeout* asociado.

## Propiedades

- **Timeout:** Todo mensaje enviado va a ser recibido antes de un $t$ conocido.
- **Tiempo:** Es el tiempo que tarda en ser recibido una vez enviado.
- **Steadiness:** Es la máxima diferencia entre el mínimo y el máximo tiempo de delivery de cualquier mensaje recibido por un proceso.
	- Define la varianza con la cual un proceso observa que recibe los mensajes.
	- Define que tan constante es la recepción de mensaje.
- **Tightness**: Es la máxima diferencia entre los tiempos de delivery para cualquier mensaje.
	- Define la simultaneidad con la cual un mensaje es recibido por múltiples procesos.
