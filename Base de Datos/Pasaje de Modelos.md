## Entidades

Los tipos de entidades se transforman en una relación, con los atributos claves como claves primarias.

![[Modelo Relacional 1693352989.png|475]]

## Atributos

Los atributos en las interrelaciones se agregan como atributos normales en sus respectivas tablas, o como un atributo en el lado de la entidad que contiene la clave foránea, en el caso de interrelaciones $1$ a $n$.

### Atributos Multievaluados

Los atributos multievaluados pueden ser representados como una relación $n$ a $n$.

![[Modelo Relacional 1693353045.png|475]]

### Atributos Compuestos

Los atributos compuestos pueden ser representados a partir de sus componentes atómicos.

![[Modelo Relacional 1693433718.png|475]]

## Interrelaciones Binarias

Se resuelven de forma distinta, dependiendo de las cardinalidades

### $N - N$

Se transforman en una relación que contenga como claves foráneas las claves de las entidades que participan.

![[Modelo Relacional 1693353077.png|475]]

Ambas claves foráneas se denotan, además, como claves primarias. Esto permite asociaciones muchos a muchos.

### $1 - N$

La **transformamos** en una interrelación, pero solo la clave foránea del lado de cardinalidad $N$ deben ser marcadas como clave primaria.

![[Modelo Relacional 1693353531.png|475]]

### $1,1 - N$

Si hubiese **participación total**, entonces es mejor reutilizar la tabla de la entidad dependiente.

![[Modelo Relacional 1693353627.png|475]]

Esto permite obligar a la entidad dependiente a relacionarse con otra.

### $1 - 1$

Podemos transformar la interrelación

![[Modelo Relacional 1693353143.png|475]]

### $1,1 - 1$

Si tenemos **una participación total**, es recomendable colocar la clave foránea en la entidad dependiente.

![[Modelo Relacional 1693353180.png|475]]

Nos asegura que se cumpla la dependencia. Además, se puede declarar como clave candidata para imponer la restricción de uno a uno.

### $1,1 - 1,1$

Si ambas tienen participación total, entonces podremos unificarlas en una sola tabla

![[Modelo Relacional 1693353485.png|475]]

Esto resultará en dos claves candidatas, una de cada entidad.

## Interrelaciones Ternarias

Para las relaciones $n$-arias, siempre crearemos una tabla adicional, declarando claves foráneas a las claves principales de las entidades que participan.

### $N - N - N$

Las claves primarias serán todas las claves foráneas

![[Modelo Relacional 1693354368.png|475]]

### $1 - N - N$

Las claves primarias serán las de cardinalidad $N$. Ya que forzara un $1$ en el extremo restante.

![[Modelo Relacional 1693354423.png|475]]

Las claves primarias serán la de cardinalidad $N$, y una de las otras dos restantes. Esto resulta en dos claves candidatas.

![[Modelo Relacional 1693354476.png|475]]

### $1 - 1 - 1$

Cualquier combinación de dos claves primarias es una clave válida, por lo que tendremos tres claves candidata.

![[Modelo Relacional 1693438138.png|475]]

## Interrelaciones Unarias

Se puede resolver con las mismas tácticas que los casos anteriores. Podemos pensar las relaciones unarias como relaciones binarias entre dos tipos de entidades iguales.

![[Modelo Relacional 1693436724.png|475]]

## Entidades Débiles

Las claves dependientes pueden ser registradas como claves foráneas y, a su vez, como claves primarias.

![[Modelo Relacional 1693353713.png|475]]

Como siempre será una dependencia total, no necesitaremos una tabla adicional.

## Especializaciones

Las subclases tienen una clave foránea refiriendo a la superclase, permitiendo expandir sus atributos y relaciones.

![[Pasaje de Modelos 1693606871.png|475]]

Si la especialización es total, podremos eliminar la superclase

![[Modelo Relacional 1693434470.png|475]]

Para agregar la restricción de disyunción, debemos agregar logica adicional a la base de datos.

## Uniones

En las uniones, podemos agregar los atributos de la unión en las superclases

![[Modelo Relacional 1693435127.png|475]]

Otra forma de resolverlo, es a partir de una clave subrogada que relacione las superclases con la unión.

![[Modelo Relacional 1693354200.png|475]]

Una clave **subrogada** es una clave independiente de los datos que utilizamos para diferenciar dos entidades. Se utiliza cuando no hay un clave primaria clave, o el conjunto de clave primaria es muy grande.

## Agregación

Primero, creamos una relación para el tipo de interrelación de la agregación. Luego, podemos referir a una tupla de esta relación en una nueva relación externa.

![[Modelo Relacional 1693438567.png|475]]

Notamos que la clave foránea incluye dos elementos, pues son una misma clave foránea que refiere a una sola relación.
