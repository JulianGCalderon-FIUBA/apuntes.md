---
title: Simplificación de Funciones
---

## Simplificación Algebraica

Para simplificar un circuito, aplicamos los teoremas del álgebra de Boole para eliminar la mayor cantidad de términos que sea posible.

1. Sacar negaciones, de externa a interna, a partir de las leyes de Morgan
2. A partir del postulado de Huntington P5, factorizar y eliminar términos redundantes.

## Mapa de Karnaugh

El mapa de Karnaugh consiste en hacer una tabla de doble entrada, donde separamos variables. Marcamos en la tabla para que valores la función binaria devuelve un $1$.

![[Simplificacion de Funciones 1.png|475]]

A partir de los valores de esta tabla, podemos simplificar términos. Consiste en agrupar minitérminos y representarlos con un único termino. Notemos que este método únicamente aplica el postulado P5 de Huntington.

### Definiciones

- **Adyacencias**: Dos elementos son vecinos si solo cambia una variable entre ambos elementos, se piensa el mapa como un cilindro.
- **Implicante Primo**: Mayor agrupación posible para un grupo de elementos
- **Implicante Primo Esencial.** Implicante primo que no puedo omitir

### Algoritmo

1. Marcar implicantes primos
2. Marcar implicantes primos esenciales
3. Construir expresión algebraica

> [!note]
> Los mapas de Karnaugh de 5 variables se pueden pensar como dos mapas de Karnaugh, con una variable cambiada. Los homólogos en la posición son vecinos.
