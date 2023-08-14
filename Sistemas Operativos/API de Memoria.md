Cuando corremos un programa en C, hay dos tipos de memoria que reservamos. La primera es llamada ***stack***, esta memoria se maneja automáticamente por el compilador, al utilizar variables y llamar a funciones. A veces es llamada memoria ***automática.***

Esta memoria no tiene larga duración, sólo dura durante el contexto en el que fue declarada. Muchas veces necesitamos memoria que viva más allá de este contexto, en estas situaciones necesitamos el segundo tipo de memoria, el ***heap.***

Las asignaciones y des asignaciones de memoria en esta parte se realizan de forma automática, nosotros como programadores debemos reservar y liberar esta memoria cuando sea necesario. Esta memoria nos permite utilizar una variable afuera del ambiente en el que fue declarada, lo cual muchas veces es totalmente necesario.

Esta memoria suele tener más capacidad que el stack, por lo que para estructuras grandes y de tamaño indefinido, debemos utilizar el ***stack***.

## malloc()

Es una función de la biblioteca estándar que nos reserva memoria del tamaño requerido, y nos devuelve un puntero a esta posición. Para reservar la memoria que necesitamos, utilizamos el operador `sizeof`, que resuelve los tamaños en tiempo de compilación. Muchas veces. no reserva exactamente la memoria que pedís, sino que un poco más.

## free()

Junto con ***malloc***, tendremos ***free***. Estas dos funciones están fuertemente conectadas, la memoria reservará por *malloc* debe ser liberada por *free*. Estas dos funciones utilizan las mismas estructuras para poder comunicarse entre si y liberar correctamente la memoria.

Esta función sólo funciona correctamente si le pasamos punteros a memoria previamente reservada por *malloc*, como indican las ***man pages***.

## garbage collector

En lenguajes de programación modernos, tendremos mecanismos que se encargaran de manejar la memoria dinámica de forma simple, sin que nosotros nos tengamos que preocupar por la misma.

## uninitialized read

Cuando reservamos memoria, no se inicializa con algún valor, por lo que decimos que se inicializa con ***basura***. Información que no tiene ningún valor significativo para nosotros, si no que son residuos de otro proceso del sistema operativo.

## memory leak

Cuando nos olvidamos de liberar memoria en un programa largo, esto es un gran problema. Olvidarse de liberar memoria implica que eventualmente nos podremos quedar sin, lentamente perdiendo memoria. Este problema se mantiene en lenguajes con ***garbage collector***, ya que referencias a memoria no utilizada no son liberadas.

## dangling pointer

Ocurre cuando liberamos memoria antes de que terminemos de utilizarla, en estos casos tendremos un *dangling pointer*, un puntero suelto. Esto puede terminar nuestro programa o encontrarse con comportamiento indefinido.

## double free

Muchas veces nos confundimos y liberamos dos veces el mismo puntero, esto puede llevar a errores y tiene un comportamiento indefinido.

## system calls

Estas funciones mencionadas pertenecen a la biblioteca estándar de C, pero se construyen a partir de system calls

Una de ellas es ***brk***, la cual se utiliza para aumentar el tamaño del heap de nuestro programa.

Otra system call útil es ***mmap***, se puede utilizar para reservar una región de memoria anónima dentro de tu programa.
