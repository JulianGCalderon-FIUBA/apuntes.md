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

- **Transientes**: ocurren una vez y luego desaparecen; si se repite la operación, el fallo desaparece. Es un ello esporádico.
- **Intermitentes**: Ocurren de forma intermitente; son difíciles de diagnosticar.
- **Permanentes**: Existen hasta que los componentes defectuosos se reemplaza: se rompe el disco.

Es importante entender la diferencia entre fallos **improbables**, y fallos **imposibles**: ¿Es imposible que una lluvia solar altere el estado de un sistema?

Otra forma de clasificar los fallos es:

- **Crash**: se detiene el servicio por completo.
- **Timing**: Se da una respuesta fuera de los tiempos aceptables.
- **Omisión**: El servicio falla al responder solicitudes entrantes.
- **Respuesta**: La respuesta es incorrecta.
- **Bizantina**: Es arbitraria en tiempos y respuesta; la información es diferente para distintos consumidores. A veces lo hace por motivos maliciosos.
