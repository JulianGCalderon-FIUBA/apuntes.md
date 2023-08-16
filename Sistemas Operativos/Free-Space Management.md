---
title: Free-Space Management
---

El manejo del espacio libre puede ser fácil cuando utilizamos paginación, ya que estamos lidiando con páginas de tamaño fijo. Donde el manejo se vuelve difícil, es cuando tratamos con memoria del usuario, donde la memoria tiene tamaño variable.

Hay dos problemas a resolver cuando tratamos con este manejo:

- ***Fragmentation Externa:*** Ocurre cuando el espacio libre es separado en pequeños fragmentos de distintos tamaños, esto puede ocasionar que no tengamos la memoria que necesitamos de forma contigua.
- ***Fragmentación Interna:*** Ocurre cuando el le damos mas memoria al usuario de la que necesita, por lo que tendrá memoria sin utilizar.

Nos centraremos en el primer problema por simplificación, y debido a que su análisis es más interesante.

Cuando le entregamos una región de memoria a un usuario, esta no puede ser movida, le corresponde totalmente al usuario. No podemos compactar el espacio como hacíamos con el sistema operativo.

Para manejar el tamaño de las regiones entregadas al usuario, la mayoría de los ***allocators*** utilizan los llamados ***headers***. Reservan un poco de memoria extra justo antes de la región para guardar información útil sobre la misma, metadata. Tanto ***malloc*** como ***free*** utilizan estos headers como lenguaje común para operar.

## Mecanismos de Bajo Nivel

Antes de investigar sobre las políticas del manejo de memoria, hay algunos mecanismos útiles que nos permitirán mejorar estas problemáticas.

- ***Splitting:*** Si tenemos una región más grande de lo que el usuario pidió, entonces esta se puede partir en dos, dándole al usuario la región justa. Esto previene fragmentación interna.
- ***Coalescing:*** Cuando liberamos una región, debemos unirla con las regiones libres contiguas para mejorar la fragmentación externa.

## Crecimiento del Heap

Cuando nos quedamos sin regiones libres del tamaño necesario para entregarle al usuario, debemos pedirle al sistema operativo más memoria. Las *system calls* ***sbrk*** y ***mmap*** cumplen este propósito. Al aumentar el tamaño del ***heap,*** tendremos más memoria disponible y podemos dársela al usuario.

## Estrategias de Búsqueda

Hay numerosas estrategias para encontrar la mejor región para darle al usuario.

La estrategia ***best fit*** consiste en iterar la lista de regiones libres, dándole al usuario la menor región que cumple con el pedido. De esta forma, evitamos realizar splitting ***de las regiones grandes.

Por otro lado tenemos ***worst fit***. En contraste con la anterior, le entregamos al usuario la región más grande disponible (realizando splitting). La idea de esto es evitar tener muchos bloques pequeños como tendríamos con el enfoque anterior, dejando bloques grandes.

Un enfoque más simple es ***first fit***.* Simplemente devuelve la primer región que encuentra, la ventaja de este enfoque es su simpleza y velocidad. Este enfoque depende de como el ***allocator*** maneja la lista de bloques libres. Si utilizamos un ordenamiento ***address-based***, entonces la implementación será fácil y reducirá fragmentación.

Existen algunas estrategias más complejas para lidiar con estos problemas.

El enfoque de s***egregated lists*** consiste en tener algunas lista para manejar objetos de cierto tamaño, y otra lista de propósito general. Al tener un bloque dedicado a ***requests*** de un tamaño particular, la fragmentación no es un problema.

Así como ventajas, este enfoque introduce nuevas problemáticas ¿Cuanta memoria le dedicamos a cada lista particular? Una buena forma de solucionarlo consiste en pedirle mas memoria al ***allocator*** de propósito general cuando una de nuestras listas segregadas se queda sin memoria

Otro enfoque interesante es el de ***buddy allocator***. Este enfoque es bueno para mejorar el proceso de ***coalescing,*** haciéndolo más simple.

Cuando se requiere memoria, la búsqueda de un espacio libre divide el espacio libre en dos hasta encontrar un bloque con el tamaño justo deseado. Este enfoque solo puede entregar bloques en potencias de dos, por lo que puede sufrir fragmentación interna.

Cuando si libera un bloque, se revisa si el *buddy* (bloque vecino) está libre, en ese caso se realiza *coalescing* y se repite la lógica.

El problema principal de estas técnicas es su escalabilidad, los ***allocators*** complejos utilizan estructuras avanzadas para lidiar con este problema.
