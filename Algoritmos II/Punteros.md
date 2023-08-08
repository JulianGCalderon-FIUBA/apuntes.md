Los punteros son simplemente variables que poseen una dirección de memoria, estas son útiles para modificar la memoria desde cualquier parte del programa. Un vector, por ejemplo, es simplemente un puntero que apunta al primer elemento del arreglo. Nosotros a partir de esta primera posición podemos acceder al resto de elementos.

```c
elemento_t vector[MAX_ELEMENTOS];

vector[0] == *vector;
vector[1] == *(vector+1);
vector[2] == *(vector+2);
```

Al sumarle un entero a un puntero, estamos desplazándonos una cantidad `size_of(elemento_t)` de bytes, por lo que terminamos al comienzo del próximo elemento del vector.

Al declarar un puntero, es útil inicializarlo con el valor `NULL` para asegurarnos de no acceder a memoria invalida

## Multiples Punteros

Es posible crear punteros que apunten a otros punteros, como es el caso de un vector de `strings`. Los elementos de este puntero doble apuntan al primer elemento de cada *`string`*

```c
char strings[10][10];

strings[0][0] == **string;
strings[2][0] == **(string+2);
strings[3][3] == *(*(string+3)+3);
```

## Punteros a Funciones

Un puntero a función no es mas que la dirección de memoria donde reside una determinada función. Lo que permite pasarlo como argumento para funciones.

- Se puede tener un arreglo de funciones.
- Para punteros a funciones, no se debe reservar/liberar memoria.

```c
void imprimir_entero(int n)
{
	printf("%i", n);
}

int main()
{
	void (*func)(int) = imprimir_entero; // No es necesario referenciar la funcion
	
	(*func)(10);	
	func(10); // No es necesario desreferenciar el puntero

	return 0;
}
```

### **¿En Que Situaciones Se utilizan?**

Los punteros a funciones son útiles cuando tengo dos funciones con mucho código en común, pero difieren en una parte. Entonces puedo pasar este código distinto como un puntero a función.

Es útil, por ejemplo, para ordenar vectores, puedo tener la lógica de ordenar vector en una función y pasarle como parámetro una función que se ocupe de comparar los elementos.

## Puntero Comodín `void*`

En C, existe un tipo de puntero denominado ***puntero comodín***, este puede apuntar a cualquier tipo de dato ya que no esta asociado a ninguno. El puntero comodín no puede ser desreferenciado, para acceder a su valor se debe castear a otro tipo de puntero.

```c
int main()
{
	int a = 10;
	char b = 'a';

	
	void *p = &a;
	printf("%i", *((int*) p));
	p = &b;
	printf("%c", *((char*) p));
	
	return 0;
}
```
