La tolerancia a fallos estudia las necesidades de los sistemas confiables (*dependable systems*):

- Busca garantizar que se ejecuten y comporten de acuerdo a lo esperado por el usuario en distintas condiciones.
- Busca prevenir la aparición de fallas de cara al usuario, tanto normales como excepcionales.
- Hay distintas alternativas para prevenir o tolerar cada situación.

La idea es que el sistema nunca salga de estados definidos.

Se permite definir la inversión y el nivel de tolerancia para cada tipo de sistema.

Algunas herramientas para lograr esto son:

- Recuperación.
- Redundancia (ej. replicación).
- Consenso (ej. esquema de votación)

> En presencia de fallos, el sistema distribuidos continúa operando de forma aceptable

## Generación de Fallos

Un **fallo** o *fault* causa la ocurrencia de un estado de **error** en el sistema. Esto eventualmente desencadena en un comportamiento incorrecto: falla o **avería** (*failure*). Se busca que todos los fallos (o errores) se encapsulen y que nunca se llegue a una avería.

Un fallo parcial ocurre cuando un componente de un sistema distribuido incurre en error. Es una característica distintiva de los sistemas distribuidos, y puede generar una reacción encadena que afecta al comportamiento del sistema completo.

Por ejemplo:

- Un rayo cósmico cambia el estado de un bit en memoria: esto es un **fallo**.
- Esto causa que un puntero apunte a una dirección inválida: hay un **error** en el estado del sistema.
- Eventualmente, el programa accede a esta dirección de memoria inválida y morirá: esto es una falla o una **avería**.

Otro ejemplo:

- Un programa `Y` no puede comunicarse con el programa `X` debido a un fallo en la comunicación.
- El programa `Y` hace un *polling* infinito con un timeout pequeño a programa `X`, dejando conexiones abiertas.
- El programa `Y` llega al límite de conexiones abiertas, y muere.

## Clasificación de Fallos

Los fallos se clasifican en:

- Transientes: ocurren una vez y luego despa
