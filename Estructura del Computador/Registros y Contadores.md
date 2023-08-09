Los registros son bloques que permiten almacenar un dato y recuperarlo un tiempodespues. Para diseñarlos, utilizamos un Flip-Flop D para cada bit a almacenar

## Registros de Almacenamiento

Cada Flip-Flop D esta conectado a una entrada externa, el Flip-Flop D guarda el valor recibido al recibir un pulso de reloj

![[Registros y Contadores 1.png]]

Con cada ciclo de reloj la entrada de 4 bits es copiada en la salida.

En un microprocesador, se usan para presentar los operadores a la unidad y para guardar los resultados de las operaciones. Son extremadamente rapidos, pero son mas caros

## Registros de Desplazamiento

Los registros de desplazamiento periten multiplizar y dividir por potencias de $2$. Ademas, permiten convertir una entrada en serie a una entrada en paralelo.

Cada Flip-Flop D esta conectado con el siguiente, por lo que cada uno copia la entrada del Flip Flop anterior con un pulso de reloj.

### Carga de Datos en Serie

![[Registros y Contadores 2.png]]

Tiene una unica entrada, se debe esperar a que todos los datos esten cargados en el registro, a un pulso de reloj por vez.

### Carga de Datos en Paralelo

![[Registros y Contadores 3.png]]

Permite que todos los datos se carguen a la vez a partir de multiplexores, ademas, se puede utilizar la salida en serie para convertir una entrada de datos en paralelo a una entrada de datos en serie.

## Contadores

Los contadores se pueden diseñar con distintas compuertas. Cada Flip-Flop añade un bit mas que puede ser usado para contar.

Los contadores pueden ser tanto ascendentes como descendentes

### Definiciones

- **Modulo**: Cantidad de estados del contador. Se define como $2^n$, siendo $n$ la cantidad de FFs
- **Codigo de Cuenta**: Representa la combinacion de bits de cada estado
- **Secuencia**: Secuencia de Estados
	- **Secuencia Cerrada**: Termina el ultimo estado y vuelve al inicial
	- **Secuencia Prohibida:** Secuencia de estados prohibidos

### Sincronico vs Asincronico

El contador Sincronico tiene cada flip flop conectado con el reloj, por lo que todos los flip flops cambian a la vez. El retardo es menor porque todos los flip flops actuan a la vez. Ademas, tiene mas flexibilidad, ya que puedo customizar la logica de estados como quiera, a partir del diseño de compuertas

El contador Asincronico tiene cada la entrada de reloj de cada flipflop conectada con el flipflop anterior, por lo que el circuito se ejecuta en cadena. Solo puede contar en binario hasta cierto estado

### Diseño

1. Elijo el módulo de mi contador y el codigo de cuenta que necesito
2. Elijo el numero de FFs necesarios a partir del modulo
3. Elijo el tipo de FFs que quiero usar, cada uno tiene sus ventajas dependiendo del codigo de cuenta
4. A partir de una tabla de transiciones, diseño la logica de cada flipflop

### Tabla de Transiciones

La tabla de transiciones parte de la transicion de cada estado al siguiente, y a partir de ahi busca que entrada debe tener cada flip flop para que se cumpla.

Luego se diseño un circuito combinacional a partir de la funcion logica de cada entrada de flip flop y se diseña el circuito.
