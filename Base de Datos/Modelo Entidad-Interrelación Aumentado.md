Con el tiempo, surgieron bases de datos con restricciones más complejas de las que permitía el modelo entidad-interrelación. Esto llevo al desarrollo de un modelo con conceptos semánticos adicionales, además de los anteriores.

## Subclases y Superclases

Las subclases y superclases nos permiten representar relaciones del tipo "es un" en el modelo de datos. Un miembro de una subclase pertenece al mismo tipo de su entidad padre, pero en con un rol específico.

A través del concepto de herencia, las subclases heredan atributos y tipos de interrelaciones de su entidad padre.

![[Modelo Entidad-Interrelación Aumentado 1.png]]

### Especialización

La **especialización** es el proceso de definir un conjunto de subclases para un tipo de entidad, la cual es denominada superclase. Podemos tener distintas especializaciones para un mismo tipo de entidad, basándose en características distintas.

### Generalización

Podemos pensar la **generalización** como el proceso inverso. Es la identificación de características comunes y la abstracción de esas características en una superclase.

### Atributos y Tipos de Interrelaciones Específicos

Las subclases pueden tener **atributos específicos** o locales. A su vez, pueden participar en **tipos de interrelaciones específicos**.

La especialización se utiliza cuando algunos atributos o participaciones aplican a algunas entidades de un tipo de entidad, pero no a todos. En este caso podemos usar especialización para diferenciar estas entidades.

### Definidas por Condición

En algunas especializaciones, podemos determinar exactamente qué entidades pertenecerán a una subclase. Diremos que estas subclases son **definidas por condición**.

![[Modelo Entidad-Interrelación Aumentado 2.png|450]]

Si todas las subclases en una especialización utilizan el mismo atributo como condición, diremos que es una especialización **definida por atributo**.

Cuando no existe una condición, diremos que la subclase es **definida por usuario**.

### Disyunción

La restricción de **disyunción**, especifica que las subclases de una especialización son conjuntos disjuntos. Esto quiere decir que pueden ser miembros de, a lo sumo, una subclase. Las especializaciones definidas por atributo son automáticamente disjuntas. Se denotan con la letra 'd'.

Si no existe esta restricción, entonces los conjuntos de entidades pueden **superponerse**, permitiendo que una misma entidad pertenezca a más de una subclase, en una misma especialización. Se denotan con la letra 'o'.

![[Modelo Entidad-Interrelación Aumentado 3.png|525]]

### Completitud

La restricción de **completitud** o totalidad puede ser total, o parcial. Una **especialización total** implica que cada entidad de la superclase debe ser miembro de al menos una subclase. Una **especialización parcial**, por otro lado, no impone esta restricción.

Por lo general, una superclase que fue identificada a través de la generalización es total, pues la superclase fue derivada de las subclases.

### Jerarquías y Redes

En una **especialización jerárquica**, cada subclase participa como subclase con a lo sumo una superclase, resultando en una estructura de árbol.

En una **especialización en red**, las subclases pueden tener más de una superclase. Estas clases son denominadas **subclases compartidas**

![[Modelo Entidad-Interrelación Aumentado 4.png|550]]

En estas especializaciones, las subclases heredan atributos e interrelaciones no solo de su superclase, sino de todos sus predecesores hasta la raíz de la jerarquía o red.

## Categorías

En algunas situaciones, es necesario representar una colección de entidades de distintos tipos de entidad. En esta clase, utilizamos la **unión**, llamaremos a cada subclase como una **categoría**.

![[Modelo Entidad-Interrelación Aumentado 5.png]]

Cuando una **subclase** tiene múltiples superclases (como es en el caso de la especialización en red), entonces una entidad de la subclase es, a su vez, miembro de todas las superclases. Cuando una **categoría** tiene múltiples superclases, entonces una entidad perteneciente a dicha categoría pertenece a exactamente una sola de las superclases.

La herencia de atributos funciona de forma más selectiva en el caso de las categorías. La categoría solo hereda los atributos de la superclase a la cual pertenece la entidad.

Una categoría puede ser **total**, involucrando a todas las entidades de sus superclases, o puede ser **parcial**, involucrando solo un subconjunto de ellas. Una categoría total se representa con una doble raya conectando la categoría con el círculo, mientras que una parcial se representa con una raya simple.

## Agregación

En una relación ternaria, no se permite que dos entidades participen en una interrelación, sin incluir a una tercera.

![[Modelo Entidad-Interrelación Aumentado 6.png|473]]

En este caso, todas las entrevistas deben resultar en una oferta de trabajo. Para salvar estos escenarios, se utilizan las agregaciones.

![[Modelo Entidad-Interrelación Aumentado 7.png|478]]

Se genera una agregación que incluye el tipo de interrelación "entrevista", y esta se interrelaciona con la oferta de trabajo.

En el modelo entidad-interrelación original, esto se resuelve utilizando entidades débiles.

![[Modelo Entidad-Interrelación Aumentado 8.png|474]]
