Una barbería tiene una sala de espera con sillas. Si la barbería está vacía, el barbero se pone a dormir.

Si un cliente entra y el barbero está atendiendo, se sienta en una de las sillas y espera su turno. Si está durmiendo, lo despierta.

El cliente espera a que le corten el pelo.

## Solución con Semáforos

Se necesitan tres semáforos, todos inicializados en cero.

- Cola de clientes.
- Barbero listo.
- Corte de pelo listo.

Cuando el barbero comienza, realiza un `wait` del semáforo de cola de clientes. En el momento que un cliente entra al negocio, realiza un `signal` del mismo semáforo, despertando al barbero.
