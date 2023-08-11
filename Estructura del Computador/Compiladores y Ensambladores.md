Cuando programamos en un lenguaje de alto nivel, esto se debe traducir a un lenguaje que el sistema pueda ejecutar

## Diseño a Ejecución

- **Compilación:** El lenguaje de alto nivel compilado en código Assembly
- **Ensamblador:** Este código de alto nivel luego es traducido a código de máquina
- **Linker:** El linker se encarga de unir los distintos módulos de nuestro programa (bibliotecas)
- **Loader:** El programa se carga en memoria para luego ser ejecutado

## Compilador

Hay distintos tipos de compiladores:

- **Compilador de una sola pasada o múltiples pasadas:** Completa el proceso en uno o varios recorridos del programa fuente
- **Compilador incremental:** Compila línea por línea, no todo el programa (interpretes)
- **Cross-Compilador:** Compila para un sistema distinto al que se utiliza para compilar

 Proceso de compilación:

1. **Análisis Léxico**: Identifica palabras clave o identificadores y crea una tabla de símbolos.
2. **Análisis Sintáctico:** Interpreta que significan las instrucciones
3. **Análisis Semántico:** Se analizan los atributos de los identificadores (tipo de símbolo)
4. **Mapeo de Acciones:** Traduce las líneas de código en código Assembly.
5. **Generación de Código:** Genera una archivo con el código Assembly

Todos los pasos del proceso alteran y actualizan la tabla de símbolos.

### Mapeo de Acciones

Hay tres tipos de instrucciones:

- Operaciones Aritmética-Lógicas.
- Control de flujo del programa.
- Movimiento de datos.

Cuando es excedida la cantidad de registros, se utiliza el stack. El compilador debe decidir que registros deben ser guardados en el stack. Esto afecta la eficiencia del código que genera.

Las variables globales permanecen a lo largo del tiempo de ejecución del programa y se guardan en memoria. Las variables locales se guardan en el stack.

## Ensamblador

Traduce el código Assembly, creado por el compilador, en código de máquina.

Es mucho más simple, ya que a cada instrucción de Assembly, hay una relación 1 a 1 con el código de máquina. Simplemente traduce el código. A esta función se la considera como transcodificación.

También se ocupa de la representación simbólica para direcciones y constantes, También nos permite definir la ubicación del código. Además, provee cierto grado de aritmética en tiempo de ensamblado. Puedo utilizar variables declaradas en otros módulos y declarar macros.

Muchas de las funciones del ensamblador se realizan a partir de las directivas del ensamblador. Indican al ensamblador como procesar una sección del programa, son específicas del programa ensamblador.

Algunas de estas directivas generan información en memoria.

### Proceso de Ensamblado en Dos Pasadas

Consiste de tres pasos:

1. **Pre proceso:** Expande las macros, registra las definiciones y las remplaza por el código correspondiente
2. **Primera Pasada:** Detecta identificadores y les asigna una posición de memoria, genera la tabla de símbolos
3. **Segunda Pasada:** Cada instrucción es convertida a código de máquina, los identificadores son remplazados por su ubicación en memoria, cada línea es procesada por completo antes de avanzar a la siguiente lineal. Genera el código objeto (código de máquina) y el listado (archivo de texto interpretado para ser interpretado por el programador)

El archivo objetó incluye un encabezamiento que contiene:

- La dirección de la primera instrucción a ejecutar, si corresponde (`main`),
- las bibliotecas externas que son utilizadas
- La tabla de símbolos externos y globales.
- Además, incluye información sobre la relocalización del código.

A la hora de incluir módulos externos, estos pueden se relocalizados para poder ser cargados en memoria correctamente. Es el ensamblador el encargado de marcar que direcciones son relocalizables y cuáles son absolutas. Esta información es necesaria para el linker.

### Tabla de Símbolos

Para generarla, el ensamblador recorre el archivo línea por línea, Incluye su nombre en la tabla. Al encontrarlos, les asigna un valor correspondiente.

Es una tabla que contiene el nombre de los símbolos, su dirección, si son *extern* o *global*, o si son relocalizables.

No todos los símbolos son relocalizables, por ejemplo:

- Direcciones de entrada/salida
- Rutinas del sistema

## Linker

El linker combina módulos que fueron ensamblados de forma separada:

- Resuelve referencias de forma externa al módulo
- Relocaliza los módulos combinándolos y reasignando las direcciones internas a cada uno para reflejar su nueva localización
- Define en el módulo a cargar la dirección de la primera instrucción a ser ejecutada.

## Loader

En ambientes multitarea la RAM es compartida entre varios procesos.

El loader debe relocalizar todos los símbolos relocalizables

Algunos loaders tienen la capacidad de combinar módulos en tiempos de carga (loader con capacidad de linkeo)

## Linking & Loader

Hay varias instancias

- **Link-Editor**: Produce una versión linkeada del programa. (linker)
- **Relocating Loader**: Linkea en tiempo de carga y carga el programa en memoria para su ejecución. (loader)
- **Linking Loader:** Linkea en tiempo de carga. Además de relocalizar, Busca automáticamente bibliotecas, Linkea y carga el programa en memoria. De esta forma, el ejecutable no tiene que contener las bibliotecas utilizadas.
- **Linking Loader Dinámico:** Carga rutinas únicamente cuando el programa las necesita. Utiliza *Dynamic Link Libraries (dll)*

![[Compiladores y Ensambladores 1.png]]

## Archivos Objeto

Hay distintos tipos de archivos objeto:

- **Relocalizable**: Código binario y datos en un formato que permite combinarlo con otros archivos objeto.
- **Ejecutable:** Código binario y datos en un formato que permite ser cargado directamente a memoria y ejecutarse.
- **Compartido:** Tipo especial de archivo objeto relocalizable. Puede ser cargado en memoria y vinculado dinámicamente.
