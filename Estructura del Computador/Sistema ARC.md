Cualquier lenguaje de alto nivel es traducido a Assembly, para luego se ensamblado en codigo de maquina, lenguaje que la computadora puede entender (ceros y unos).

Cuando un programa se guarda, este se guarda en el disco rigido, pero al momento de ejecutarse, toda la informacion se guarda en la memoria ram, para poder ser accedida.

## Memoria Ram

La memoria ram forma una estructura de datos tipo tabla, cada renglon de la tabla es identificado con su direccion. Cada dato es agrupado fisicamente cada 1 byte.

Los procesadores tienen instrucciones para acceder simultaneamente a 1, 2, 4, o mas bytes (palabras).

Las palabras de mas de 1 byte es guardada como una serie de bytes.

### Orden de Guardado

Tenemos dos ordenes distintos, ambos igual de validos, mientras se respete a lo largo de todas las operaciones.

- **Little-Endian**

	Guarda el byte menos significativo en la dirección mas baja.

- **Big-Endian**

	Guarda el byte menos significativo en la dirección mas alta.

### Espacio Direccionable

El espacio direccionable es aquel que puede ser accedido mediante una direccion de memoria. Incluso si no es memoria lo que se encuentra alli.

El mapa del espacio direccionable representa la signacion dada al espacio de direcciones, este es especifico del sistema.

Los dispositivos de entrada y salida tambien se encuentran en el espacio direccionable, el procesador puede cargar y leer datos por esos canales de informacion.

## Arquitectura Arc

Acronimo: **(A Risc Computer)**

### Manejo de Memoria

La arquitectura ARC maneja datos de 32 bits, direccionables por byte. Contiene un espacio de direcciones de $2^{32}$, Con un orden de guardado **Big-Endian.**

El mapa de memoria esta especificado por el siguiente grafico:

![[Sistema ARC 1.png]]

La mitad de la memoria se utilizar para los dispositivos de entrada y salida, la otra mitad se utiliza para el sitema operativo *(2048bytes)* y para la memoria ram.

### Set de Instrucciones

Es un subconjunto de SPARC. El PSR (Program Status Register) guarda los flags de ALU.

Las instrucciones ocupan 4 bytes, tenemos 32 registros de 4 bytes.

Solo hay dos instrucciones que acceden a la memoria principal:

- Leer memoria a registro.
- Escribir desde registro a memoria.

Debido a esto, para operar con numeros debemos cargarlo a un registro, y a partir de ahi hacer las operaciones.

## Instrucciones Arc

![[Sistema ARC 2.png]]

Las operaciones que terminan en **cc** alteran el contenido de los flags luego de la operación.

La **bifurcacion** salta a una direccion de memoria si se cumple una condicion

El salto por igual verifica el flag cero.

## Registros Accesibles Al Programador

![[Sistema ARC 3.png]]

Los registros `%r` son de proposito general y se pueden utilizar libremente, excepto por algunas excepciones.

El registro **PSR** es el que guarda los flags, pero no podemos acceder a su valor, unicamente a traves de instrucciones.

El registro **PC** guarda la direccion de la instruccion siendo ejecutada.

El registro `%r14` es el stack pointer

El registro `%r15` es la direccion de retorno de procedimiento

El registro `%r0` siempre vale 0.

## Sintaxis

![[Sistema ARC 4.png]]

Distingue mayusculas de minusculas

Numeros por defecto en base 10

Si empieza con **0x** o finaliza on **h**, se trata de hexadecimal.

## Directivas del Ensamblador

![[Sistema ARC 5.png]]

Indican al ensamblador como procesar una seccion del programa

Las instrucciones son especificas de un procesador, las pseudo-instrucciones son especificas de un programa ensamblador

Algunas directivas generan informacion en la memoria

## Subrutinas

La instruccion `call` llama a la subrutina deseada, guarda la direccion de retorno en `%r15`. La instruccion `jmpl` indica la siguiente linea a ejecutar. Se utiliza para volver de una subrutina

### Macros

Una macro es una porcion de codigo que se ejecuta antes del ensamblado. En el proceso de expansion de macros, Sus nombres se intercambian por el codigo correspondiente, reemplazando con los parametros necesarios.

### Diferencias

Las macro se accede en tiempo de ensamblado por lo que es mas rapido. La subrutina es accedida por la instruccion `call` y termina con un `jmpl`, en tiempo de ejecucion

Los parametros de una macro son interpretados por el ensamblador mientras que los de una subrutina es accedida por memoria o registro

El codigo de maquina de una macro se repite tantas veces como se invoque. En el caso de la subrutina, el codigo se encuentar en un solo lugar y se referencia a el cuando se necesita.

## Codigos de Máquina

Las instrucciones son traducidas en codigo de maquina. Hay cinco formatos de instruccion.

![[Sistema ARC 6.png]]

## Modos de Direccionamientos

- **Inmediato**: La constante esta incluida en la instruccion
- **Por Registro**: El registro tiene el dato
- **Directo o Absoluto**: La direccion de memoria esta incluida en la instruccion
- **Indirecta**: Contiene la direccion de memoria donde esta el puntero al dato (poco usado, lento)
- **Indirecta por Registro**: El registro tiene el puntero al dato
- **Indexado por Registro**: Un registro da la direccion inicial, el otro un incremento.

## Modelos de Arquitectura

- **CISC: Complex Instruction Set Computer**

	Tiene mas instrucciones, pero las instrucciones son de tamaño variable y es mas lento. Como tiene instrucciones con acceso a memoria, utiliza menos registros.

	Utiliza el stack de forma inmersa, con instrucciones que acceden a el. La logica de encontrar instrucciones, decodificarlas, e interconexiones dentro del procesador es mas complicada.

- **RISC: Reduced Instruction Set Computer**

	Todas las instrucciones ocupan el mismo espacio y es mas rapido. Tiene mas registros disponibles ya que todo debe estar en ellos para operar. Para utilizar el stack, se debe hacer de forma manual. Su set de instrucciones es mas reducido, no contiene instrucciones redundantes

	Las opraciones aritmeticas son unicamente entre registros. Para acceder a memoria, solo se puede guardar y recuperar. Los dipositivos de entrada y salida estan mapeados en memoria.

	Esta arquitectura es mucho mas rapida y simple que la de una arquitectura CISC. Por el otro lado, se requiere un poco mas de trabajo por parte del programador.
