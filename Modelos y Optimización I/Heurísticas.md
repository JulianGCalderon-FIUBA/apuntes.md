Para resolver modelos de programación lineal entera, tendremos muchos métodos. Los problemas exactos son muy costosos, ya que no se pueden resolver de forma lineal. Debido a esto, existen heurísticas para hallar soluciones aproximadas al modelo.

Las **heurísticas** las utilizaremos cuando no existe un método exacto de resolución o requiere demasiado tiempo o recursos. También la utilizaremos cuando no necesitemos obtener la solución óptima y con una aproximación es suficiente, o cuando tenemos datos poco confiables. En casos, las heurísticas se utilizarán como paso intermedio antes de la aplicación de otro algoritmo.

Los problemas **NP** son aquellos que no pueden resolverse en tiempo polinómico y debido a esto, se suelen usar ***heurísticas*** para resolverlos.

Existen dos tipos de heurísticas. Las heurísticas de **construcción** utilizan un algoritmo para crear una solución inicial. Las heurísticas de **mejora** parten de una solución y buscan mejorarla.

Las heurísticas pueden de construcción tener una **garantía de calidad**. Esto nos garantiza que si yo aplico la heurística, estaré ante un cierto desvió conocido del optimo.

Las **meta-heurísticas** plantearan multiples heurísticas para un mismo problema, para encontrar aquella que de mejores soluciones. Puede agrupar heurísticas y aplicar heurísticas tras otras para encontrar la mejor solución.

## Secuenciación de Tareas

Recordemos que en estos problemas, tendremos un conjuntos de tareas $T_i$. Buscamos obtener el orden de tareas que minimice el costo total. Contamos con restricciones de orden, donde ciertas tareas deben ser completadas antes que otras. Además, tendremos multiples operarios que pueden trabajar a la vez.

Tendremos un conjunto de reglas que utilizaremos para hallar una solución. Un ejemplo de posible heurística, será:

- Si todos los operarios están desocupados, entonces se les asigna tareas en orden.
- Si hay multiples tareas para realizar, se elige la de mayor duración. Otra posibilidad es que se elija la tarea de menor duración.
- Si hay multiples tareas con igual duración, entonces se elige por orden alfabético.
- SI no hay ninguna tarea, se espera a que finalice otro operario (y libere una tarea).

Pueden surgir un gran numero de heurísticas, cada uno siendo efectiva en distintos escenarios.
