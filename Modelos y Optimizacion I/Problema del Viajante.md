El problema de determinar el mejor circuito entra varias ubicaciones fue encarado por distintas profesiones desde la prehistoria, este es conocido como el problema del viajante:

- Un viajante tiene que partir de su casa y visitar una serie de clientes antes de retornar finalmente a su casa
- No puede dejar de visitar ningún cliente
- Se conocen las distancias entre cada par de clientes y entre cada cliente y la casa del viajante

Una formulación equivalente en términos de teoría de grafos es la de encontrar en un grafo completamente conexo y con arcos ponderados (pesado) el ciclo hamiltoniano de menor costo. El ciclo hamiltoniano en un grafo es un camino cerrado que pasa una sola vez por todos los nodos del grafo.

## Tipo del Problema

Dependiendo de si la dirección en la cual se atraviesa una ciudad importa o no, se define:

- **Viajante simétrico:** No importa la dirección.
- **Viajante asimétrico:** Importa la dirección.

En otras palabras, se define un viajante asimétrico para un grafo dirigido.

## Formulación

Definimos las variables bivalentes $Y_{ij}$ para que tomen valor positivo cuando se utiliza el camino que va de la ciudad $i$ a la ciudad $j$, con $i,j = 0,1, \cdots, n$. Siendo $n$ la cantidad de ciudades. Consideramos la ciudad inicial como la ciudad $0$. Por otro lado, definimos $C_{ij}$ constante como el costo de utilizar el camino que va de la ciudad $i$ a la ciudad $j$.

Primero, debemos asegurarnos que solo lleguemos a una ciudad una sola vez, y que solo salgamos de una ciudad una sola vez.

$$

\sum_{i=0, i\neq j}^n Y_{ij} = 0,\quad \forall i=0,1,2,\cdots, n
$$

$$

\sum_{j=0, i\neq j}^n Y_{ij} = 0,\quad \forall j=0,1,2,\cdots, n
$$

Luego, podemos definir el funcional como el costo de los caminos utilizados

$$
Z_{\min} = \sum_{i=0}^{n}\sum_{ j=0, i\neq j}^{n} C_{ij}Y_{ij}
$$

Esta dos restricciones aún no son suficientes, ya que todavía no impedimos la formación de **subtours**. Sean $A, B, \cdots, G$ siete ciudades, entonces los caminos $GF, FD, DG$ no incumplirán restricciones, pero formarían un camino aislado.

### Formulación MTZ

La formulación **MTZ**, llamada así tras los que la formularon (Miller, Kuhn, Tucker), define $U_i$ como el número de secuencia en el cual la ciudad $i$ es visitada, para todo $i = 1, 2, \cdots, n$.

$$
U_i - U_j + nY_{ij} \leq n-1
$$

Si se utiliza el camino $ij$, entonces tendremos que $U_i - U_j \leq -1$. En otras palabras, el número de secuencia de la ciudad $U_i$ debe ser menor al número de secuencia de la ciudad $U_j$. A partir del primer caso, se obliga a que todas las ciudades tomen un número de secuencia distinto y ordenado, evitando así la formación de subtours. Si analizamos el ejemplo anterior: $CF, FD, DC$ e imponemos las restricciones, tendremos $U_c < U_f < U_d < U_c$, esto es absurdo. Debido a que no estamos utilizando $i=0$ en la formación de restricciones, el único camino cerrado que podemos formar es aquel que incluya a la ciudad cero, (y, por lo tanto, completo).

Si no se utiliza el camino $ij$, entonces tendremos que $U_i - U_j \leq n-1$. En otras palabras, la diferencia de secuencia entre todo par de ciudades debe ser menor o igual a $n-1$. Esto obliga a que los números de secuencia no solo estén ordenados, sino que además sean consecutivos. Sean $U_1, \cdots, U_n$ números distintos tal que $U_1 <U_2< \cdots < U_n$, con $U_n - U_1 \leq n-1$. Entonces los únicos valores que posibles que podrán tomar los números de secuencia serán los números consecutivos de $1$ a $n$.

## Características del problema

Una situación se modela como problema del viajante cuando:

- En el problema se plantean actividades o cosas de las cuales no se conoce el orden en el cual se realizan
- La función objetivo dependerá del orden que indique el modelo para esas actividades.

## Variaciones al problema del Viajante

### Variables para Recorrido

Si contamos con que existen dos tramos posibles para cada par de ciudades posible, entonces podemos separar $Y_{ij}$ en uno de los tramos utilizados

$$
Y_{ij} = Y_{A_{ij}} + Y_{B_{ij}}
$$

$$
Z_{\min} = \sum_{i=0}^{n}\sum_{ j=0, i\neq j}^{n} C_{A_{ij}}Y_{A_{ij}} + C_{B_{ij}}Y_{B_{ij}}
$$

### Variables de Orden

Se debe visitar la ciudad $i$ antes de visitar la ciudad $j$, entonces

$$
U_i < U_j
$$

No se puede visitar la ciudad $i$ sin antes visitar la ciudad $j$ o la ciudad $k$

$$
U_i \geq U_j - MY
$$

$$
U_i \geq U_k - M(1-Y)
$$

> [!note] Nota
> Estamos obligando a cumplir una de las dos restricciones, pero eso no implica que ambas no se pueden cumplir a la vez. Una restricción anulada puede igualmente cumplirse.
