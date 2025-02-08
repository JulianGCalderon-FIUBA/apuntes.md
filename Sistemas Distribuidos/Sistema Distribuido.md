En un sistema distribuido, los componentes están conectados y realizan trabajo colaborativo buscando un objetivo común.

Escalan distribuyendo trabajo y recursos.

- **Disponibilidad**: aún frente a fallos aislados, el sistema general puede prestar servicios.
- **Escalabilidad**: poseen mejores alternativas de adaptarse a nuevas escalas
- **Reducción de Latencia**: al favorecer principios de localidad de recursos.
- **Colaboración**: permite interacciones entre sistemas de forma orgánica y natural.
- **Movilidad**: no están circunscritos al alcance de un único computador.
- **Costo**: los componentes más simples, puede contener subsistemas delegados en servicios terceros

## Ley de Conway

> "Cualquier organización que diseñe un sistema, inevitablemente producirá un diseño cuya estructura será una copia de la estructura de comunicación de la organización" (Conway M., How do committees invent, Datamation, 1968).

Este enunciado fue demostrado empíricamente en distintos relevamientos de arquitecturas de software corporativo. Es decir, se probó que diseñamos de acuerdo a lo que conocemos y estamos acostumbrados a hacer en el día a día.

No es necesariamente negativo: en su trabajo, el hombre tiende a encontrar soluciones distribuidas y paralelas eficientes (minimizan costo, energía, tiempo, etc.).

## Centralización

Por otro lado, un sistema **centralizado** tiene las siguientes ventajas:

- **Control**: lógica de control muy simple, efectiva y, en ocasiones, eficiente.
- **Homogeneidad**: la centralización fuerza estándares para software y hardware.
- **Consistencia**: es posible definir fuertes políticas de consistencia de información y monitoreo del estado global del sistema.
- **Seguridad**: se disminuye la 'superficie de ataque' frente a amenazas.

## Descentralizar vs. Distribuir

Existen tres conceptos que están relacionados entre sí:

- **Centralizar** implica la concentración de la autoridad en los niveles más altos de una jerarquía.
- **Descentralizar** implica transferir la toma de decisiones a eslabones inferiores de cierta organización.
- **Distribuir** implica utilizar un modelo descentralizado de control de computadoras para la coordinación de actividades con una coherencia dada.

## Arquitecturas

Hay dos arquitecturas principales de un sistema distribuido

- [[Cliente-Servidor]]
- [[Peer-to-Peer]]
