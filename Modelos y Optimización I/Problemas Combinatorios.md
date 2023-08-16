---
title: Problemas Combinatorios
---

Los problemas combinatorios son aquellos en los cuales se desea determinar combinaciones óptimas. Se caracterizan por tener un número finito de soluciones factibles. Generalmente, este número es muy grande

## Problema de Distribución o Transporte

Tenemos un conjunto de lugares, cada uno de los cuales tiene disponible una cantidad de unidades de un producto. Otro conjunto de lugares, cada uno de los cuales demanda una cantidad de unidades de un producto. Se conoce el costo $C_{ij}$ de enviar una unidad desde el origen $i$ hasta el destino $j$. Si la cantidad de unidades de un producto no es igual a la demanda, entonces tendremos que definir destinos ficticios, ya sean para indicar faltantes como sobrantes.

El objetivo es determinar la cantidad de unidades de producto que cada origen envía a cada destino, para minimizar los costos de transporte totales en un cierto periodo de tiempo.

Supondremos que el producto es homogéneo (el mismo en origen y en destino), y los costos de envío son lineales (proporcionales a la cantidad de producto enviado).

### Formulación

Definimos $X_{ij}$ como la cantidad de unidades del origen $i$ a enviar al destino $j$. Debemos asegurarnos que se cumpla la demanda y la disponibilidad de todos los productos.

$$
\sum_{j=1}^{n_d}X_{ij} = \text{Disponibilidad de origen $i$}, \forall i
$$

$$
\sum_{i=1}^{n_o}X_{ij} = \text{Disponibilidad de destino $j$}, \forall j
$$

Para definir el funcional, definiremos las constantes $C_{ij}$ que indica el costo de distribuir unidad del origen $i$ al destino $j$

$$
Z_{\min} \sum_{i=0}^{n_o}\sum_{j=0}^{n_d} C_{ij}X_{ij}, \quad \forall i,j
$$

Existe un teorema que demuestra que, si todas las ofertas son números enteros, y todas las demandas son números enteros, siendo todas las restricciones igualdades, el problema de distribución o transporte tendrá como resultado que todas las variables tomarán valor entero.

## Problema de Transbordo

En este problema, las unidades no son enviadas directamente desde los orígenes hacia los destinos, sino que las unidades van desde los orígenes hasta alguno de los centros de transbordo y desde este a alguno de los destinos.

### Formulación

Definimos $XO_iT_J$ como la cantidad de unidades que son enviadas desde el origen $i$ hasta el transbordo $j$. También definimos $XT_iDj$ la cantidad de unidades que son enviadas del transbordo $i$ hasta el destino $j$. Debemos asegurarnos que se cumpla la demanda y la disponibilidad de todos los productos.

$$
\sum_{j=1}^{n_t}XO_iT_j = \text{Disponibilidad de origen $i$}, \forall i
$$

$$
\sum_{i=1}^{n_t} XT_iD_j = \text{Disponibilidad de destino $j$}, \forall j
$$

Por otro lado, todo lo que entra en un transbordo debe salir

$$
\sum_{i=1}^{n_o} XO_i T_j = \sum_{i=1}^{n_d}XT_jD_i, \quad\forall j = 0,1,\cdots,n_t
$$

Para calcular el funcional, definimos la constante $CO_iT_j$ como el costo de enviar una unidad del origen $i$ al transbordo $j$. También definimos $CT_iD_j$ como el costo de enviar una unidad del transbordo $i$ al destino $j$.

$$
Z_{\min} \sum_{i=1}^{n_o}\sum_{j=1}^{n_t} CO_iT_j \times XO_iT_j + \sum_{i=1}^{n_t}\sum_{j=1}^{n_d} CT_iD_j \times XT_iD_j
$$

## Problema de Asignación

Sean $A, B$, dos conjuntos con $n$ elementos. El problema de asignación consiste en encontrar el conjunto $P$ tal que cada elemento de $P$ es un par $(a,b) \in A\times B$, tal que minimice una función de costo $\sum C(a,b)$. Se debe cumplir que cada elemento de $A$ debe aparecer en $P$ exactamente una vez, y cada elemento de $B$ debe aparecer en $P$ exactamente una vez.

Definimos la variable bivalente $Y_{ij}$ como positiva si el elemento $i$ de $A$ está asignado al elemento $j$ de $B$. Luego restringimos a que cada elemento aparezca una sola vez.

$$
\sum_{j=1}^n Y_{ij} = 1,\quad \forall i
$$

$$
\sum_{i=1}^n Y_{ij} = 1,\quad \forall j
$$

Para el funcional, definimos la constante $C_{ij}$ como el costo de asociar el elemento $i$ con el elemento $j$.

$$
Z_{\min} = \sum_{i=1}^n\sum_{j=1}^n C_{ij}Y_{ij}
$$

### Asignación Cuadrática

Ocurre cuando existe un costo o beneficio que se produce únicamente si se dan dos asociaciones particulares en conjunto.

Sea $C_{ijkl}$ el costo asociado al par de asociaciones $ij$ y $kl$. Entonces el funcional valdría:

$$
\sum_{i=1}^M\sum_{j=1}^M\sum_{k=1}^M\sum_{l=1}^M Y_{ij} Y_{kl} C_{ijkl}
$$

Parece que el funcional es cuadrático. Para solucionarlo, definimos una nueva variable $Y_{ijkl}$ que tome valor uno si ambas asociaciones se cumplen:

$$
2Y_{ijkl} \leq Y_{ij} + Y_{kl} \leq 1 + Y_{ijkl}
$$

Cambiamos el funcional por el linealizado

