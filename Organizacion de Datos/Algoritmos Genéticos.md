Para modelar estos algoritmos, se plantearon las siguientes definiciones:

- **Fenotipo:** Problema a solucionar
- **Cromosoma:** Cada una de sus posibles soluciones
- **Gen:** Cada uno de los símbolos en el cromosoma
- **Genotipo:** Si los símbolos son binarios
- **Generación:** Cada iteración.

## Operaciones

Con estos cromosomas, podemos aplicar ciertas operaciones:

- ***Cruza:*** Combinamos distintos cromosomas para generar uno nuevo
- ***Mutación:*** Modificamos algunos símbolos del cromosoma
- ***Selección:*** Probamos el cromosoma para obtener un puntaje, obtenemos el que tiene un mejor puntaje.

En un algoritmo genético, tendremos las distintas variables:

- **Tamaño de la población:** Si es muy excesiva el algoritmo puede volverse lento, pero si es escasa entonces la solución puede ser poco óptima
- **Probabilidad de Cruce:** de 0 a 100%
- **Probabilidad de Mutación:** de 0 a 100%

## Codificación

Existen distintos tipos de codificaciones

- Codificación binaria: Problema de la mochila (los genes son valores binarios)
- Codificación por valor directo: Problema del viajante (los genes contienen el valor directo)
- Codificación en Árbol: El cromosoma se modela como un árbol y la cruza es a nivel de nodos

## Selección

Existen distintos tipos de métodos de selección:

- **Por Ruleta:** A cada cromosoma se le asigna una probabilidad en base a su puntaje
- ***Selección Elitista:*** Además del método anterior, se seleccionan manualmente las mejores muestras
- ***Otras Selecciones:*** Jerárquica, por torneo, escalada, etc.

## Cruza

Existen distintos métodos para la cruza:

- ***Crossover 1 punto:*** Dividimos un cromosoma en dos, e intercambiamos cada mitad con otro cromosoma

	![[Algoritmos Genéticos 1.png]]

- ***Crossover 2 puntos:*** Dividimos el cromosoma en 3

	![[Algoritmos Genéticos 2.png]]

- **Crossover Aritmético:** Se aplica alguna operación sobre los cromosomas, como por ejemplo el operador AND

![[Algoritmos Genéticos 3.png]]

## Mutación

La mutación no se debe abusar, debe realizarse con probabilidad muy baja. Consiste en cambiar aleatoriamente un gen.

Hay distintas alternativas, se pueden intercambiar valores o alterar sus valores de forma directa.
