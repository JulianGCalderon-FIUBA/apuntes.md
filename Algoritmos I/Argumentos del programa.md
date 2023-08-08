El main, como cualquier otra función, también puede recibir parámetros. Estos argumentos se envían al llamar al ejecutable.

```c
int main(int argc, char *argv[]);
```

- `argc`: Representa la cantidad de argumentos enviados
- `argv`: Es un vector de **strings** de los argumentos enviados

El primer argumento del main es siempre la ruta relativa del ejecutable

```c
//Comando: ./output.exe arg1 arg2 64

argc = 4;

argv[0] = "./output.exe";
argv[1] = "arg1";
argv[2] = "arg2";
argv[3] = "64";
```
