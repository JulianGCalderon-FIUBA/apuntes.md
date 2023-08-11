## Definiciones Importantes

**Calidad (ISO)**: La totalidad de prestaciones y características de un producto o servicio que generan su capacidad de satisfacer necesidades explícitas o implícitas

***Verificación:*** Es un conjunto de actividades que compara un producto del ciclo de vida con las características exigidas para ese producto. El sistema ha sido construido correctamente

***Validación:*** Conjunto de actividades que permiten garantizar que un sistema es capaz de cumplir con su uso previsto, metas y objetivos. Se ha construido el sistema correcto.

La verificación y validación pueden tener lugar en cualquier momento del ciclo de vida del producto.

***Control de Calidad:*** Apunta más a la evaluación operativa para determinar si lo que hemos producido cumple con los requerimientos de calidad. (verificación y validación caen en esta categoría)

***Aseguramiento de Calidad:*** No tiene nada que ver con las pruebas, apunta a evaluar si los productos y mis procesos se adhieren a los estándares aplicables. Es importante marcar la diferencia, ya que mucha gente usa los términos indistintamente.

## Técnicas de verificación y validación

Para cada elemento, tendremos técnicas para su correcta verificación y validación:

![[Verificar y Validar requerimientos 1.png|500]]

La prueba de aceptación es una técnica de validación, mientras que las otras técnicas son de verificación.

## Actividades de Control de Calidad

Tendremos actividades dinámicas y estáticas. Las actividades dinámicas están relacionadas con las pruebas del ***software***.

![[Verificar y Validar requerimientos 2.png|500]]

Las revisiones por pares es una familia que incluye múltiples técnicas, según la estructura y la cantidad de integrantes

![[Verificar y Validar requerimientos 3.png|500]]

Las revisiones de a pares es un tipo de revisión en el cual y un artefacto es examinado por pares (lideradas por el autor) con el propósito de encontrar defectos. No hay específicamente una técnica que se llame "revisión de pares", sino que existen varias y cada una tiene características particulares y distintivas.

### Revisiones (Walkthrough)

Son revisiones de a pares, es un enfoque menos formal que otros. Usualmente, son lideradas por el autor. No siempre es necesaria la preparación previa, ni hay límites a la cantidad de material revisado ni a la duración de la reunión.

Se sugiere una hora de duración y una hora de preparación. Se permite la discusión de sugerencias. Usualmente, el presentador es el autor, pero participa un secretario y varios revisores. Como regla general, el management no debe estar presente. En el ámbito de la ingeniería de requerimientos se pueden emplear para la validación.

### Inspecciones

Son mucho más formales, hay roles, pasos, etapas, artefactos detallados. Tiene como objetivo encontrar defectos: cualquier falla o imperfección en un producto o proceso. Esta técnica le llevo a la ingeniería de software 30 años en terminar de adoptar.

#### Etapas

1. Planificación: Dado un artefacto a inspeccionar, se asigna un moderador, quien decidirá quién participara, donde, cuando, y distribuirá la documentación necesaria.
2. Presentación: Se realiza una Reunión corta en la que se presenta a los inspectores el material a revisar (opcional)
3. Preparación: Los inspectores trabajan solos durante una hora y media, familiarizándose con el material y tratando de detectar potenciales defectos.
4. Reunión de la inspección: Los inspectores presentan los supuestos defectos. El moderador confecciona una lista de defectos unificada. No está permitida la discusión en torno de la autenticidad de los defectos, ni de las posibles soluciones.
5. "Tercer Tiempo": Los inspectores discuten con el autor posibles mejoras a los defectos encontrados (opcional)
6. Retrabajo: El autor resuelve los defectos encontrados. Luego de esta etapa, se puede volver a la etapa de planificación.
7. Seguimiento: El moderador verifica que se haya realizado el trabajo.

![[Verificar y Validar requerimientos 4.png|175]]

Algunas personas proponen que los autores no deberían participar en la inspección, para evitar posibles rencores generados.

#### Estándares

Para el correcto funcionamiento, se deben definir estándares:

- Estándares para los defectos
- Lista de chequeos para facilitar encontrar defectos

#### Reglas

Las reglas de las inspecciones son:

- El objetivo es encontrar defectos
- Se inspeccionan productos, no se evalúa a los productores
- El equipo debe estar formado por entre tres y seis personas que deben ser pares del autor
- Las reuniones no deben durar más de dos horas (esto limitará la cantidad de material a revisar)
- Hay distintos roles: Moderador, presentador, secretario.

#### Beneficios

Los beneficios de la técnica son:

- Pueden identificar tempranamente hasta un 80% de los defectos
- EN combinación con testing, se reduce la cantidad de defectos en software liberados en un factor de 10
- Permiten un incremento del 25-30% de productividad
- Requieren una inversión de alrededor del 15& del costo total.
- En el ámbito de la ingeniería de requisitos, se pueden emplear para la validación (aunque son orientadas a la verificación)

### Prototipos

Pueden emplearse en la validación con los usuarios, con la salvedad que deben comprender que el diseño no es final y hay que concentrarse en los detalles funcionales.