$$
\sum_{i=1}^M\sum_{j=1}^M\sum_{k=1}^M\sum_{l=1}^M Y_{ijkl} C_{ijkl}
$$

## Problema de la Mochila

Este problema se caracteriza por tener una persona con una mochila con una cierta capacidad, y tiene que elegir qué elementos pondrá en ella. Cada elemento aportará un valor, pero también ocupará espacio en la mochila.

Definiendo las siguientes variables:

- Capacidad de la mochila constante: $C$.
- Beneficio unitario por llevar el producto $i$: $P_i$
- Peso del producto $i$: $W_i$
- Cantidad de elementos constante: $N$

Por último, defino $Y_i$ como verdadero si llevo el elemento en la mochila. Entonces podemos plantear el modelo como:

$$
\sum_{i=1}^n W_iY_i \leq C
$$

$$
Z_{\max} = \sum_{i=1}^n P_iY_i
$$

El problema es simple, pero existen múltiples variantes

### Acotado

En lugar de contar con un elemento de cada tipo, podremos llevar muchos. Bastaría con utilizar variables enteras $X_i$ en lugar de las bivalentes, definiendo límites de ser necesario.

### Suma de Subconjuntos

Si el beneficio de cada elemento equivale a su peso, estamos ante un problema de suma de subconjuntos.

### Múltiples Mochilas

En este caso, definiremos $Y_{ij}$ si se lleva el elemento $i$ en la mochila $j$. Luego

$$
\sum_{i=1}^n W_iY_{ij} \leq C_j,\quad \forall j
$$

$$
Z_{\max} = \sum_{i=1}^n\sum_{j=1}^m P_iY_{ij}
$$

Cada elemento puede estar en una única mochila

$$
\sum_{j=1}^m Y_{ij} \leq 1, \quad\ \forall i
$$

## Calendarización (Scheduling)

Se busca encontrar una solución a la pregunta ¿En qué orden deberán ejecutarse las tareas? ¿Quién deberá ejecutar cada tarea? Analicemos el caso de una fábrica.

Definimos dos variables. $I_{ij}$ como el tiempo en el que empieza la tarea $i$ en la máquina $j$, y $F_{ij}$ como el tiempo en el que finaliza la tare $i$ en la máquina $j$. Si las tareas no se interrumpen, tendremos que:

$$
F_{ij} = I_{ij} + T_{ij}
$$

Siendo $T_{ij}$ el tiempo constante que le toma a la máquina $j$ ejecutar la tarea $i$.

Si únicamente tenemos dos tareas, y si las tareas deben ejecutarse primero en la máquina $1$ y luego en la máquina $2$, entonces debemos definir que:

$$
F_{i1} \leq I_{i2},\quad \forall i
$$

Si buscamos el tiempo total que toma completar el trabajo, entonces tendremos que:

$$
\text{FINAL} \geq F_{i2}, \quad \forall i
$$

Las tareas no pueden ejecutarse a la vez en cada máquina, esto se puede plantear indicar que se deben cumplir uno de dos casos. La tarea $A$ finaliza antes de que empiece la tarea $B$. La tarea $B$ finaliza antes de que empiece la tarea $A$. Planteamos entonces para cada par desordenado de tareas $i,j$ en cada máquina $k$.

$$
\begin{gathered}
F_{ik} \leq I_{jk} + M Y_{i<j} \\
F_{jk} \leq I_{ik} + M Y_{i>j} \\
Y_{i< j} + Y_{i>j} = 1
\end{gathered}
$$

### Notación

Es un problema tan común que se propuso una notación para identificarlos:

$$
\alpha | \beta | \gamma
$$

El término $\alpha$ representa el entorno de máquinas. Una única máquina se representa con un uno, $m$ máquinas idénticas se identifica con $P_m$.

El segundo término $\beta$ índica las características de la tarea. $pmtn$ en este término indica que las tareas son interrumpibles

El último término $\gamma$ incluye la función objetivo. Minimizar el término se denota con $\text{Cmax}$.

## Satisfacibilidad Booleana - SAT

Dada una función proposicional en su forma normal conjuntiva, hallar los valores para los cuales la proposición es verdadera.

Se definen $X_i$ como variables binarias o bivalentes y definimos $Y$ como verdadera si existe solución. Luego planteamos las restricciones de la forma:

$$
\begin{gathered}
f_1(X) \geq Y \\
f_2(X) \geq Y \\
\cdots
\end{gathered}
$$

Donde $f_i$ son las proposiciones cuya intersección forma la función proposicional original.

## Uncapacitated Facility Location (UFL)

Se debe decidir dónde abrir los depósitos, qué proporción de la demanda de los clientes satisface cada depositó abierto.

Definimos $X_{ij}$ como la fracción de la demanda de la zona $j$ satisfecha por el depósito ubicado en $i$. Por otro lado, $Y_i$ valdrá $1$ cuando se establece un depósito en $i$.

Conoceremos $f_i$ como el costo anual fijo de establecer un depósito en el lugar $i$, y $c_{ij}$ como el costo de producción y distribución si el depósito que está ubicado en $i$ le proporcionará al cliente $j$ todo lo que este demanda.

El modelo propuesto por Erlenkotter (1978) es minimizar:

$$
Z_{\min} = \sum_i\sum_j c_{ij}x_{ij} + \sum_i f_iy_i
$$

Se debe satisfacer toda la demanda de todos los clientes

$$
\sum_i x_{ij} = 1,\quad \forall j
$$

Para que una fábrica distribuya producto, deberá haber sido establecida

$$
x_{ij} \leq y_i, \quad \forall i,j
$$

Para que tenga sentido, se define $Y_i$ como bivalente y $x_{ij}$ como positiva, $\forall i,j$
