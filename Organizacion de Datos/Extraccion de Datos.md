---
title: Extraccion de Datos
---

El objetivo de la extracción de información es capturar ciertas partes relevantes de un texto. Muchas veces en el contexto de varios documentos. Luego, generar una representación estructurada y limpia de la información.

- **Open Information Extraction**: Métodos no supervisados, independientes del dominio, que trabajan con grandes volúmenes de datos.

## NER: Reconocimiento de nombres de entidades

Es lo primero que se hace cuando analizamos un texto. Consiste en reconocer todas aquellas entidades que puedan tener un nombre.

Para cada entidad, debemos identificar que tipo de identidad es.

1. Tokenizar la información
2. Etiquetar cada token con la clase a la que corresponda: *IO/IOB - encoding*
3. Especificar características de extracción que se adecuen a las clases y el texto que tenemos:
	1. Basado en palabras: Actual, Adyacente, Substring de palabra, Su forma
	2. Basado en otras inferencias: Reglas gramaticales
	3. Basado en contexto: Etiquetas anteriores y siguientes
4. Entrenar un clasificador secuencial para predecir las etiquetas del conjunto de pruebas

### Ontología

Es una forma de representar el conocimiento. Una forma de representarlo es a través de dos relaciones:

- **Hipónimo (Is-a):** Recurro jerárquicamente a la categoría que lo contiene
- **Instance-of:** De qué clase es instancia cierto token, OOP.

Esta ontología se puede generar automáticamente:

### Reglas escritas a mano, del tipo pattern-matching:

- Alta precisión
- Adaptado a dominios específicos
- Bajo *Recall*
- Implica mucho trabajo

### Aprendizaje automático supervisado

- Debemos decidir que relaciones nos interesa extraer
- Debemos decidir que tipos de entidades son pertinentes a estas relaciones
- Necesitamos un conjunto de datos etiquetado, sus entidades y sus relaciones
- Para cada par de entidades, hacer un *bag word* con sus palabras intermedias.

### Auto-Supervisado

- **BOOTSTRAP:** Encuentra relaciones a partir de semillas.
	1. Para un par de entidades semilla, buscar coincidencias
	2. Extraer el contexto de la oración, reemplazar entidades por comodines
	3. Realizar búsquedas con esos patrones para encontrar nuevas entidades y repetir
- **DISTANT SUPERVISION:** Combina *bootstrapping* con aprendizaje supervisado. En lugar de usar pocas semillas, se utiliza un gran volumen de datos.
	1. Para cada relación
	2. Para cada tupla de entidades
	3. Encuentra sentencias en un corpus donde aparecen esas entidades
	4. Extraer las características frecuentes (patrones)
	5. Entrenar un clasificador, utilizando esos patrones

### No supervisado para la web.

- **KnowItAll:** No Supervisado; Independiente del Dominio; Escalable
- **TEXTRUNNER:** Primer algoritmo que podríamos definir de Open Information Extraction
	1. Realiza una sola pasada sobre el conjunto de datos
	2. Extraer relaciones semánticas no definidas a priori

Hay muchas mejoras a estos métodos

![[Extraccion de Datos 1.png|500]]
