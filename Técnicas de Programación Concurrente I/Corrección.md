En un programa secuencial, la reejecución de un programa garantizará el mismo resultado. Esto no ocurre en un programa concurrente debido al intercalado.

En los programas secuenciales, la definición de *correctness* no tiene sentido. En los programas concurrentes, existen dos tipos de propiedades de *correctness*:

- **Propiedades de Seguridad:** Esta propiedad debe siempre ser cierta.
- **Propiedad de Liveness:** Esta propiedad debe eventualmente ser cierta.

Estas dos propiedades son duales una a la otra, si una falta, la otra también. La definición de estas propiedades depende del dominio y del problema a resolver.

Debido a que se debe demostrar para todos los escenarios, no se puede demostrar esta propiedad a través de las pruebas.

## Safety

Existen dos principales propiedades del tipo *safety*.

- **Exclusión mutua:** Dos procesos no deben intercalar ciertas secuencias de instrucciones. Por ejemplo: incremento de una variable global.
- **Ausencia de deadlocks:** Un sistema que aún no finalizó debe poder continuar realizando su tarea, es decir, avanzar productivamente.

## Liveness

Existen dos principales propiedades del tipo *liveness*.

- **Ausencia de starvation:** Todo proceso que esté listo para utilizar un recurso debe recibir dicho recurso eventualmente.
- **Fairness:** También llamado equidad o justicia. Un escenario es débilmente justo si en algún estado en el escenario, una instrucción que está continuamente habilitada eventualmente aparece en el escenario.
