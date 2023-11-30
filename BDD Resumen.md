## Cálculo Relacional

La lógica de predicados de primer orden se basa en tres componentes:

- **Predicados:** Son funciones de una o más variables cuyo resultado es un valor de verdad (verdadero o falso).
- **Operaciones** entre predicados: $\land$, $\lor$, $\neg$.
- **Cuantificadores** de variables: Existen dos cuantificadores:
	- Cuantificador universal: $(\forall m)q(m)$.
	- Cuantificador existencial: $(\exists m)q(m)$.

Para restringir el dominio de la variable en un cuantificador universal, tenemos que usar la negación. En caso contrario, el resultado siempre será falso.

$$
(\forall m)(m \notin \text{Dominio} \lor \Phi(m))
$$

De forma equivalente, podemos usar el cuantificador existencial negado

$$
(\nexists m)(m \in \text{Dominio} \land \neg\Phi(m))
$$
