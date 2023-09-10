Un lenguaje de programación es aquel que es **Turing completo**. Esto quiere decir que el lenguaje es computable por una máquina de Turing.

## Conceptos de Programación

Los **lenguajes** de programación soporta distintos **paradigmas**. Un paradigma es un grupo de **conceptos**, relacionados entre sí.

No vamos a estudiar los paradigmas, sino los conceptos que abarca. Los lenguajes pueden implementar, de forma muy distinta, los distintos conceptos.

> [!example] Ejemplo
> El paradigma orientado a objetos abarca distintos conceptos independientes pero interrelacionados: herencia, abstracción, privatización, etc.

## Elementos de un Lenguaje

Existen tres elementos principales en cualquier lenguaje. Estos pueden ser trasladados al mundo de la programación.

### Sintaxis

La **sintaxis** es la estructura, la forma de los programas. ¿Cómo se escribe un lenguaje? Los caracteres sueltos de un programa se *tokenizan* en una serie de *tokens*. Estos luego se *parsean* en un árbol de sintaxis.

La sintaxis de un lenguaje se suele definir en un lenguaje (declarativo) conocido como **Extended Backus-Naus Form (EBNF)**.

```EBNF
<digit> ::== 0|1|2|3|4|5|6|7|8|9
<int> ::== <digit>{<digit>}
```

### Semántica

La **semántica** es el significado de un elemento del lenguaje. ¿Cómo se ejecuta? No se implementan de igual forma los hilos de Go y los hilos de Java.

La semántica de un lenguaje debe ser simple, y debe permitirme entender el programa en cuanto a correctitud y complejidad.

Para definirla, utilizaremos el **Kernel Language Approach**. Es un conjunto mínimo de instrucciones intuitivas.

Estas deben ser fácil de razonar, con semántica formal. El resto de la sintaxis se podrá componer de este conjunto mínimo de instrucciones.

Estas instrucciones se extienden a un lenguaje práctico a través de: *syntatic sugar*; *linguistic abstraction*.

### Pragmática

La **pragmática** es el propósito del lenguaje. ¿Para qué propósitos es útil un lenguaje? ¿Para qué propósitos no lo es?.
