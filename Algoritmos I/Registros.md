## Registros

Un registro (del inglés *record*) es un tipo de dato que define una lista de variables agrupadas bajo un mismo nombre en un bloque de memoria.

```c
typedef struct fecha{
  unsigned short dia;
	unsigned short mes;
	int anio;
} fecha_t;
```

- Para acceder a estos campos a partir de un registro, usamos el operador `.`
- Para acceder a estos campos a partir de un puntero, podemos usar la abreviación `->`

```c
fecha_t reg;
reg.dia = 16;
reg.mes = 5;

fecha_t *ptr = &reg;
ptr->año = 2002;        // El caracter 'ñ' no esta permitido
//(*ptr).año = 2002;
```
