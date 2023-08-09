Una algoritmo recursivo es aquel que se llama a si mismo, hay distintos tipos de recursividad:

- Recursividad Directa
- Recursividad Indirecta
- Recursividad de Cola

La recursividad se puede aplicar para resolver problemas que son resolubles mediante una solución de una nueva instancia del mismo problema

## Recursividad Directa

El algoritmo de recursividad directa es aquel que se llama a si mismo, directamente. Una función recursiva debe cumplir con ciertas reglas para que funcione correctamente:

- Debe poseer una condición de corte
- Debe poseer una llamada recursiva

### Ámbito

El ámbito de una función es la región de memoria del *stack* a la que el puede acceder. Dentro del ámbito de una función se almacenan:

- Los argumentos que son pasados a la funcion
- Las variables declaradas en la funcion
- La línea a la que debe regresar una vez completada la ejecución.

## Recursividad Indirecta

El algoritmo de recursividad indirecta es aquel que no se llama a si mismo, sino que llama a otra función, la cual llama a la función original.

![[Algoritmos II/Attachments/Recursividad 1.png]]

Para lograr esto, en C se debe declarar la firma de las funciones de antemano, para que el compilador las detecte.

## Recursividad de Cola

La recursividad de cola es aquella que la ultima función que ejecuta es la llamada recursiva. De esta forma, se puede descartar la memoria almacenada al final de cada llamada, para optimizar mas el uso del stack.

```c
// Un ejemplo de un alguritmo factorial, recursivo de cola.

int factorial_rec (int n, int parcial)
{
	if(n == 0)
	{
		return parcial ;
	}
	return factorial_rec (n - 1 , parcial * n );
}

int factorial (int n)
{
	return factorial_rec (n, 1) ;
}
```

## Divide y Conquista

El método ***divide y conquista*** es una forma general no solo de solucionar problemas, sino también de diseñar algoritmos.

Esta compuesto por tres fases:

1. **Dividir:** el problema es un numero de sub-problemas, que sean instancias menores del mismo problema
2. **Conquistar:** los sub-problemas de modo tal que sean resueltos recursivamente, hasta que el tamaño del problema sea lo suficientemente pequeño como para que su solución sea simple (caso base)
3. **Combinar:** las soluciones obtenidas por cada sub-problema en la solución del problema original
