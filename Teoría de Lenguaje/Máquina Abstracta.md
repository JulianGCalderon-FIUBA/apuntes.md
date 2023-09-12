La máquina abstracta es un modelo teórico de una máquina virtual, que nos permite definir la semántica de un lenguaje de programación.

Definimos que efecto tienen las instrucciones en nuestra máquina abstracta.

## Single Assignment Store

El primer elemento de una máquina abstracta es la memoria. Las variables serán declarativas.

- Se permiten variables sin valores asignados: **partial values**.
- Cuando todas las variables tienen un valor asignado, se dice que tendremos un **value store**.
- Si quiero usar una variable que no tiene valor, espero a su valor. Este concepto se conoce como **dataflow**.

Cada declaración se va a ejecutar en un entorno de ejecución.

## Entorno

El entorno nos indicará a qué variable apunta cada identificador de variable:

- Denotamos con `<x>` al identificador de una variable
- Denotamos con `E(<x>)`al valor en el *store* del identificador `<x>`, según su entorno.

Tendremos dos operaciones:

- **Adición:** Debemos indicar para un identificador de variable, a que variable efectiva está apuntando. Nos permite agregarle a un entorno, nuevas variables `E' = E + {<x> -> x}`
- **Restricción:** Nos permite descartar variables que ya no pertenecen al entorno `E' = E|_{<x>,..<z>}`

## Stack

El stack de nuestra ejecución es una pila de *semantic statements*. Un **semantic statement** es un par `(<s>, E)`, siendo `<s>` un *statement*.

## Computo

El cómputo es el estado de ejecución del programa. El cómputo define como se modifica el estado de ejecución de un programa.

$$
(ST_0, \sigma_0) \to (ST_1, \sigma_1) \to \cdots, \to, (ST_n, \sigma_n)
$$

## Estados de Ejecución

Tenemos tres estados de ejecución posibles:

- Ejecutable
- Terminado
- Suspendido
