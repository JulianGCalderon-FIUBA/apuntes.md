Al ahora de realizar él [[Diseño del Sistema]], se emplean distintos principios.

## Sujetos y Objetos

Un objeto es lo que contiene o almacena datos:

- Archivos
- Memoria
- Dispositivos
- Paquetes de red

Un sujeto son aquellas entidades que pueden acceder o manipular objetos:

- Usuarios
- Procesos

## Mínimo Privilegio

Un sujeto sólo debe tener asignados los privilegios que necesita para completar su tarea asignada.

- Si el sujeto no necesita un permiso, no debería tenerlo
- Los privilegios deberían ser asignados de acuerdo al _rol_ que cumple el sujeto
- Si alguna acción específica requiere elevar el nivel de privilegio que tiene un sujeto, esos derechos deben ser retirados _inmediatamente_ luego de completar esa acción.

Muchos sistemas implementan su sistema de permisos de forma insuficientemente granular: por ejemplo, en UNIX y similares, el usuario root tiene permiso para todo, de manera que el encargado de hacer los _backups_.

tiene la posibilidad de borrar archivos de los usuarios. Al mismo tiempo, esto está mitigado por el comando

_sudo_:

● Permite ejecutar programas con los privilegios de otro usuario

● Permite configurar con precisión los usuarios que tienen derecho de hacerlo, y para qué programas.
