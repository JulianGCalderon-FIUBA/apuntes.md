Una barbería tiene una sala de espera con sillas. Si la barbería está vacía, el barbero se pone a dormir.

Si un cliente entra y el barbero está atendiendo, se sienta en una de las sillas y espera su turno. Si está durmiendo, lo despierta.

El cliente espera a que le corten el pelo.

## Solución con Semáforos

Se necesitan tres semáforos, todos inicializados en cero.

- Cola de clientes.
- Barbero listo.
- Corte de pelo listo.

Cuando el barbero comienza, realiza un `wait` del semáforo de cola de clientes.

En el momento que un cliente entra al negocio, realiza un `signal` del mismo semáforo, despertando al barbero. (e indicando que se une a la cola de espera).

Luego, el cliente realiza un `wait` del semáforo de barbero listo (debe esperar a ser atendido).

El barbero, luego de ser despertado, realizará un `signal` del semáforo de barbero listo, indicando que va a atender al próximo cliente.

El cliente despierta para ser atendido, y realiza un `wait` del semáforo de corte de pelo listo.

Una vez el barbero finaliza el corte del pelo, realiza un `signal` en el semáforo del corte de pelo listo, liberando el cliente.

Luego, el barbero realiza un `wait` del semáforo de cola de clientes. Si hay clientes en la cola continuará su ejecución con un `signal`  del semáforo que indica que está listo para atender. De no ser el caso, 
