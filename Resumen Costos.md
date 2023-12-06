## Selección

### Estimación de costos

- **Búsqueda lineal:** $\text{cost}(\sigma) = B(R)$
- **Índice primario:** $\text{cost}(\sigma) = \text{Height}(I(A_i, R)) + 1$
- **Índice de ordenamiento:** $\text{cost}(\sigma) \approx \text{Height}(I(A_i, R)) + \Big\lceil\frac{B(R)}{V(A_i, R)}\Big\rceil$
- **Índice secundario:** $\text{cost}(\sigma) \approx \text{Height}(I(A_i, R)) + \Big\lceil\frac{n(R)}{V(A_i, R)}\Big\rceil$

### Estimación de cardinalidad

- **Estimación de cantidad de tuplas:** $n(\sigma_{A_i=c}(R)) = \frac{n(R)}{V(A_i, R)}$
- **Estimación de cantidad de bloques** $B(\sigma_{A_i=c}(R)) = \frac{B(R)}{V(A_i, R)}$

## Proyección

### Estimación de costos

Llamaremos $\hat\pi_X(R)$ a la proyección de multiconjuntos.

- **Con superclave:** $cost(\pi) = B(R)$
- **Sin superclave:**
	- **Sort:** $\text{cost}(\pi) = \text{cost}(\text{ord}_M(R)) = 2B(R) \cdot [\log_{M-1}(B(R))] - B(R)$
	- **Hashing:** $\text{cost}(\pi) = B(R) + 2\cdot B(\hat\pi_X(R))$

### Estimación de cardinalidad

Si no elimina duplicados, entonces:

$$
B(\pi_{\text{DNI}}(\text{Persona})) = \frac{\text{\#Tuplas} \cdot \text{size}(\text{DNI})}{\text{size}(\text{bloque})}
$$

## Unión e Intersección

### Estimación de costos

$$
\text{cost}(\cup | \cap) = \text{cost}(\text{ord}_M(R)) + \text{cost}(\text{ord}_M(S)) + 2B(R) + 2B(S)
$$

## Junta

### Loops anidados por bloque

- **Peor caso:** $B(R) + B(R)\cdot B(S)$
- **Mejor caso:** $B(R) + B(S)$
- **Caso general:** $B(R) + \lceil B(R)/(M-2)\rceil \cdot B(S)$

### Método de único loop con índice

El costo va a depender del índice que tengamos disponible:

$$
\text{cost}(R*S) = B(S) + n(S)\cdot\text{cost}(\sigma_{cond})
$$

### Método de sort-merge

$$

\text{cost}(R*S) = B(R) + B(S) + 2B(R) \cdot \lceil\log_{M-1}(B(R))\rceil + 2B(S) \cdot \lceil\log_{M-1}(B(S))\rceil

$$

### Método de junta hash GRACE

$$

\text{cost}(R*S) = 3 \cdot (B(R) + B(S))

$$

Hay que elegir cantidad de particiones, tal que:

- Un bloque por particion, y uno para el desfile: $k < M$
- Particion completa en memoria, y uno para el desfile: $k \geq B(n)/(M-1)$

### Estimación de Cardinalidad

La cantidad de tuplas se estima como:

$$
n(R*S) = \text{js} \cdot n(R) \cdot n(S) = \frac{n(R) \cdot n(S)}{\max{(V(B,R), V(B, S))}}
$$

El factor del bloque como:

$$
F(R*S) = \Big(\frac{1}{F(R)} + \frac{1}{F(S)}\Big)^{-1}
$$
