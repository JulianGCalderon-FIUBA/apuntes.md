## Buenas Practicas

**El software tiene 4 propiedades:**

- Variabilidad
- Complejidad
- Conformidad
- Invisibilidad

**Practicas:**

- Usar nombres descriptivos, significantes.
- Usar una sola palabra para cada concepto.
- Definir todo en **snake_case.**
- Constantes en **MAYUSCULA.**
- Escribir **pre-post** condiciones para cada función.

## Modulacion

Una `función` solo debe hacer una cosa, y recibe el nombre de lo que devuelve.

Un `procedimiento` es una función que no devuelve nada, recibe el nombre de lo que hace

```c
int cuadrado(int numero){ //FIRMA DE LA FUNCION
	return numero*numero;
}

void saludar_usuario(char msg[]){
	printf("%s", msg);
}
```

El **ámbito** de una función es el espacio de memoria que puede acceder. Cada función tiene su propio ámbito y las variables que se crean ahi se destruyen al salir.

### Pasaje

Algunos tipos de datos se pasan por valor, `(char, int, float)`**.**

Otros se pasan por referencia `(vectores, matrices)`

## Punteros

La **memoria** es un conjunto de celdas distribuidas linealmente, y cada una tiene una única dirección de memoria

Un `puntero` es un numero que apunta a una dirección de memoria, lo que permite modificarla desde cualquier lugar del código

```c
void duplicar(int *numero){
	*numero = (*numero) * (*numero);
}

int numero = 3;
duplicar(&numero);

printf("%i", numero); //9
```

**Operadores:**

`&`: Devuelve la dirección en la que se encuentra una variable.

`*`: Devuelve el valor al que apunta un puntero

## Vectores

Un `vector` almacena una colección finita y secuencial, de elementos de un mismo tipo de dato.

- El **tamaño** del vector define la cantidad máxima de elementos que puede llegar a tener
- El **tope** de un vector define la cantidad de elementos significantes que tiene el vector
- El í**ndice** es la posición en la que se encuentra cada elemento, empieza a contar desde 0.

Las **operaciones** entre vector se hacen elemento a elemento. Existen dos tipos de eliminaciones:

- **Eliminación Física:** Es aquella que consiste en eliminar realmente el elemento del vector
- **Eliminación Lógica:** Es aquella que consiste en marcar como 'eliminado' un elemento del vector, Pero dejándolo en su posición.

```c
int agregar_elemento(int edades[MAXIMO], int *tope, int elemento){
	edades[*tope] = elemento;
	(*tope)++
}

int const MAXIMO = 10;
int edades[MAXIMO] = {12, 23, 34, 45, 56, 67};
int tope = 6;

int elemento = 78;
agregar_elemento(edades, &tope, elemento);
```

## Matrices

Una `matriz` es un arreglo de 2 dimensiones, como vectores adentro de un vector. Se comporta como un vector

```c
int matriz[MAX_FILAS][MAX_COLUMNAS] = ...

printf("%i", matriz[i][j])
```

## Bibliotecas

Las bibliotecas son código externo, que podemos importar a nuestro archivo.

Las bibliotecas estándar son aquellas que vienen con c, no tenemos que instalarlas.

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <ctype.h>
```

## Strings

`#include <string.h>`

Al trabajar con strings, las funciones suponen que un string es un vector de caracteres terminado en '\0'

### Funciones

```c
// POST: La longitud de la cadena
int strlen(char cadena[]);

// Copia los contenidos de 'origen' en 'destino' (sobrescribe)
void strcpy(char destino[], char origen[]);

// Copia los contenidos de 'origen' al final de 'destino' (concatena)
void strcat(char destino[], char origen[]);

/* 
 * POST: Compara las dos cadenas
 *    0 si son iguales
 *   >0 si cadena1 > cadena2
 *   <0 si cadena1 < cadena2
 */	
int strcmp(char cadena1[], char cadena2[]);
```

### Operaciones

**Imprimir cadenas:**

`printf("%s", cadena);`

**Leer Cadenas**

`scanf("%s", &cadena);` Lee hasta el primer espacio o \n

`scanf("%s[^\n]", cadena);` Lee hasta el primer \n

## Registros

Un registro es un tipo de dato que define una lista de variables agrupadas bajo un mismo nombre en un bloque de memoria.

```c
typedef struct fecha{
  unsigned short dia;
	unsigned short mes;
	int anio;
} fecha_t;
```

Para acceder a estos campos a partir de un registro, usamos el operador **[.]**

Para acceder a estos campos a partir de un puntero, podemos usar la abreviación **[→]**

```c
fecha_t reg;
reg.dia = 16;
reg.mes = 5;

fecha_t *ptr = &reg;
ptr->anio = 2002;
//(*ptr).anio = 2002;
```
