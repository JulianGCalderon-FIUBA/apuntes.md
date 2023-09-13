## Entidades

Los tipos de entidades se transforman en una relación, con los atributos claves como claves primarias.

![[Pasaje de Modelos 1694374211.png|475]]

## Atributos

Los atributos en las interrelaciones se agregan como atributos normales en sus respectivas tablas, o como un atributo en el lado de la entidad que contiene la clave foránea, en el caso de interrelaciones $1$ a $n$.

### Atributos Multievaluados

Los atributos multievaluados pueden ser representados como una relación $n$ a $n$.

![[Pasaje de Modelos 1694374211-1.png|475]]

### Atributos Compuestos

Los atributos compuestos pueden ser representados a partir de sus componentes atómicos.

![[Pasaje de Modelos 1694374211-2.png|475]]

## Interrelaciones Binarias

Se resuelven de forma distinta, dependiendo de las cardinalidades

### $N - N$

Se transforman en una relación que contenga como claves foráneas las claves de las entidades que participan.

![[Pasaje de Modelos 1694374211-3.png|475]]

Ambas claves foráneas se denotan, además, como claves primarias. Esto permite asociaciones muchos a muchos.

### $1 - N$

La **transformamos** en una interrelación, pero solo la clave foránea del lado de cardinalidad $N$ deben ser marcadas como clave primaria.

![[Pasaje de Modelos 1694374211-4.png|475]]

### $1,1 - N$

Si hubiese **participación total**, entonces es mejor reutilizar la tabla de la entidad dependiente.

![[Pasaje de Modelos 1694374212.png|475]]

Esto permite obligar a la entidad dependiente a relacionarse con otra.

### $1 - 1$

Podemos transformar la interrelación

![[Pasaje de Modelos 1694374212-1.png|475]]

### $1,1 - 1$

Si tenemos **una participación total**, es recomendable colocar la clave foránea en la entidad dependiente.

![[Pasaje de Modelos 1694374212-2.png|475]]

Nos asegura que se cumpla la dependencia. Además, se puede declarar como clave candidata para imponer la restricción de uno a uno.

### $1,1 - 1,1$

Si ambas tienen participación total, entonces podremos unificarlas en una sola tabla

![[Pasaje de Modelos 1694374212-3.png|475]]

Esto resultará en dos claves candidatas, una de cada entidad.

## Interrelaciones Ternarias

Para las relaciones $n$-arias, siempre crearemos una tabla adicional, declarando claves foráneas a las claves principales de las entidades que participan.

### $N - N - N$

Las claves primarias serán todas las claves foráneas

![[Pasaje de Modelos 1694374212-4.png|475]]

### $1 - N - N$

Las claves primarias serán las de cardinalidad $N$. Ya que forzara un $1$ en el extremo restante.

![[Pasaje de Modelos 1694374212-5.png|475]]

Las claves primarias serán la de cardinalidad $N$, y una de las otras dos restantes. Esto resulta en dos claves candidatas.

![[Pasaje de Modelos 1694374212-6.png|475]]

### $1 - 1 - 1$

Cualquier combinación de dos claves primarias es una clave válida, por lo que tendremos tres claves candidata.

![[Pasaje de Modelos 1694374212-7.png|475]]

## Interrelaciones Unarias

Se puede resolver con las mismas tácticas que los casos anteriores. Podemos pensar las relaciones unarias como relaciones binarias entre dos tipos de entidades iguales.

![[Pasaje de Modelos 1694374212-8.png|475]]

## Entidades Débiles

Las claves dependientes pueden ser registradas como claves foráneas y, a su vez, como claves primarias.

![[Pasaje de Modelos 1694374212-9.png|475]]

Como siempre será una dependencia total, no necesitaremos una tabla adicional.

## Especializaciones

Las subclases tienen una clave foránea refiriendo a la superclase, permitiendo expandir sus atributos y relaciones.

![[Pasaje de Modelos 1694630382.png|475]]

Si la especialización es total y disjunta, podremos eliminar la superclase

![[Pasaje de Modelos 1694374212-10.png|475]]

Para agregar la restricción de disyunción, debemos agregar logica adicional a la base de datos.

## Uniones

En las uniones, podemos agregar los atributos de la unión en las superclases

![[Pasaje de Modelos 1694374213.png|475]]

Otra forma de resolverlo, es a partir de una clave subrogada que relacione las superclases con la unión.

![[Pasaje de Modelos 1694374213-1.png|475]]

Una clave **subrogada** es una clave independiente de los datos que utilizamos para diferenciar dos entidades. Se utiliza cuando no hay un clave primaria clave, o el conjunto de clave primaria es muy grande.

## Agregación

Primero, creamos una relación para el tipo de interrelación de la agregación. Luego, podemos referir a una tupla de esta relación en una nueva relación externa.

![[Pasaje de Modelos 1694374213-2.png|475]]

Notamos que la clave foránea incluye dos elementos, pues son una misma clave foránea que refiere a una sola relación.
