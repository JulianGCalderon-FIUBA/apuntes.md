---
title: Programación Lineal Continua
---

En la programación lineal continua, las variables de decisión serán variables continuas, y el objetivo y las restricciones serán lineales.

Este tipo de modelos no admiten relaciones de menor o mayor estricto, únicamente admiten los símbolos: $\leq, \geq, =$

## Resolución

Debido a que nuestro objetivo será lineal, tendrá una dirección constante de crecimiento. Para variables continuas, la solución óptima (aquella que maximiza el funcional) se encontrara en uno de los vértices del poliedro (o en un borde, en caso de que haya infinitas soluciones)

El poliedro se construye encontrando la región del espacio que cumple con todas las restricciones planteadas en el modelo.

## Variables Slack

Para convertir todas las restricciones a igualdades, se utilizan las variables *slack*. Aquellas variables slack que tomen el valor cero en la solución indican que esta restricción es limitante (si este es un recurso, entonces está agotado)

$$
g(x) \leq x \iff g(x) + S = x, S\geq 0
$$

$$
g(x) \geq x \iff g(x) - S = x, S\geq 0
$$

## Solución Óptima

Cuando se resuelve un modelo, se pueden presentar uno de los siguientes casos:

- **Solución única**: El modelo tiene una única solución óptima, mejor que las otras.
- **Solución indeterminada**: El modelo tiene infinitas soluciones, la traza de la función objetivo coincidirá con un lado del poliedro óptimo
- **Solución incompatible:** El modelo no tiene ninguna solución (no existe región de soluciones factibles)
- **No acotado:** Hay puntos con valor del funcional arbitrariamente grandes en la región factible

Para un modelo compatible, se puede dar que un punto óptimo se encuentre en la intersección de múltiples intersecciones. Estos se llaman **puntos degenerados.**

## Supuestos Básicos de la P.L. Continua

Para los problemas de este tipo, se deben definir los siguientes supuestos básicos:

- **Certeza**: Todos los parámetros del modelo son constantes conocidas. Para poder plantear el modelo dentro de la optimización determinística, se debe cumplir este principio.
- **Proporcionalidad:** Tanto el beneficio como el uso de recursos son directamente proporcionales al nivel de actividad.
- **Aditividad:** No existen interacciones entre las actividades que cambien la medida total de la efectividad o el uso total de algún recurso. No en todo los dominios se cumple esta propiedad. Por ejemplo, en el caso de la química, las interacciones no suelen ser lineales.
- **Divisibilidad:** Las unidades de actividad pueden dividirse en niveles fraccionarios cualesquiera, de modo que pueden permitirse valores no enteros para las variables. Si este supuesto no se cumple, tendremos que trabajar con variables enteras.

### Variables Enteras

Desde el punto de vista del planteo no hay inconveniente, pero al únicamente admitir variables continuos, entonces la solución óptima ya no siempre se encontrará en uno de los vértices del poliedro. Una posible solución a este problema es agregar restricciones al poliedro para lograr que la solución óptima se encuentre en los vértices.

## Esquema Modular

### Definiciones

Un **módulo** es un conjunto de vinculaciones que poseen una misma naturaleza funcional. Por naturaleza funcional entendemos que el conjunto de vínculos representan una misma función.

La **modularidad** es la interdependencia entre los módulos.

Una **estructura** es un conjunto de módulos vinculados entre sí que cumplen la condición de modularidad. Un modelo podría plantearse como una estructura.

### ¿Cómo se plantea?

Lo que está dentro de un módulo tiene que estar vinculado por una función común y el pasaje de variables entre módulos debe ser mínimo. Debemos respetar la heurística de la alta cohesión (todo lo que pertenece a un módulo responde a la misma función) y bajo acoplamiento (los módulos son independientes entre sí).
