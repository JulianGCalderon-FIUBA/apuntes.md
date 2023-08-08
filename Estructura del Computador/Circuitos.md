Dada una expresión algebraica, buscamos simplificar para que el costo de representarla en la realidad sea lo más simple. Cuanto más simple es la expresión, necesitaremos menos compuertas y menos entradas por compuerta

## Compuertas

![[Circuitos 1.png|Untitled]]

# Diseño de Circuitos

El diseño de circuitos consiste en definir una tabla de verdad y luego representar el circuito con compuertas.

1. Expresión Informal
2. Expresión Formal
3. Expresión Mínima
4. Circuito
5. Implementación

## Lógica Combinacional

Puedo clasificar mis circuitos según la cantidad de niveles:

- **Lógica de Dos Niveles:** La suma de minitérminos o el producto de maxitérminos representan la lógica dos niveles
- **Lógica Multinivel:** Son mas costosos ya que tienen mas compuertas y de distintos tipos, generará un tiempo de respuesta mayor.

## Complejidad de Un circuito

Podemos medir la complejidad de un circuito de la siguiente manera

$$
\text{Complejidad} = \sum\text{Tc}\cdot \text{Ce}
$$

Siendo $\text{Tc}$ el tipo de compuerta y $\text{Ce}$ la cantidad de entradas de esa compuerta