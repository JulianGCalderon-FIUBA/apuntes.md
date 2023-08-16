La tarea principal de una computadora es la de ejecutar un algoritmo, para esto utiliza operaciones muy sencillas de forma ordenada. Estas operaciones sencillas se pueden utilizar en conjunto para resolver problemas complejos.

## Arquitectura Harvard

![[Micro Arquitectura 1.png|500]]

Este modelo corresponde a la arquitectura de las primeras computadoras, sin embargo, tiene un problema. Estas computadoras no son fácilmente programables, por lo que no pueden resolver todos los problemas.

Se utiliza para dispositivos automáticos que no requieren programación. Tiene pequeño volumen de memoria de datos y de programa

## Arquitectura von Neumann

![[Micro Arquitectura 2.png|500]]

En este modelo, se unifica el almacenamiento de datos con las instrucciones, lo que permite cargar fácilmente un programa en memoria y ejecutarlo.

Es más versátil, lo que permite resolver una variedad de problemas.

## Problema del Conexionado

Cuando quiero conectar muchos dispositivos, no pueden estar todos conectados con la CPU directamente. Para resolver esto, se utilizan buses.

Lo más común es la utilización de tres líneas:

- **Línea de Datos:** Por aquí se envían los datos
- **Línea de Direcciones:** Por aquí se envía la dirección con la que se está comunicando la CPU
- **Línea de Control:** Por aquí índica si los datos son de entrada o de salida

De esta forma, todos los dispositivos se comunican con el procesador a través del Bus

Este sistema de buses permite conectar componente de una computadora, así como varias computadoras entre sí. Los componentes electrónicos dentro de un procesador también interactúan con el bus.

![[Micro Arquitectura 3.png]]

En este sistema, los dispositivos de entrada y salida están mapeados en memoria. En caso de no ser así, se deberá usar un bus distinto para comunicarse con ellos.

## Arquitectura del Microprocesador

Para ejecutar un programa, el microprocesador realiza el llamado **Ciclo Fetch**, o ciclo de búsqueda-ejecución.

1. Buscar en memoria la próxima instrucción a ser ejecutada
2. Decodificar el código de operación de esa instrucción
3. Ejecutar la instrucción
4. Repetir

Hay distintas formas de implementar este ciclo de búsqueda, y estas varían en la velocidad o el consumo del mismo.

### Unidad de Datos

La unidad de datos es la parte del procesador que se encarga de realizar las operaciones y guardar los registros. Para realizar esto utiliza tres buses. Se puede realizar con menos buses, pero son soluciones más lentas, ya que requiere más ciclos de reloj para guardar los datos a usar en registros correspondientes, para luego ser usados.

![[Micro Arquitectura 4.png|527]]

- **Bus A:** Está conectado con la salida de los registros y con la primera entrada de la ALU. Además, está conectado con la línea de direcciones.
- **Bus B:** Está conectado con la salida de los registros y con la segunda entrada de la ALU. Además, está conectado con la línea de datos.
- **Bus C**: Está conectado con la entrada de los registros.

Para operar con los registros, se utilizan tres decodificadores:

- **Decodificador A:** Decide cuál registro enviará sus datos por el bus A
- **Decodificador B:** Decide cuál registro enviará sus datos por el bus B
- **Decodificador C:** Decide en cuál registro se guardará la información del bus C

Para decidir esto, se utiliza el **tri-state buffer,** este utiliza una resistencia muy alta para no permitir que la información salga de los registros no necesarios, solo habilitando el registro buscado.

Además de los registros utilizados por el programador, el microprocesador tiene más registros que son utilizados por el mismo para realizar operaciones.

- **Registros Temporales:** En estos registros se guardará información adicional que necesite el microprocesador.
- **Registro IR:** En este registro se cargará la instrucción que se debe ejecutar

La unidad de control contiene también el multiplexor del bus C. Este define si debe leer la información proveniente de la ALU o de la línea de datos.

No todos los registros se implementan de la misma forma, hay algunos con características especiales:

- **Registro %r0**: Este registro no necesita Flip-Flops, ya que siempre vale 0.
- **Registro PC:** Los últimos dos bits valen siempre 0, por lo que no necesita Flip-Flops allí.
- **Registro IR:** Tiene salidas especiales para cada campo, tiene comunicación bit a bit. Esto permite analizar la instrucción a ejecutar.

#### ALU

Para implementar las operaciones, utiliza dos componentes:

- **Look-Up Table**: Esta tabla contiene la tabla de verdad de cada operación. Se opera de a un bit por vez, llevando el carry para la próxima operación.
- **Barrel-Shifter:** Este componente permite desplazar bits a izquierda o derecha en un solo ciclo de reloj, a diferencia de un registro de desplazamiento.

