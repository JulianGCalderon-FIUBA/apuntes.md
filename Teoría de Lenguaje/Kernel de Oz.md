Definiremos dos conceptos de Oz. Las expresiones y las declaraciones.

## Expresiones

Con las siguientes definiciones, habremos definido todas las expresiones base de nuestro lenguaje

![[Kernel de Oz 1694370444.png|575]]

## Declaraciones

Con las siguientes definiciones, habremos definido todas las expresiones base de nuestro lenguaje

![[Kernel de Oz 1694370528.png|575]]

Una vez definidos estos dos conceptos, habremos definido la sintaxis del lenguaje completo.

## Elementos Faltantes

Ahora, veremos como definimos los elementos faltantes utilizando estos elementos.

### Multiples Declaraciones

Las declaraciones con más de una variable se podrán realizar anidando declaraciones de una sola variable

![[Kernel de Oz 1694370747.png|500]]

### Declaraciones sin Asignación

Para realizar una asignación en una declaración, podemos colocar la asignación inmediatamente debajo.

![[Kernel de Oz 1694370814.png|500]]

### Funciones a Procedimientos

Las funciones las podremos definir como procedimientos, donde pasamos como variable a asignar como último argumento.

![[Kernel de Oz 1694370848.png|500]]

### Llamados Anidados

Para realizar llamados anidados, necesitaremos una variable auxiliar.

![[Kernel de Oz 1694370957.png|500]]

### Condicionales Booleanos

Necesitaremos una variable auxiliar para almacenar la condición.

![[Kernel de Oz 1694370999.png|500]]
