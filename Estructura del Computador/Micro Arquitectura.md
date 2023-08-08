La tarea principal de una computadora es la de ejecutar un algoritmo, para esto utiliza operaciones muy sencillas de forma ordenada. Estas operaciones sencillas se pueden utilizar en conjunto para resolver problemas complejos.

# Arquitectura Harvard

![[Micro Arquitectura 1.png|Untitled]]

Este modelo corresponde a la arquitectura de las primeras computadoras, sin embargo tiene un problema. Estas computadoras no son facilmente programables, por lo que no pueden resolver todos los problemas.

Se utiliza para dispositivos automaticos que no requieren programacion. Tiene pequeño volumen de memoria dedatos y de programa

# Arquitectura von Neumann

![[Micro Arquitectura 2.png|Untitled]]

En este modelo, se unifica el almacenamiento de datos con las instrucciones, lo que permite cargar facilmente un programa en memoria y ejecutarlo.

Es mas versatil lo que permite resolver una variedad de problemas.

# Problema del Conexionado

Cuando quiero conectar muchos dispositivos, no pueden estar todos conectados con el CPU directamente. Para resolver esto, se utilizan buses.

Lo mas comun es la utilizacion de tres lineas:

- **Linea de Datos:** Por aqui se envian los datos
- **Linea de Direcciones:** Por aqui se envia la direccion con la que se esta comunicando el CPU
- **Linea de Control:** Por aqui indica si los datos son de entrada o de salida

De esta forma, todos los dispositivos se comunican con el procesador a traves del Bus

Este sistema de buses permite conectar componente de una computadora, asi como varias computadoras entre si. Los componentes electronicos dentro de un procesador tambien interactuan con el bus.

![[Micro Arquitectura 3.png|Untitled]]

En este sistema, los dipositivos de entrada y salida estan mapeados en memoria. En caso de no ser asi, se debera usar un bus distinto para comunicarse con ellos.

# Arquitectura del Microprocesador

Para ejecutar un programa, el micropocesador realiza el llamado **Ciclo Fetch**, o ciclo de busqueda-ejecución.

1. Buscar en memoría la próxima instrucción a ser ejecutada
2. Decodificar el código de operación de esa instrucción
3. Ejecutar la instrucción
4. Repetir

Hay distintas formas de implementar este ciclo de busqueda, y estas varian en la velocidad o el consumo del mismo.

## Unidad de Datos

La unidad de datos es la parte del procesador que se encarga de realizar las operaciones y guardar los registros. Para realizar esto utiliza tres buses. Se puede realizar con menos buses, pero son soluciones mas lentas, ya que requiere mas ciclos de reloj para guardar los datos a usar en registros correspondientes, para luego ser usados.

![[Micro Arquitectura 4.png|Untitled]]

- **Bus A:** Esta conectado con la salida de los registros y con la primer entrada de la ALU. Ademas, esta conectado con la linea de direcciones.
- **Bus B:** Esta conectado con la salida de los registros y con la segunda entrada de la ALU. Ademas, esta conectado con la linea de datos.
- **Bus C**: Esta conectado con la entrada de los registros.

Para operar con los registros, se utilizan tres decodificadores:

- **Decodificador A:** Decide cual registro enviara sus datos por el bus A
- **Decodificador B:** Decide cual registro enviara sus datos por el bus B
- **Decodificador C:** Decide en cual registro se guardara la informacion del bus C

Para decidir esto, se utiliza el **tri-state buffer,** este utiliza una resistencia muy alta para no permitir que la informacion salga de los registros no necesarios, solo habilitando el registro buscado.

Ademas de los registros utilizados por el programador, el microprocesador tiene mas registros que son utilizados por el mismo para realizar operaciones.

- **Registros Temporales:** En estos registros se guardara informacion adicional que necesite el microporcesador.
- **Registro IR:** En este registro se cargara la instrucción que se debe ejecutar

La unidad de control contiene tambien el multiplexor del bus C. Este define si debe leer la información proveniente de la ALU o de la linea de datos.

No todos los registros se implementan de la misma forma, hay algunos con caracteristicas especiales:

- **Registro %r0**: Este registro no necesita flip-flops ya que siempre vale 0.
- **Registro PC:** Los ultimos dos bits valen siempre 0, por lo que no necesita flip flops alli.
- **Registro IR:** Tiene salidas especiales para cada campo, tiene comunicacion bit a bit. Esto permite analizar la instruccion a ejecutar.

### ALU

Para implementar las operaciones, utiliza dos componentes:

- **Look-Up Table**: Esta tabla contiene la tabla de verdad de cada operación. Se opera de a un bit por vez, llevando el carry para la proxima operación.
- **Barrel-Shifter:** Este componente permite desplazar bits a izquierda o derecha en un solo ciclo de reloj, a diferencia de un registro de desplazamiento.

