Cualquier lenguaje de alto nivel es traducido a Assembly, para luego se ensambla en código de máquina, lenguaje que la computadora puede entender (ceros y unos).

Cuando un programa se guarda, este se guarda en el disco rígido, pero al momento de ejecutarse, toda la información se guarda en la memoria RAM, para poder ser accedida.

## Memoria RAM

La memoria RAM forma una estructura de datos tipo tabla, cada renglón de la tabla es identificado con su dirección. Cada dato es agrupado físicamente cada 1 byte.

Los procesadores tienen instrucciones para acceder simultáneamente a 1, 2, 4, o más bytes (palabras).

Las palabras de más de 1 byte es guardada como una serie de bytes.

### Orden de Guardado

Tenemos dos órdenes distintos, ambos igual de válidos, mientras se respete a lo largo de todas las operaciones.

- **Little-Endian**: Guarda el byte menos significativo en la dirección más baja.
- **Big-Endian**: Guarda el byte menos significativo en la dirección más alta.

### Espacio Direccionable

El espacio direccionable es aquel que puede ser accedido mediante una dirección de memoria. Incluso si no es memoria lo que se encuentra allí.

El mapa del espacio direccionable representa la asignación dada al espacio de direcciones, este es específico del sistema.

Los dispositivos de entrada y salida también se encuentran en el espacio direccionable, el procesador puede cargar y leer datos por esos canales de información.

## Arquitectura ARC

Es un acronimo de "A Risc Computer"

### Manejo de Memoria

La arquitectura ARC maneja datos de 32 bits, direccionables por byte. Contiene un espacio de direcciones de $2^{32}$, Con un orden de guardado **Big-Endian.**

El mapa de memoria está especificado por el siguiente gráfico:

![[Sistema ARC 1.png]]

La mitad de la memoria se utiliza para los dispositivos de entrada y salida, la otra mitad se utiliza para el sistema operativo *(2048 bytes)* y para la memoria RAM.

### Set de Instrucciones

Es un subconjunto de SPARC. El PSR *(Program Status Register)* guarda los flags de ALU.

Las instrucciones ocupan 4 bytes, tenemos 32 registros de 4 bytes.

Solo hay dos instrucciones que acceden a la memoria principal:

- Leer memoria a registro.
- Escribir desde registro a memoria.

Debido a esto, para operar con números debemos cargarlo a un registro, y a partir de ahí hacer las operaciones.

## Instrucciones ARC

![[Sistema ARC 2.png|475]]

- Las operaciones que terminan en **cc** alteran el contenido de los flags luego de la operación.
- La **bifurcación** salta a una dirección de memoria si se cumple una condición
- El salto por igual verifica el flag cero.

## Registros accesibles al Programador

![[Sistema ARC 3.png|475]]

- Los registros `%r` son de propósito general y se pueden utilizar libremente, excepto por algunas excepciones.
- El registro **PSR** es el que guarda los flags, pero no podemos acceder a su valor, únicamente a través de instrucciones.
- El registro **PC** guarda la dirección de la instrucción siendo ejecutada.
- El registro `%r14` es el stack pointer
- El registro `%r15` es la dirección de retorno de procedimiento
- El registro `%r0` siempre vale 0.

## Sintaxis

![[Sistema ARC 4.png|475]]

- Distingue mayúsculas de minúsculas
- Números por defecto en base 10
- Si empieza con **0x** o finaliza con **h**, se trata de hexadecimal.

## Directivas del Ensamblador

![[Sistema ARC 5.png|475]]

- Indican al ensamblador como procesar una sección del programa
- Las instrucciones son específicas de un procesador, las pseudo-instrucciones son específicas de un programa ensamblador
- Algunas directivas generan información en la memoria

## Subrutinas

La instrucción `call` llama a la subrutina deseada, guarda la dirección de retorno en `%r15`. La instrucción `jmpl` índica la siguiente línea a ejecutar. Se utiliza para volver de una subrutina

### Macros

Una macro es una porción de código que se ejecuta antes del ensamblado. En el proceso de expansión de macros, Sus nombres se intercambian por el código correspondiente, reemplazando con los parámetros necesarios.

### Diferencias

Las macro se accede en tiempo de ensamblado, por lo que es más rápido. La subrutina es accedida por la instrucción `call` y termina con un `jmpl`, en tiempo de ejecución

Los parámetros de una macro son interpretados por el ensamblador, mientras que los de una subrutina es accedida por memoria o registro

El código de máquina de una macro se repite tantas veces como se invoque. En el caso de la subrutina, el código se encuentra en un solo lugar y se referencia a él cuándo se necesita.

## Códigos de Máquina

Las instrucciones son traducidas en código de máquina. Hay cinco formatos de instrucción.

![[Sistema ARC 6.png|475]]

## Modos de Direccionamientos

- **Inmediato**: La constante está incluida en la instrucción
- **Por Registro**: El registro tiene el dato
- **Directo o Absoluto**: La dirección de memoria está incluida en la instrucción
- **Indirecta**: Contiene la dirección de memoria donde está el puntero al dato (poco usado, lento)
- **Indirecta por Registro**: El registro tiene el puntero al dato
- **Indexado por Registro**: Un registro da la dirección inicial, el otro un incremento.

## Modelos de Arquitectura

### CISC: Complex Instruction Set Computer

Tiene más instrucciones, pero las instrucciones son de tamaño variable y es más lento. Como tiene instrucciones con acceso a memoria, utiliza menos registros.

Utiliza el stack de forma inmersa, con instrucciones que acceden a él. La lógica de encontrar instrucciones, decodificarlas, e interconexiones dentro del procesador es más complicada.

### RISC: Reduced Instruction Set Computer

Todas las instrucciones ocupan el mismo espacio y es más rápido. Tiene más registros disponibles, ya que todo debe estar en ellos para operar. Para utilizar el stack, se debe hacer de forma manual. Su set de instrucciones es más reducido, no contiene instrucciones redundantes

Las operaciones aritméticas son únicamente entre registros. Para acceder a memoria, solo se puede guardar y recuperar. Los dispositivos de entrada y salida están mapeados en memoria.

Esta arquitectura es mucho más rápida y simple que la de una arquitectura CISC. Por el otro lado, se requiere un poco más de trabajo por parte del programador.
