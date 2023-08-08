# Columna

Se define $\text{Col}(A)$, al subespacio formado por combinación lineal de las columnas de $A$

**Propiedades:**

- El sistema $Ax = b$ tiene solución si $b \in \text{Col}(A)$. Si es solución única, entonces el conjunto de columnas es linealmente independiente.
- Se puede demostrar que $\text{Dim}(\text{Col}(A)) = \text{Dim}(\text{Fil}(A)) = \text{Rg}(A)$

# Fila

Se define $\text{Fil}(A)$, al subespacio formado por combinación lineal de las filas de $A$

**Propiedades:**

- El sistema $A^tx = b$ tiene solución si $b \in \text{Fil}(A)$. Si es solución única, entonces el conjunto de filas es linealmente independiente.
- Se puede demostrar que $\text{Dim}(\text{Col}(A)) = \text{Dim}(\text{Fil}(A)) = \text{Rg}(A)$

# Núcleo

Se define el núcleo de un sistema lineal como el subespacio de combinaciones lineales nulas del mismo

$$
\text{Nul}(A) = \{x \in \Bbb K^n/Ax = 0\}
$$

$$
\text{Nul}(A^T) = \{x \in \Bbb K^n/A^Tx = 0\}
$$

Si la dimension del núcleo es mayor a 0, entonces el sistema no es linealmente independiente.

**Propiedades:**

- $\text{Rg}(A) + \text{Dim}(\text{Nul}(A)) = n$
- Si $\text{Nul}(B) \subseteq \text{Nul}(AB)$ y $\text{Col}(B) \cap \text{Nul}(A) = \{{0_{\Bbb K^n}}\}$, entonces $\text{Nul}(B) = \text{Nul}(AB)$
- Si $\text{Col}(AB) \subseteq \text{Col}(A)$  y $\text{Rg}(B) = n$, entonces $\text{Col}(AB) = \text{Col}(A)$