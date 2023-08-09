Cuando programamos en un lenguaje de alto nivel, esto se debe traducir a un lenguaje que el sistema pueda ejecutar

## Diseño a Ejecucion

- **Complilacion:** El lenguaje de alto nivel compilado en codigo assembly
- **Ensamblador:** Este codigo de alto nivel luego es traducido a codigo de maquina
- **Linker:** El linker se encarga de unir los distintos modulos de nuestro programa (bibliotecas)
- **Loader:** El programa se carga en memoria para luego se rejecutado

## Compilador

Hay distintos tipos de compiladores:

- **Compilador de una sola pasada o multiples pasadas:** Completa el proceso en uno o varios recorridos del programa fuente
- **Compilador incremental:** Compila linea por linea, no todo el programa (interpretes)
- **Cross-Compilador:** Compila para un sistema distinto al que se utiliza para compilar

 Proceso de compilacion:

1. **Analisis Lexico**: Identifica palabras clave o identificadores y crea una tabla de simbolos.
2. **Analisis Sintactico:** Interpreta que significan las instruccines
3. **Analisis Semantico:** Se analizan los atributos de los identificadores (tipo de simbolo)
4. **Mapeo de Acciones:** Traduce las lineas de codigo en codigo assembly.
5. **Generacion de Codigo:** Genera una archivo con el codigo assembly

Todos los pasos del proceso alteran y actualizan la tabla de simbolos.

### Mapeo de Acciones

Hay tres tipos de instrucciones:

- Operaciones Aritmética-Logicas.
- Control de flujo del programa.
- Movimiento de datos.

Cuando es excedida la cantidad de registros, se utiliza el stack. El compilador debe decidir que registros deben ser guardados en el stack. Esto afecta la eficiencia del codigo que genera.

Las variables globales permanecen a lo largo del tiempo de ejecucion del programa y se guardan en memoria. Las variables locales se guardan en el stack.

## Ensamblador

Traduce el codigo assembly, creado por el compilador, en codigo de maquina.

Es mucho mas simple ya que a cada instruccion de assembly, hay una relacion 1 a 1 con el código de maquina. Simplemente traduce el codigo. A esta funcion se la considera como transcondificacion.

Tambien se ocupa de la representacion simbolica para direcciones y constantes, Tambien nos permite definir la ubicacion del codigo. Ademas, provee cierto grado de aritmetica en tiempo de ensamblado. Puedo utilizar varible declaradas en otros módulos y declarar macros.

Muchas de las funciones del ensamblador se realizan a partir de las directivas del ensamblador. Indican al ensamblador como procesar una seccion del programa, son especificas del programa ensamblador.

Algunas de estas directivas generan informacion en memoria.

### Proceso de Ensamblado en Dos Pasadas

Consiste de tres pasos:

1. **Preproceso:** Expande las macros, registra las definiciones y las remplaza por el codigo correspondiente
2. **Primera Pasada:** Detecta identificadores y les asigna una posición de memoria, genera la tabla de simbolos
3. **Segunda Pasada:** Cada instrucciones es convertida a codigo de maquina, los identificadores son remplazados por su ubicacion en memoria, cada linea es procesada por completo antes de avanzar a la siguiente lineal. Genera el codigo objeto (codigo de maquina) y el listado (archivo de texto interpretado para ser interpretado por el programador)

El archivo objeto incluye un encabezamiento que contiene:

- La direccion de la primera instruccion a ejecutar si corresponde (`main`),
- las bibliotecas externas que son utilizada
- La tabla de simbolos externos y globales.
- Ademas incluye información sobre la relocalización del codigo.

A la hora de incluir modulos externos, estos pueden se relocalizados para poder ser cargados en memoria correctamente. Es el ensamblador el encargado de marcar que direcciones son relocalizables y cuales son absolutas. Esta información es necesaria para el linker.

### Tabla de Simbolos

Para generarla, el ensamblador recorre el archivo linea por linea, Incluye su nombre en la tabla. Al encontrarlos, les asigna un valor correspondiente.

Es una tabla que contiene el nombre de los simbolos, su direccion, su son extern o global, o si son relocalizables.

No todos los simbolos son relocalizables, por ejemplo:

- Direcciones de entrada/salida
- Rutinas del sistema

## Linker

El linker combina modulos que fueron ensamblados de forma separada:

- Resuelve referencias de forma externa al módulo
- Relocaliza los módulos combinándolos y reasignando las direccines internas a cada uno para reflejar su nueva localizacion
- Define en el módulo a cargar la dirección de la primera instruccion a ser ejecutada.

## Loader

En ambientes multitarea la ram es compartida entre varios procesos.

El loader debe relocalizar todos los simbolos relocalizables

Algunos loaders tienen la capacidad de combinar modulos en tiempos de carga (loader con capacidad de linkeo)

## Linking & Loader

Hay varias instancias

- **Link-Editor**: Produce una version linkeada del programa. (linker)
- **Relocating Loader**: Linkea en tiempo de carga y carga el programa en memoria para su ejecucion. (loader)
- **Linking Loader:** Linkea en tiempo de carga. Ademas de relocalizar, Busca automaticamente bibliotecas, Linkea y carga el programa en memoria. De esta forma, el ejecutable no tiene que contener las bibiliotecas utilizadas.
- **Linking Loader Dinamico:** Carga rutinas unicamente cuando el programa las necesita. Utiliza *Dynamic Link Libraries (dll)*

![[Compiladores y Ensambladores 1.png]]

## Archivos Objeto

Hay disintos tipos de archivos objeto:

- **Relocalizable**: Codigo binario y datos en un formato que permite combinarlo con otros archivos objeto.
- **Ejecutable:** Codigo binario y datos en un formato que permite se cargado directamente a memoria y ejecutarse.
- **Compartido:** Tipo especial de archivo objeto relocalizable. Puede se cargado en memoria y vinculado dinamicamente.
