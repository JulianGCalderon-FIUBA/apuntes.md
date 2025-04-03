Hay distintas metas de los mecanismos de seguridad

- Prevención: Evitar que un ataque sea exitoso.
  - Mecanismos que el usuario no puede inhabilitar ni modificar.
- Detección: Avisar si un ataque tuvo o está teniendo lugar.
  - Asume que la prevención puede fallar.
  - Permite responder ante un ataque o compromiso.
- Recuperación: Detener un ataque y evaluar/reparar el daño.
  - Backups.
  - Business Continuity Plan.
  - Recuperación de contraseñas.

## Autenticación

La autenticación puede basarse en distintos elementos:

- Algo que el usuario sabe (una contraseña).
- Algo que el usuario tiene (un token de seguridad).
- Algo que el usuario es (mecanismos biométricos).

Pueden usarse múltiples factores de autenticación para incrementar el nivel de confianza en la correcta identificación del usuario.

## Autorización

Mecanismo por el cual el sistema determina si el usuario tiene derecho o no a realizar una determinada acción sobre un recurso determinado.

- Discrecional: Es controlado por el usuario, como una lista de control de acceso (ACL). El usuario puede prestarle ese acceso a otro usuario.
- Basado en roles: Es determinado por el rol del usuario, como administrador.
- Basado en anillos: A nivel del procesador. El kernel puede ejecutar instrucciones que un proceso de usuario no.

## Cifrado

El cifrado se utiliza para preservar la confidencialidad y la integridad de los datos

- Puede ser de clave simétrica o asimétrica
- Resultados probados de aritmética modular

Es muy de tener problemas de canales laterales, por eso no se recomienda programar uno mismo sus bibliotecas de criptografía salvo especialización. También es fácil utilizarlas incorrectamente, por lo que hay estudiar igual.

Para más información, ver: [cryptopals](https://cryptopals.com)

## Análisis de Riesgo

Se evalúa dinámicamente si el comportamiento del usuario sigue los patrones usuales, y se solicitan autenticaciones adicionales, se cierra la sesión, y/o se advierte a un administrador, si se estima que hay riesgo.

- Conexiones desde zonas/dispositivos nuevos.
- Conexiones simultáneas desde zonas distintas.
- Creación de un destinatario nuevo y transferencia de mucho dinero.
