Sean $\Bbb V$ y $\Bbb W$ dos $\Bbb K$ espacios vectoriales, se dice que una función $T: \Bbb V \to \Bbb W$ es una transformación lineal, si cumple:

- $T(u_1 + u_2) = T(u_1) + T(u_2),\quad \forall u_1,u_2 \in \Bbb V$
- $T(\lambda u) = \lambda T(u),\quad \forall u \in \Bbb V \text{ y }\lambda \in \Bbb K$

Para verificar que una función es una transformación lineal, entonces tengo que demostrar las dos propiedades anteriores para todo vector de $\Bbb V$.

## Conjuntos de T.L.

- Se dice que $\Bbb V$ es el **dominio** de $T$ y $\Bbb W$ es el **codominio** de $T$
- Se le llama **imagen** de $T$ al conjunto:

	$$
    Im(T) = \{w \in \Bbb W:T(v) = w, v\in\Bbb V\}
    $$

- Si $S$ es un subespacio de $\Bbb V$, se llama **imagen** de $S$ por $T$, al conjunto:

	$$
    T(S) = \{w \in \Bbb W:T(v) = w, v\in S\}
    $$

- Si $U$ es un subespacio de $\Bbb W$, se llama **preimagen** de $U$ por $T$, al conjunto:

	$$
    T^{-1}(U) = \{x \in \Bbb V: T(x) \in U\}
    $$

- Se le llama **núcleo** de $T$ al conjunto:

	$$
    Nu(T) = \{x\in\Bbb V: T(x) = 0_{\Bbb W}\} = T^{-1}(0_{\Bbb W})
    $$

## Propiedades

Sea $T: \Bbb V \to \Bbb W$ una transformación lineal, siendo $\Bbb V$ y $\Bbb W$, espacios vectoriales:

- $T: \Bbb V \to \Bbb W \implies T(0_{\Bbb V}) = 0_{\Bbb W}$
- Sea $\Bbb V = gen(v_1, v_2, \cdots, v_n)$, entonces $Im(T) = gen(T(v_1), T(v_2), \cdots, T(v_m))$
- Si $S \subset \Bbb V$, entonces $T(S) \subset \Bbb W$
- Si $U \subset \Bbb W$, entonces $T^{-1}(U) \subset \Bbb V$
- Toda T.L. queda unívocamente determinada sobre una base.

> [!theorem] Dimensión de subespacios fundamentales es una transformación lineal
> 
> Si $\Bbb V$ es un espacio vectorial de dimensión finita y $T: \Bbb V \to \Bbb W$, entonces:
> 
> $$
> \text{dim}(Nu(T)) + \text{dim}(Im(T)) = \text{dim}(\Bbb V)
> $$

## Clasificación

Sea $T: \Bbb V \to \Bbb W$ una transformación lineal, siendo $\Bbb V$ y $\Bbb W$, $\Bbb K$-espacios vectoriales:

- **Monomorfismo**: Si es una transformación lineal **inyectiva** $:x_1 \neq x_2, F(x_1) \neq F(x_2)$
- **Epimorfismo**: Si es una transformación lineal **sobreyectiva** $: Im(F) = Cod(F) = \Bbb W$
- **Isomorfismo:** Sí es una transformación lineal **biyectiva** (inyectiva y sobreyectiva)

Una transformación lineal es un **monomorfismo** cuando su núcleo es de dimensión 0. Es decir, solo hay una forma de generar cada elemento.

Una transformación lineal es un **epimorfismo** cuando la dimensión de la imagen es de igual dimensión que $\Bbb W$. Es decir, se generan todos los elementos del codominio.

## Matriz de T.L.

Si $\Bbb V$ y $\Bbb W$ son espacios vectoriales de dimensión finita, podemos encontrar una expresión matricial para una transformación lineal $T: \Bbb V \to \Bbb W$.

Supongamos que $B$ y $B'$ son bases de $\Bbb V$ y $\Bbb W$ respectivamente. $B = \{v_1, \cdots, v_n\}, B' = \{w_1, \cdots, w_m\}$

$$
\begin{gathered}
x \in \Bbb V,\quad x = \alpha_1 v_1 + \cdots + \alpha_n v_n \implies T(x) = T(\alpha_1 v_1 + \cdots + \alpha_n v_n)
\\\,\\
\Big[T(x)\Big]^{B'} = \alpha_1\big[T(v_1)\big]^{B'} + \cdots + \alpha_n\big[T(v_n)\big]^{B'}
\end{gathered}
$$

$$
\Big[T(x)\Big]^{B'} = 
\Big[ \big[T(v_1)\big]^{B'} \big| \cdots \big| \big[T(v_n)\big]^{B'}\Big]
\begin{bmatrix}\alpha_1 \\ \vdots \\ \alpha_n\end{bmatrix}
$$

Entonces, obtenemos una matriz de $m\times n$, que nos permite transformar cualquier vector de $\Bbb V$ con coordenadas en $B$, a un vector de $\Bbb W$ con coordenadas en $B'$. A esta matriz se le llama matriz de $T$ con respecto a las bases $B$ y $B'$, y se denota como $[T]_B^{B'}$

$$
[T(x)]^{B'} = [T]_B^{B'} [x]^{B}
$$
