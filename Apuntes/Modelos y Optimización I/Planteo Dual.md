El problema dual es un problema equivalente al primal (con el mismo valor del funcional), pero será estructurado de forma distinta

# Planteo del Problema

Dada un primal de la primer forma:

$$
AX \leq B\\
X \geq 0\\
\max CX
$$

- ***Planteo del Primal***
    
    Tendremos un problema de maximización, con tres restricciones y dos variables:
    
    $$
    \begin{alignat*}{2}
    -2x_1& + 1x_2& \leq 2\\
    1x_1& - 1x_2& \leq 2\\
    1x_1& + 1x_2& \leq 5\\
    Z_{max} = 10x_1& + 3x_2
    \end{alignat*} 
    $$
    

El problema dual tendrá la siguiente forma:

$$
YA \geq C\\
Y \geq 0\\
\min YB
$$

La dimensión del vector $Y$ será la cantidad de restricciones del problema original

- ***Planteo del Dual***
    
    En el dual, intercambiaremos los términos independientes de las restricciones con los coeficientes del funcional, y los coeficientes de las restricciones se obtendrán transponiendo los originales
    
    $$
    \begin{alignat*}{2}
    -2y_1& + 1y_2& + 1y_3& \geq 10\\
    1y_1& - 1y_2& + 1y_3& \geq 3\\
    Z_{max} = 2y_1& + 2y_2& + 5y_3&
    \end{alignat*} 
    $$
    

Podremos asignar las variables del dual de modo las primeros elementos de $Y$ corresponderán a las variables ***slack***, mientras que lo siguientes elementos corresponderán a las variables reales.

- ***Asignación***
    
    En nuestro ejemplo, asignaremos:
    
    $$
    y_1 \iff x_3\\
    y_2 \iff x_4\\
    y_3 \iff x_5\\
    y_4 \iff x_1\\
    y_5 \iff x_2\\
    $$
    

## Relación entre Primal y Dual

- El dual tiene una variable real por cada restricción del problema primal
- El dual tiene tantas restricciones como variables reales tiene el primar
- El dual de un problema de maximización es un problema de minimización y viceversa
- Los coeficientes del funcional del primal son los términos independientes de las restricciones del dual. Si en el problema original de maximización (minimización), se trataba de un restricción de mayor o igual (menor o igual), el signo se invierte. Esto se debe a que para el planteo, todas las restricciones deben ser de mismo tipo.
- Toda columna de coeficientes en el primal se transforma en una fila de coeficientes en el dual
- El sentido de las desigualdades del primal es el inverso del dual
- Si el planteo primal tiene multiples soluciones alternativas, entonces en el planteo dual tendremos un punto degenerado (pero un único punto)

## Teorema Fundamental de la Dualidad

Si el problema primal (o el dual) tiene una solución óptima finita, entonces el otro problema tiene una solución óptima finita y los valores de los dos funcionales son iguales

Si cualquiera de los dos problemas tiene una solución optima no acotada, entonces el otro problema no tiene soluciones posibles.

## Teorema de la Holgura Complementaria

Dados el problema primal y el dual correspondiente, siempre que en la $k$-ésima restricción de uno de ellos la variable ***slack*** tome valor distinto de cero, entonces la $k$-ésima variable del otro problema desaparece de la base.

Si la $k$-ésima variable de uno de los dos problemas es mayor que cero, en la $k$-ésima restricción del otro problema se verifica la igualdad (la ***slack*** es nula)

## Reconstrucción de Tabla del Dual

Podremos reconstruir la tabla del dual a partir de la tabla del primal: 

- ***Tabla Optima del Primal***
    
    
    | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | $0$ | $x_3$ | $7.5$ | $0$ | $0$ | $1$ | $1.5$ | $0.5$ |
    | $10$ | $x_1$ | $3.5$ | $1$ | $0$ | $0$ | $0.5$ | $0.5$ |
    | $3$ | $x_2$ | $1.5$ | $0$ | $1$ | $0$ | $-0.5$ | $0.5$ |
    |  |  | $39.5$ | $0$ | $0$ | $0$ | $3.5$ | $6.5$ |
1. El valor de las variables del problema dual sera el $z_j - c_j$ de su variable relacionada al directo, el reciproco es valido también. El signo es determinado según el contexto, para el valor de las variables deberá ser siempre positivo, mientras que para el desmejoro dependerá del sentido del funcional.
    - **Valor de las variables**
        
        
        | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
        | --- | --- | --- | --- | --- | --- | --- | --- |
        | $2$ | $y_2$ | $3.5$ |  |  |  |  |  |
        | $5$ | $y_3$ | $6.5$ |  |  |  |  |  |
        |  |  | $39.5$ | $-7.5$ | $0$ | $0$ | $-3.5$ | $-1.5$ |
2. Las vectores asociados a las variables de la base deben contener los vectores canónicos, debido a que nos encontramos en una tabla *simplex.*
    - **Vectores canónicos**
        
        
        | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
        | --- | --- | --- | --- | --- | --- | --- | --- |
        | $2$ | $y_2$ | $3.5$ |  | $1$ | $0$ |  |  |
        | $5$ | $y_3$ | $6.5$ |  | $0$ | $1$ |  |  |
        |  |  | $39.5$ | $-7.5$ | $0$ | $0$ | $-3.5$ | $-1.5$ |
3. El resto de los valores los tomaremos transponiendo las columnas de la primal e invirtiendo sus signos. Sea $A$ la matriz de la tabla del primal y $A'$ la matriz de la tabla del dual, entonces $A_{ij} = -A'_{lk}$, donde $X_i \sim Y_k, X_j \sim X_l$. Nótese que los indices se invierten, ya que los valores de la base de una tabla no estarán en la tabla del otro (transposición).
    - **Valores restantes**
        
        
        | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
        | --- | --- | --- | --- | --- | --- | --- | --- |
        | $2$ | $y_2$ | $3.5$ | $-1.5$ | $1$ | $0$ | $-0.5$ | $0.5$ |
        | $5$ | $y_3$ | $6.5$ | $-0.5$ | $0$ | $1$ | $-0.5$ | $-0.5$ |
        |  |  | $39.5$ | $-7.5$ | $0$ | $0$ | $-3.5$ | $-1.5$ |
        
4. Si una de las filas del planteo dual, provenía de una restricción originalmente de mayor o igual, entonces debo invertir los signos de toda esa fila (tanto el valor de $c_j$, como los $a_{ij}$ de la fila).