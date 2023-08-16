---
title: Gradient Boost
---

Este método no solo sirve para clasificación, sino para regresión

1. Crea una cadena de árboles de profundidad fija.
2. Comienza con un solo valor, un nodo hoja.
3. Crea un árbol para tratar de predecir el error cometido (pseudo-residuo) para cada observación por el árbol anterior.
4. Ahora, la predicción será el valor original + la predicción del error del segundo árbol.
5. Este algoritmo se repite hasta que los residuos no cambien significativamente, o se alcance un límite de arboles.

El **bias** de este modelo es muy bajo, aunque la **variance** es muy alto.

Para esto, cada árbol está ponderado por un factor constante llamado *learning rate.* El cual ayuda a reducir la varianza.

![[Gradient Boost 1.png]]
