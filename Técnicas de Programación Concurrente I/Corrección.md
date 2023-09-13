La corrección implica que el programa haga lo que tiene que hacer.

Existen dos tipos de propiedades de la corrección:

- **Safety:** Deben ser verdaderas siempre
- **Liveness:** Deben volverse verdaderas eventualmente.

## Safety

Existen dos principales propiedades del tipo *safety*.

- **Exclusión mutua:** Dos procesos no deben intercalar ciertas secuencias de instrucciones. Por ejemplo: incremento de una variable global.
- **Ausencia de deadlocks:** Un sistema que aún no finalizó debe poder continuar realizando su tarea, es decir, avanzar productivamente.

## Liveness

Existen dos principales propiedades del tipo *liveness*.

- **Ausencia de starvation:** Todo proceso que esté listo para utilizar un recurso debe recibir dicho recurso eventualmente.
- **Fairness:** Equidad o justicia. Un escenario es débilmente justo si en algún estado en el escenario, una instrucción que está continuamente habilitada eventualmente aparece en el escenario.

## Sección Crítica
