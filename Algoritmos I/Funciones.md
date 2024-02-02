Una **función** solo debe hacer una cosa, y recibe el nombre de lo que devuelve.

Un **procedimiento** es una función que no devuelve nada, recibe el nombre de lo que hace

```c
int cuadrado(int numero){ //FIRMA DE LA FUNCION
	return numero*numero;
}

void saludar_usuario(char msg[]){
	printf("%s", msg);
}
```

El **ámbito** de una función es el espacio de memoria que puede acceder. Cada función tiene su propio ámbito y las variables que se crean ahí se destruyen al salir.

## Pasaje

Algunos tipos de datos se pasan por valor: `(char, int, float)`. Otros se pasan por referencia `(vectores, matrices)`