> [!note]
> En la tabla no estan todas las operaciones, la operacion subcc por ejemplo se puede realizar con un complemento y un suma. De esto se encarga la unidad de control.


La ALU calcula los flags de cada operación y los carga en el registro **PSR** en cada de ser necesario.

## Unidad de Control

Hay dos formas de implementarla, con logica micro-programada o con logica cableada. El diseño cableado puede ser mas dificil de diseñar y de modificar. El micro-programa se puede grabar mientras que el diseño cableado debe cambiar completamente. Sin embargo, es un método mas rápido. Nos vamos a centrar en diseño micro-programado

![[Micro Arquitectura 5.png|Diagrama completo de la unidad de control.]]

Diagrama completo de la unidad de control.

Para diseñarlo, se utilizan contadores que permiten indicar en que estado nos encontramos

- **ROM**. Esta contiene 2048 instrucciones, de 41 bits cada una. Aca esta programada la logica de cada instrucción del sistema
- **MIR:** Aca se almacenan la instrucciones de la ROM que deben ser ejecutadas
- **CS-Addres-MUX:** Envia la direccion a ejecutar dependiendo de su entrada de control.
    
    Esta conectado con el CSAT, con los codigos de operacion de la instruccion almacenada en IR, y con la direccion de salto de la MIR.
    
    A partir de una entrada de control proveniente de el CBL, decide que entrada tomar y envia al decodificador.
    
- **Decodificador:** Permite habilitar unicamente la instruccion deseada de la ROM, para ser copiada en el MIR.
- **CSAT:** Es el contador de instrucciones, indica cual es la siguiente instruccion en la ROM
- **CBL:** Esta conectado con los flags y los codigos de condicion y el bit 13 del registro IR. Decide que tipo de salto se debe realizar y lo envia al CS-Address-MUX.
- **MUX A, B, C:** Estos tres multiplexores deciden si tomar el registro indicado por el MIR o por el IR, dependiendo de los correspondientes bits en el MIR.

Como la lectura de memoria puede ser mas lenta, se utiliza el **ACK (Acknowledge)**, por este canal se envia un 1 una vez que termino la operacion en memoria. Permite indicarle a la unidad de control que puede seguir con la proxima instruccion.

### Formato de Instrucciones MIR

![[Micro Arquitectura 6.png|Untitled]]

Cada parte de la MIR tiene un proposito distinto:

- **A:** Contiene la informacion que debe ser enviada por el bus A en caso de ser necesario
- **Amux:** Contiene un 1 si la información de A debe ser cargada en el bus A
- **B:** Contiene la informacion que debe ser enviada por el bus B en cado de ser necesario
- **Bmux:** Contiene un 1 si la información de B debe ser cargada en el bus B
- **C:** Contiene la informacion que debe ser enviada por el bus A en cado de ser necesario
- **Cmux:** Contiene un 1 si la información de C debe ser cargada en el bus C
- **RD:** Contiene un 1 si la instruccion es de lectura de la memoria
- **WR:** Contiene un 1 si la instruccion es de escritura en memoria
- **ALU:** Contiene el codigo de la instrucción de la ALU a ser ejecutada. Si no se necesita ninguna instruccion se realiza alguna que no altere flags
- **COND:** Indica el tipo de salto que debe hacer luego de realizar la instruccion
- **JUMP ADDR:** Indica la direccion a la cual saltar en caso de que la condicion lo indique

La instrucción **DECODE** lee la instruccion del registro IR y determina la instruccion de la ROM que se debe ejecutar.

Para obtener que instruccion de la ROM se debe realizar, se utiliza el OP, seguido del OP3. Con un total de 8 bits. Como las instrucciones estan en 11 bits. El primer bit siempre vale 1, mientras que los ultimos dos bits siempre estan en 0.

Para las instrucciones de assembly que no contienen ***OP3, se le asigna a toda instruccion posible un mismo microcodigo, delegandole al mismo identificar cual operacion es. Por ejemplo, branches, sethi, call.

Para no repetir el microcodigo en cada instrucciones, se puede utilizar la **nanoprogramación.** Consiste en remplazar la tabla de *2048wordsx41bits* por una tabla de *2048wordsx7bits*, donde se redirige a una nueva tabla de *100wordsx41bits*, la cual contiene el microcodigo para cada operación.

### **Tablas de Operaciones**

![[Micro Arquitectura 7.png|Codigos de Condicion]]

Codigos de Condicion

![[Micro Arquitectura 8.png|Codigos de la ALU]]

Codigos de la ALU