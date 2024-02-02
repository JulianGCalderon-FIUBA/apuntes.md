La **memoria** es un conjunto de celdas distribuidas linealmente, y cada una tiene una única dirección de memoria

Un `puntero` es una variable que apunta a una dirección de memoria, lo que permite modificarla desde cualquier lugar del código.

- `&`: Devuelve la dirección en la que se encuentra una variable.
- `*`: Devuelve el valor al que apunta un puntero

```c
void duplicar(int *numero){
	*numero = (*numero) * (*numero);
}

int numero = 3;
duplicar(&numero);

printf("%i", numero); // 9
```
