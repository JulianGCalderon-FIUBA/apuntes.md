## Caracteristicas

**Cardinalidad infinita:** El tamaño puede variar en el tiempo, y puede virtualmente contener cualquier cantidad de elementos. Su limitación esta dada por el tamaño de la memoria principal de la computadora.

**Persistencia total:** La información almacenada dentro de un archivo persiste en el tiempo, es decir que queda almacenada una vez el algoritmo termina de hacer uso de la misma.

**De Texto:** Los archivos de texto están escritos en caracteres, son secuenciales. Tienen extension `.txt`

**Binarios**: Están escritos en binario, pueden ser tanto secuenciales como de acceso directo. Tienen extension `.dat`

**Secuenciales**: No pueden abrirse con el modo `+`. Se leen o modifican de principio a fin.

**Acceso Directo:** Podemos modificar la posición del puntero y modificarlo o leerlo en cualquier orden.

**Lectura**: La minima unidad de lectura que puede tiene un archivo de texto es un struct `char`, en el caso de archivos binarios, la unidad es el `int`

## Funciones

### `fopen`

```c
FILE *fopen(const char *filename, const char *mode);

if (!FILE){
	printf("Error de apertura!\n");
}
```

Abre el archivo en la ruta indicada, y devuelvo un puntero al stream asociando a dicho archivo.

#### Modos:

- `"r"`: Abre un archivo para lectura
- `"w"`: Crea un archivo en blanco para escritura
- `"a"`: Adjunta al final del archivo
- `"r+"`: Abre un archivo para lectura/escritura
- `"w+"`: Crea un archivo en blanco para lectura/escritura
- `"a+"`: Abre un archivo al final para lectura/escritura

### `fclose`

```c
int fclose(FILE *stream); //Devuelve 0 si es exitosa.
```

Cierra el stream dado, y guarda los datos del buffer en el dispositivo. Es importante cerrar un archivo para evitar la corrupción del mismo

### `feof`

```c
int feof(FILE *stream);

while (!feof(arch))
{
	//PROCEDIMIENTO
}
```

Devuelve `true` si el stream llego al fin del archivo.

### `fflush`

```c
int fflush( FILE *stream);
```

Si el stream apunta a un archivo de salida, la función envía los datos sin escribir al archivo.

## Stream

Los streams de caracteres son un flujo continuo de caracteres, tienen una naturaleza **exclusivamente secuencial**. Existen tres tipos de streams en todo programa escrito en **C**:

- S**tandard input:** Corresponde a la entrada estándar del programa, el stream por el cual ingresan datos al programa, esta asociado al teclado
- **Standard output:** Corresponde a la salida estándar del programa, el stream al que se mandan los datos para ser mostrados, esta asociado a la consola
- **Standard error:** Corresponde al stream de errores estándar, al cual se mandan los errores que ocurren durante la ejecución del mismo.

### `fgetc`

```c
int fgetc(FILE *stream);
```

Se utiliza cuando el stream esta abierto en modo `"r"`, extrae el próximo carácter del flujo de caracteres y lo devuelve casteado como un `int`

### `fputc`

```c
int fputc(int c, FILE *stream);
```

Se utiliza cuando el stream esta abierto en modo `"w"`, escribe el carácter casteado como un `int` en le stream de datos.

### `fscanf`

```c
int fscanf(FILE *stream, char *format, ...);
```

Lee de un `stream` una entrada con formato `format` y lo almacena en los punteros deseados `...`, devuelve la cantidad de elementos leídos.

### `fprintf`

```c
int fprintf(FILE *stream, char *format, ...);
```

Escribe en el puntero de un archivo de texto un `string` con format `format` con las variables especificadas `...`

### `fread`

```c
size_t fread(object *buffer, size_t size, size_t count, FILE *stream);
```

Lee de un `stream` una cantidad `count` de objetos binarios que ocupan una cantidad de memoria `size` almacenándola en un `buffer`. Que representa un arreglo de longitud `count` de objetos. Devuelve la cantidad de elementos leídos.

### `fwrite`

```c
size_t fwrite(object *buffer, size_t size, size_t count, FILE *stream);
```

Escribe en un `stream` una cantidad `count` de objetos binarios que ocupan una cantidad de memoria `size` almacenada en un `buffer`. Que representa un arreglo de longitud `count` de objetos

### `fseek`

```c
size_t fseel(FILE *stream, int offset, int start);
```

Sitúa el puntero del stream, desplazandolo una cantidad `offset` de bytes a partir de `start`

El parámetro `start` puede tomar tres valores:

- `SEEK_SET`: Representa el comienzo del stream
- `SEEL_CUR`: Representa la posición actual del stream
- `SEEK_END`: Representa el fin del stream

## Operaciones sobre archivos

### `remove`

```c
int remove(char *fname);
```

Elimina el archivo de nombre `fname` que se encuentra en el directorio root del programa

### `rename`

```c
int rename(const char *old, const char *new);
```

Renombra el archivo `old` por `new`

## Buenas Practicas

- **Siempre** abrir y cerrar en la misma función
- Me mantengo a la estructura:
	1. Abro el archivo
	2. Opero
	3. Cierro el archivo
- Las rutas son constantes
- Los archivos se leen una única vez
- Es buena practica tener copia de los archivos mientras se trabaja con ellos, por seguridad
