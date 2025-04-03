Una especificación es una enunciación (formal o informal) del funcionamiento deseado del sistema. Los requerimientos pueden ser funcionales, o de seguridad.

El diseño de un sistema traduce las especificaciones del mismo en una serie de componentes que las implementan.

Se dice que el diseño satisface las especificaciones si, bajo todas las circunstancias relevantes, el diseño no permite que el sistema viole las especificaciones.

Según los términos en que se expresen, verificar que un diseño satisface una especificación puede ser una tarea ardua. Si están expresados en términos matemáticos, se pueden utilizar métodos formales (que hay que asistir en algún momento), y si están en lenguaje natural, hay que buscar una explicación satisfactoria (de por qué sí o por qué no satisface los requerimientos).

Dado un diseño, la implementación crea un sistema que satisface ese diseño. Si el diseño satisface las especificaciones, por transitividad la implementación satisfará las especificaciones.

- Se dice que un programa es _correcto_ si satisface las especificaciones
- Verificar que el programa es correcto es mucho más arduo que verificar un diseño.

En una verificación formal, cada instrucción es una operación matemática. Es posible, en teoría, en la práctica solamente se usa para cosas pequeñas y críticas. El lenguaje en que se escribe no es el lenguaje que se ejecuta.

## Principios de Diseño

Al ahora de realizar él [[Diseño del Sistema]], se emplean distintos principios.

### Sujetos y Objetos

Un objeto es lo que contiene o almacena datos:

- Archivos
- Memoria
- Dispositivos
- Paquetes de red

Un sujeto son aquellas entidades que pueden acceder o manipular objetos:

- Usuarios
- Procesos

### Mínimo Privilegio

Un sujeto solamente debe tener asignados los privilegios que necesita para completar su tarea asignada.

- Si el sujeto no necesita un permiso, no debería tenerlo
- Los privilegios deberían ser asignados de acuerdo al _rol_ que cumple el sujeto
- Si alguna acción específica requiere elevar el nivel de privilegio que tiene un sujeto, esos derechos deben ser retirados _inmediatamente_ luego de completar esa acción.

Muchos sistemas implementan su sistema de permisos de forma insuficientemente granular: por ejemplo, en UNIX y similares, el usuario _root_ tiene permiso para todo, de manera que el encargado de hacer los _backups_ tiene la posibilidad de borrar archivos de los usuarios. Al mismo tiempo, esto está mitigado por el comando `sudo`.

- Permite ejecutar programas con los privilegios de otro usuario.
- Permite configurar con precisión los usuarios que tienen derecho de hacerlo, y para qué programas.

## Failsafe Defaults