> [!note]
> En la tabla no estan todas las operaciones, la operacion *subcc* por ejemplo se puede realizar con un complemento y un suma. De esto se encarga la unidad de control.

La ALU calcula los flags de cada operación y los carga en el registro **PSR** en cada de ser necesario.

### Unidad de Control

Hay dos formas de implementarla, con lógica micro-programada o con lógica cableada. El diseño cableado puede ser más difícil de diseñar y de modificar. El microprograma se puede grabar, mientras que el diseño cableado debe cambiar completamente. Sin embargo, es un método más rápido. Nos vamos a centrar en diseño micro-programado

![[Micro Arquitectura 5.png|500]]

Diagrama completo de la unidad de control.

Para diseñarlo, se utilizan contadores que permiten indicar en que estado nos encontramos

- **ROM**. Esta contiene 2048 instrucciones, de 41 bits cada una. Acá está programada la lógica de cada instrucción del sistema
- **MIR:** Acá se almacenan las instrucciones de la ROM que deben ser ejecutadas
- **CS-Addres-MUX:** Envía la dirección a ejecutar dependiendo de su entrada de control.

	Está conectado con el CSAT, con los códigos de operación de la instrucción almacenada en IR, y con la dirección de salto de la MIR.

	A partir de una entrada de control proveniente del CBL, decide que entrada tomar y envía al decodificador.

- **Decodificador:** Permite habilitar únicamente la instrucción deseada de la ROM, para ser copiada en el MIR.
- **CSAT:** Es el contador de instrucciones, indica cuál es la siguiente instrucción en la ROM
- **CBL:** Está conectado con los flags y los códigos de condición y el bit 13 del registro IR. Decide que tipo de salto se debe realizar y lo envía al CS-Address-MUX.
- **MUX A, B, C:** Estos tres multiplexores deciden si tomar el registro indicado por el MIR o por el IR, dependiendo de los correspondientes bits en el MIR.

Como la lectura de memoria puede ser más lenta, se utiliza el **ACK** *(Acknowledge),* por este canal se envía un 1 una vez que termino la operación en memoria. Permite indicarle a la unidad de control que puede seguir con la próxima instrucción.

#### Formato de Instrucciones MIR

![[Micro Arquitectura 6.png]]

Cada parte de la MIR tiene un propósito distinto:

- **A:** Contiene la información que debe ser enviada por el bus A en caso de ser necesario
- **Amux:** Contiene un 1 si la información de A debe ser cargada en el bus A
- **B:** Contiene la información que debe ser enviada por el bus B en cado de ser necesario
- **Bmux:** Contiene un 1 si la información de B debe ser cargada en el bus B
- **C:** Contiene la información que debe ser enviada por el bus A en cado de ser necesario
- **Cmux:** Contiene un 1 si la información de C debe ser cargada en el bus C
- **RD:** Contiene un 1 si la instrucción es de lectura de la memoria
- **WR:** Contiene un 1 si la instrucción es de escritura en memoria
- **ALU:** Contiene el código de la instrucción de la ALU a ser ejecutada. Si no se necesita ninguna instrucción se realiza alguna que no altere flags
- **COND:** Indica el tipo de salto que debe hacer luego de realizar la instrucción
- **JUMP ADDR:** Indica la dirección a la cual saltar en caso de que la condición lo indique

La instrucción **DECODE** lee la instrucción del registro IR y determina la instrucción de la ROM que se debe ejecutar.

Para obtener que instrucción de la ROM se debe realizar, se utiliza el **OP**, seguido del OP3. Con un total de 8 bits. Como las instrucciones están en 11 bits. El primer bit siempre vale 1, mientras que los últimos dos bits siempre están en 0.

Para las instrucciones de Assembly que no contienen **OP3**, se le asigna a toda instrucción posible un mismo microcódigo, delegándole al mismo identificar cuál operación es. Por ejemplo: *branches, sethi, call*.

Para no repetir el microcódigo en cada instrucción, se puede utilizar la **nanoprogramación.** Consiste en remplazar la tabla de *2048 words x 41 bits* por una tabla de *2048 words x 7 bits*, donde se redirige a una nueva tabla de *100 words x 41 bits*, la cual contiene el microcódigo para cada operación.

#### Tablas de Operaciones

Los códigos de condición son los siguientes

![[Micro Arquitectura 7.png|375]]

Códigos de la ALU son los siguientes

![[Micro Arquitectura 8.png]]
