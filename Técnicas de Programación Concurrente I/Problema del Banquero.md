## Problema

Un viejo banquero retirado se mudó a vivir al campo lejos de toda la tecnología.

Para vivir, invierte la plata que hizo durante sus años de trabajo mediante los amigos que tiene en diversos fondos de inversión.

Al inicio de cada semana, les envía por correo el dinero para invertir a sus amigos; luego espera hasta el final de la semana a que le envíen a su buzón el resultado de esas inversiones. Las inversiones pueden dar una ganancia entre -50% y 50% de lo invertido.

A todos los amigos les envía el mismo monto, y el dinero resultante lo vuelve a invertir la próxima semana.

## Solución con Locks

Para resolver el problema con *locks*, debemos modificar levemente el enunciado, pues no podriamos sincronizar el envío y recepción de dinero.

### Modificación del Problema

Al tiempo el señor fallece, y los hijos deciden que los inversores sigan trabajando el dinero pero con algunas condiciones extra.

Los hijos no se hacen cargo de nada, sino que los inversores toman dinero de la cuenta y lo devuelven al final de la semana.

Cada inversor puede reinvertir el capital y hasta 50% de la ganancia propia de la semana anterior, o bien todo el capital en caso de haber perdido.

Las inversiones, además, deberán ser menos riesgosas, pudieron dejar de -10% a +10%.

### Solución

Para resolverlo podríamos tener una estructura compartida "cuenta" que esté distribuida entre hilos y utilice locks para garantizar un acceso seguro. Para realizar esto es necesario envolverla en un `Rwlock` y luego en un `Arc`.

Al inicio de la semana, los inversores toman el dinero que le corresponde y luego lo devuelven.

El único inconveniente podría ser que no podemo
