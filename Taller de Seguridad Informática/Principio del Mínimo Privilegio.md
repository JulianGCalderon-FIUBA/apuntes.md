### Mínimo Privilegio

Un sujeto solamente debe tener asignados los privilegios que necesita para completar su tarea asignada.

- Si el sujeto no necesita un permiso, no debería tenerlo
- Los privilegios deberían ser asignados de acuerdo al _rol_ que cumple el sujeto
- Si alguna acción específica requiere elevar el nivel de privilegio que tiene un sujeto, esos derechos deben ser retirados _inmediatamente_ luego de completar esa acción.

Muchos sistemas implementan su sistema de permisos de forma insuficientemente granular: por ejemplo, en UNIX y similares, el usuario _root_ tiene permiso para todo, de manera que el encargado de hacer los _backups_ tiene la posibilidad de borrar archivos de los usuarios. Al mismo tiempo, esto está mitigado por el comando `sudo`.

- Permite ejecutar programas con los privilegios de otro usuario.
- Permite configurar con precisión los usuarios que tienen derecho de hacerlo, y para qué programas.