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
- **Fairness:** También llamado equidad o justicia. Un escenario es débilmente justo si en algún estado en el escenario, una instrucción que está continuamente habilitada eventualmente aparece en el escenario.

## Sección Crítica

La sección crítica se modeliza planteando un problema genérico, el cual luego se puede utilizar para analizar cualquier programa concurrente.

Cada proceso se ejecuta en un bucle infinito cuyo código puede dividirse en parte crítica y parte no crítico.

Especificamos las propiedades de corrección para este escenario:

- Exclusión mutua: No deben intercalarse instrucciones en la sección crítica
- Ausencia de deadlock: Si dos procesos están tratando de entrar a la sección crítica, eventualmente alguno de ellos debe tener éxito.
- Ausencia de starvation: Si un proceso trata de entrar a la sección crítica, eventualmente debe tener éxito.
- La sección crítica debe progresar (finalizar eventualmente)
- La sección no-crítica no requiere progreso (puede terminar o entrar en un loop infinito).

