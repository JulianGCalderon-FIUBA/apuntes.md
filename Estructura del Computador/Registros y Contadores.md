---
title: Registros y Contadores
---

Los registros son bloques que permiten almacenar un dato y recuperarlo un tiempo después. Para diseñarlos, utilizamos un Flip-Flop D para cada bit a almacenar

## Registros de Almacenamiento

Cada Flip-Flop D está conectado a una entrada externa, el Flip-Flop D guarda el valor recibido al recibir un pulso de reloj

![[Registros y Contadores 1.png|500]]

Con cada ciclo de reloj, la entrada de 4 bits es copiada en la salida.

En un microprocesador, se usan para presentar los operadores a la unidad y para guardar los resultados de las operaciones. Son extremadamente rápidos, pero son más caros

## Registros de Desplazamiento

Los registros de desplazamiento permiten multiplicar y dividir por potencias de $2$. Además, permiten convertir una entrada en serie a una entrada en paralelo.

Cada Flip-Flop D está conectado con el siguiente, por lo que cada uno copia la entrada del Flip-Flop anterior con un pulso de reloj.

### Carga de Datos en Serie

![[Registros y Contadores 2.png|500]]

Tiene una única entrada, se debe esperar a que todos los datos estén cargados en el registro, a un pulso de reloj por vez.

### Carga de Datos en Paralelo

![[Registros y Contadores 3.png|475]]

Permite que todos los datos se carguen a la vez a partir de multiplexores, además, se puede utilizar la salida en serie para convertir una entrada de datos en paralelo a una entrada de datos en serie.

## Contadores

Los contadores se pueden diseñar con distintas compuertas. Cada Flip-Flop añade un bit más que puede ser usado para contar.

Los contadores pueden ser tanto ascendentes como descendentes

### Definiciones

- **Módulo**: Cantidad de estados del contador. Se define como $2^n$, siendo $n$ la cantidad de Flip-Flops
- **Código de Cuenta**: Representa la combinación de bits de cada estado
- **Secuencia**: Secuencia de Estados
	- **Secuencia Cerrada**: Termina el último estado y vuelve al inicial
	- **Secuencia Prohibida:** Secuencia de estados prohibidos

### Sincrónico vs. Asincrónico

El contador Sincrónico tiene cada Flip-Flop conectado con el reloj, por lo que todos los Flip-Flops cambian a la vez. El retardo es menor porque todos los Flip-Flops actúan a la vez. Además, tiene más flexibilidad, ya que puedo customizar la lógica de estados como quiera, a partir del diseño de compuertas

El contador asincrónico tiene cada la entrada de reloj de cada Flip-Flop conectada con el Flip-Flop anterior, por lo que el circuito se ejecuta en cadena. Solo puede contar en binario hasta cierto estado

### Diseño

1. Elijo el módulo de mi contador y el código de cuenta que necesito
2. Elijo el número de Flip-Flops necesarios a partir del módulo
3. Elijo el tipo de Flip-Flops que quiero usar, cada uno tiene sus ventajas dependiendo del código de cuenta
4. A partir de una tabla de transiciones, diseño la lógica de cada Flip-Flop

### Tabla de Transiciones

La tabla de transiciones parte de la transición de cada estado al siguiente, y a partir de ahí busca que entrada debe tener cada Flip-Flop para que se cumpla.

Luego se diseñó un circuito combinacional a partir de la función lógica de cada entrada de Flip-Flop y se diseña el circuito.
