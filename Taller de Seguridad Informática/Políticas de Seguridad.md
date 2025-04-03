> Una política de seguridad divide los estados del sistema en "seguros" e "inseguros".

Esto implica que la seguridad del sistema es capturada por una serie de reglas explícitas. Hay que poner cuidado en que las políticas sean correctas.

> Los mecanismos de seguridad pueden evitar que el sistema pase de un estado "seguro" a uno "inseguro"

Si definimos:

- $P$: Conjunto de estados posibles del sistema
- $Q$: Conjunto de estados seguros según la política del sistema
- $R$: Conjunto de estados permitidos por un mecanismo

Entonces:

- $Q \subseteq R$: El mecanismo es amplio (broad).
- $Q = R$: El mecanismo es preciso (precise).
- $Q \supseteq R$: El mecanismo es seguro (secure).

La unión de todos los mecanismos de seguridad de un sistema idealmente debería resultar en un mecanismo preciso.

En la práctica, los mecanismos son amplios (permiten alcanzar estados inseguros). Confiar en que los mecanismos funcionan requiere varios supuestos:

1. Cada mecanismo está diseñado para implementar una o más partes de la política de seguridad.
2. La unión de los mecanismos implementa todos los aspectos de la política de seguridad.
3. Los mecanismos están correctamente implementados.
4. Los mecanismos están correctamente instalados y administrados
