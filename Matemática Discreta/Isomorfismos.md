## Isomorfismos

Dos grafos se consideran iguales si coinciden los tres elementos de la terna que lo definen. EN cambio, dos grafos simples son isomorfos solo si preservan todos sus *invariantes,* pero la recíproca es falsa.

Llamamos ***invariantes de un grafo*** a cualquier propiedad que se mantiene ante isomorfismos,. Ningún conjunto de variantes es un juego completo: Conexidad, Secuencia, Sucesión, Diámetro, Centro, Periferias.

Si dos grafos simples son isomorfos, cada grafo es representante de la clase de todos los grafos que le son isomorfos, y entonces puede prescindirse de las etiquetas (grafos no etiquetados)

Dados dos grafos simples $G$ y $H$, se considera que son isomorfos con $G \cong H \iff \exists \theta: V(G) \to V(H)$ biyectiva tal que $uv \in E(G) \iff \theta(u)\theta(v) \in E(H)$. Es decir, si preservan las adyacencias

Ademas $G \cong H$ con el isomorfismo definido por $\theta: V(G) \to V(H)$ *sii* la correspondiente matriz de permutación $P \in \{0,1\}^{n\times n}$ satisface $A_G = P^{-1}A_HP$. Esto es, $A_G$ y $A_H$ son semejantes.

Para calcular, $P$ permutaremos las filas de la matriz identidad $I_n$ como indica la permutación $\theta$. $P{-1} = P_T$ se obtendrá permutando de la misma forma, las columnas de la identidad.

## Auto morfismos

Un auto morfismo en $G$ es un isomorfismo de $G$ en si mismo. Es decir, una permutación $\theta$ tal que se preserven las adyacencias

Se designa $\text{Aut(G)}$ al conjunto de auto morfismos en $G$.
