En una base de datos relacional, la información se organiza en distintas **tablas**. Cada tabla mantiene múltiples columnas y cada columna un nombre único. Cada fila representa un pedazo de información.

> [!example] Contraejemplo
> No todas las BDD hoy en dia son relacionales. MongoDB almacena información en documentos JSON

## Definición Matemática

Un **nombre de relación** $R$ junto con su lista de atributos asociados se denomina esquema de relación, y se denota como $R(A_1, A_2, \cdots, A_n)$.

Cada uno de los atributos $A_i$ tiene un **dominio** $D_i$ asociado, que indica los valores posibles que pueden tomar los elementos de $A_i$.

Una **relación** $R$ con esquemas de relación $R(A_1, A_2, \cdots, A_n)$ es un subconjunto del producto cartesiano $D_1 \times D_2 \times \cdots \times D_n$

A cada elemento de una relación se lo denomina **tupla**

A partir de estas definiciones, podemos definir una función llamada **predicado** para cada relación que, a partir de una tupla $(D_1, D_2, \cdots, D_n)$ nos devuelva si estos se encuentran relacionados.

El **valor** tomado por un atributo $A$ en determinada tupla $t$ se denota como $t[A]$, o $t.A$.

La **cardinalidad** de una relación es la cantidad de tuplas que posee.

## Restricciones

Una restricción de **dominio** especifican que dado un atributo $A$ de una relación $R$. El valor del atributo de una tupla $t$ debe pertenecer al dominio $D$ de $A$.

En el modelo relacional, se permiten que algunos valores tomen un valor **nulo**.

Los atributos deben ser **monoevaluados** Esto quiere decir que no se permiten arreglos de valores.

Los atributos deben ser **atómicos**. No se permiten valores compuestos.

No puede haber dos tuplas que coincidan en los valores de todos sus atributos. Generalmente, hay un subconjunto de atributos $SK$ para el cual se cumple la condición que dos tuplas cualesquiera difieran en al menos uno de los atributos de $SK$.

Cuando un subconjunto $SK$ de atributos cumple también esta prioridad, se dice que son una **superclave** de $R$. Las superclaves que son minimales se denominan **claves candidatas**. Solo una de ellas se designa como **clave primaria**.

Una **clave foránea** es un atributo de una tupla que refiere a una clave primaria de otra tupla (de la misma, u otra relación)

En una base de datos relacional, la información se representa a través de un esquema de bases de datos relacional. Un esquema de bases de datos relacional es un conjunto de esquemas de relación $S = \{R_1, R_2, \cdots, R_n\}$, junto con una serie de restricciones de integridad.

La restricción de **integridad de entidad** dice que la clave primaria de una entidad no puede tomar un valor nulo.

La restricción de **integridad referencial** dice que si una tupla de $R$ tiene una **clave foránea** de $S$. Entonces debe existir una tupla en $S$ con la clave foránea como claves primaria. Las claves foráneas pueden, a su vez, ser claves primarias.

## Operaciones

Las operaciones del modelo relacional se especifican a través de lenguajes como el **álgebra relacional** o el cálculo relacional.

Las operaciones de **consulta** no modifican ninguna relación existente, por lo que no violan ningún tipo de restricción.

Las operaciones de **inserción** pueden violar restricciones de dominio, de unicidad y de integridad de entidad o referencial.

Las operaciones de **eliminación** solo pueden violar restricciones de integridad referencial. La eliminación en cascada se encarga de eliminar todas las tuplas que refieren a la entidad a eliminar.

En las operaciones de **modificación**, si se modifica una clave foránea, se debe verificar que sus nuevos valores referencien a una tupla existente de la relación referenciada. Si se modifica una clave primaria, pueden violarse cualquiera de las restricciones de integridad.

## Pasaje de Modelo Conceptual a Modelo Relacional

### Entidades

Los tipos de entidades se transforman en una relación, con los atributos claves como claves primarias.

![[Modelo Relacional 1693352989.png|475]]

### Interrelaciones

Los tipos de interrelaciones se resuelven de distintas formas según las cardinalidades

#### Muchos a Muchos

Para el caso de $n$ a $n$ se transforman en una relación que contenga como claves foráneas las claves de las entidades que participan.

![[Modelo Relacional 1693353077.png|475]]

#### Uno a Muchos

Podremos utilizar una relación adicional para la interrelación

![[Modelo Relacional 1693353531.png|475]]

Si hubiese participación total, entonces es mejor reutilizar la tabla de la entidad dependiente.

![[Modelo Relacional 1693353627.png|475]]

#### Uno a Uno

Una opción simple es utilizar una relación adicional

![[Modelo Relacional 1693353143.png|500]]

Si tenemos participación total, es recomendable colocar la clave foránea en la entidad dependiente.

![[Modelo Relacional 1693353180.png|500]]

Nos asegura que se cumpla la dependencia. Además, se puede declarar como clave candidata para imponer la restricción de uno a uno.

Si no hay participación total, debemos admitir que la clave foránea tome valor nulo.

Si ambas tienen participación total, entonces podremos unificarlas en una sola tabla

![[Modelo Relacional 1693353485.png|500]]

#### Ternarias

Podemos generar una tabla adicional con claves foráneas a las claves principales de las entidades que participan.

Para el caso de ternaria con cardinalidad $N, N, N$, las claves primarias serán todas las claves foráneas

![[Modelo Relacional 1693354368.png|500]]

Para el caso de ternaria con cardinalidad $N, N, 1$, las claves primarias serán las de cardinalidad $N$.

![[Modelo Relacional 1693354423.png|500]]

Para el caso de ternaria con cardinalidad $N, 1, 1$, las claves primarias serán la de cardinalidad $N$, y alguna otra.

![[Modelo Relacional 1693354476.png|500]]

### Atributos

Los atributos en las interrelaciones se agregan como atributos normales en sus respectivas tablas, o como un atributo en el lado de la entidad que contiene la clave foránea, en el caso de interrelaciones $1$ a $n$.

Los atributos multievaluados pueden ser representados como una relación $n$ a $n$.

![[Modelo Relacional 1693353045.png|475]]

Los atributos compuestos pueden ser representados a partir de sus componentes atómicos.

### Entidades Débiles

Las claves dependientes pueden ser registradas como claves foráneas y, a su vez, como claves primarias.

![[Modelo Relacional 1693353713.png|475]]

Como siempre será una dependencia total, no necesitaremos una tabla adicional.

### Especializaciones

Las subclases tienen una clave foránea refiriendo a la superclase, permitiendo expandir sus atributos y relaciones.

![[Modelo Relacional 1693354035.png|475]]

### Uniones

Para las uniones, las superclases tienen una clave subrogada, refiriendo a la subclase.

![[Modelo Relacional 1693354200.png|475]]
