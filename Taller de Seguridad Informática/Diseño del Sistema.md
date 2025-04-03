Una especificación es una enunciación (formal o informal) del funcionamiento deseado del sistema. Los requerimientos pueden ser funcionales, o de seguridad.

El diseño de un sistema traduce las especificaciones del mismo en una serie de componentes que las implementan.

Se dice que el diseño satisface las especificaciones si, bajo todas las circunstancias relevantes, el diseño no permite que el sistema viole las especificaciones.

Según los términos en que se expresen, verificar que un diseño satisface una especificación puede ser una tarea ardua. Si están expresados en términos matemáticos, se pueden utilizar métodos formales (que hay que asistir en algún momento), y si están en lenguaje natural, hay que buscar una explicación satisfactoria (de por qué sí o por qué no satisface los requerimientos).

Dado un diseño, la implementación crea un sistema que satisface ese diseño. Si el diseño satisface las especificaciones, por transitividad la implementación satisfará las especificaciones.

- Se dice que un programa es _correcto_ si satisface las especificaciones
- Verificar que el programa es correcto es mucho más arduo que verificar un diseño.

En una verificación formal, cada instrucción es una operación matemática. Es posible, en teoría, en la práctica solamente se usa para cosas pequeñas y críticas. El lenguaje en que se escribe no es el lenguaje que se ejecuta.

## Principios de Diseño

Al ahora de realizar el diseño del sistema, se emplean distintos principios:

- [[Principio de Sujetos y Objetos]]
- [[Principio del Mínimo Privilegio]]
- [[Principio de Failsafe Defaults]]
- [[Principio de Economía de Mecanismo]]
- [[Principio de Mediación Completa]]
- [[Principio de Diseño Abierto]]
- [[Principio de Separación de Privilegios]]
