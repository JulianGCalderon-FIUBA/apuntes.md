---
title: Descomposición de Cholesky
---

La descomposición de Cholesky es un tipo de descomposición para cuando $A$ es simétrica y definida positiva, tomamos $U = L^T$. Este algoritmo es estable y tiene un costo operacional de $O(\frac{n^2}2)$. Además, no requiere comprobar si la matriz es definida positiva, ya que la aplicación del método lo deduce.

Para hallar los coeficientes, utilizamos las siguientes ecuaciones

$$
l_{ki} = \frac{a_{ki} - \sum_{j=1}^{i-1} l_{ij}l_{kj}}{l_{ii}} \quad k=i{+}1, \cdots, n
$$

$$
l_{kk} = \sqrt{a_{kk} - \sum_{j=1}^{k-1} l_{kj}^2} \quad k=1, \cdots, n
$$
