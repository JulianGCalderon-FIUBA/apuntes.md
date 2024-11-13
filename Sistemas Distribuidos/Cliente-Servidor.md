Se definen roles para los participantes:

- Servidor como elemento pasivo y provee servicios
- Clientes activos que envían pedidos al servidor

La arquitectura tiene las siguientes características:

- Permite centralización en toma de decisiones.
- Suele asumirse que los servidores tienen más capacidades de hardware que los clientes.
- Los clientes deben conocer la ubicación del servidor para poder utilizarlo.
- El servidor no conoce la ubicación de los clientes.
- Los clientes no entablan comunicaciones entre sí, salvo a través del servidor.

Para obtener notificaciones por parte del servidor, se pueden utilizar modelos de *callback*, aunque no es su carácter natural: Hay dos alternativas principales:

- **Long polling**: El cliente se queda esperando, esperando a que haya alguna notificación.
- **Push notifications**: El cliente se conecta cada cierto tiempo, y pregunta si tiene alguna notificación para él. No es necesario que esté continuamente conectado.
