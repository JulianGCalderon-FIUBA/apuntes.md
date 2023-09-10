La máquina abstracta es una forma de definir la semántica de un lenguaje de programación.

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
- **Adición:** `E' = E + {<x> -> x}`
- **Restrucción:** `E' = E`
