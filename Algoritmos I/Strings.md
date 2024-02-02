Para trabajar con *strings*, debemos importar `strings.h`. Las funciones suponen que un `string` es un vector de caracteres terminado en `\0`

## Funciones

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

## Operaciones

- `printf("%s", cadena);`
- `scanf("%s", &cadena);` Lee hasta el primer espacio o `\n`
- `scanf("%s[^\n]", cadena);` Lee hasta el primer `\n`
