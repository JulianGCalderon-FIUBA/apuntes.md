Para poder probar las combinaciones posibles que puede utilizar un gestor, se basaran en las reglas de equivalencia.

- **Selección:**
	- Cascada: $\sigma_{c_1\land c_2 \land \dots \land c_n}(R) = \sigma_{c_1}(\sigma_{c_2}(\dots(\sigma_{c_n}(R))\dots)$
	- Unión: $\sigma_{c_1\lor c_2 \lor \dots \lor c_n}(R) = \sigma_{c_1}(R) \cup \sigma_{c_2}(R) \cup \dots \cup \sigma_{c_n}(R)$
	- Conmutatividad: $\sigma_{c_1}(\sigma_{c_2}(R)) = \sigma_{c_2}(\sigma_{c_1}(R))$
- **Proyección:**
	- Cascada: $\pi_{X_1}(\pi_{X_2}(\dots(\pi_{X_n}(R))\dots)) = \pi_{X_1}(R)$. Siempre y cuando las proyecciones sean subconjuntos de sus proyecciones siguientes.
	- Conmutatividad con $\sigma$: $\pi_X(\sigma_c(R)) = \sigma_c(\pi_X(R))$. Siempre y cuando entre los atributos que proyecto se mantengan los atributos sobre los cuales condiciono.
- **Producto Cartesiano y Junta:**
	- Conmutatividad:
		- $R \times S = S \times R$
		- $R * S = S * R$
	- Asociatividad:
		- $(R \times S) \times T = R \times (S \times T)$
		- $(R * S) * T = R * (S * T)$
- **Operaciones de Conjuntos:**
	- Conmutatividad:
		- $R \cup S = S \cup R$
		- $R \cap S = S \cap R$
	- Asociatividad:
		- $(R \cup S) \cup T = R \cup (S \cup T)$
		- $(R \cap S) \cap T = R \cap (S \cap T)$
- **Mixtas:**
	- Distribución de la selección en la junta: $\sigma_c(R*S) = \sigma_{C_r}(R) * \sigma_{C_s}(S)*$. Solo si $c$ puede escribirse como $c_R \land c_S$. Donde involucran solo y respectivamente atributos de $R$ y $S$.
	- Distribución de la proyección en la junta: $\pi_X(R*S) = \pi_{X_R}(R)*\pi_{X_S}(S)$. Solo si todos los atributos de junta están incluidos en $X$. Entonces llamaremos $X_R, X_S$ a los atributos de $R, S$ respectivamente.

## Heurísticas de Optimización

La aplicación de las reglas de equivalencia a una expresión algebraica para obtener otra de menor costo se conoce como optimización algebraica.

Las siguientes son algunas reglas generales utilizadas para optimizar algebraicamente una consulta:

- Realizar las selecciones lo más temprano posible
- Reemplazar productos cartesianos por juntas siempre que sea posible
- Proyectar para descartar los atributos no utilizados lo antes posible. Entre la selección y la proyección, priorizar la selección.
- En caso de que haya varias juntas, realizar aquella más restrictiva primero. Se puede optar por árboles *left-deep* o *right-deep* para acotar las posibilidades.
