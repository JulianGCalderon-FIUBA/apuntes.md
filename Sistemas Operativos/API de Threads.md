## Creación de Threads

Lo primero que debemos hacer para escribir un programa ***multi-threaded*** es crear nuevos hilos:

```c
#include <pthread.h>
int
pthread_create(pthread_t      *thread,
         const pthread_attr_t *attr,
               void           *(*start_routine) (void*),
               void           *arg);
```

El primer argumento es un puntero a una estructura de tipo `pthread_t`, la usaremos para interactuar con el ***thread***. Se la pasamos a la función para inicializarla.

El segundo argumento se utiliza para especificar los atributos que tendrá el hilo. Estos atributos se inicializan con una llamada a `pthread_attr_init()`.

El tercer argumento es el es complejo, es el puntero a la función donde comenzará el hilo, Esta funcionara deberá recibir un puntero como parámetro. El cuarto argumento es el argumento que se le pasara a la función anterior cuando esta se ejecute.

## Finalización de Threads

Muchas veces,queremos esperar a que un ***thread*** finalice para continuar la ejecución:

```c
#include <pthread.h>
int
pthread_join(pthread_t      thread,
             void           **value_ptr);
```

El primer argumento es el hilo al cual se deberá esperar, mientras que el segundo argumento es un puntero al valor de retorno que esperas recibir de la función. Estos valores de retorno no pueden ser almacenados en el ***stack***, ya que este deja de ser válido en cuanto termina el ***thread***.

## Utilización de Locks

Para poder evitar las condiciones de carrera, debemos poder crear ***locks*** que nos provean con ***exclusión mutua:***

```c
int pthread_mutex_lock(pthread_mutex_t *mutex);
int pthread_mutex_unlock(pthread_mutex_t *mutex);
```

 Si ningún otro hilo posee el ***lock*** cuando llamada a ***`pthread_mutex_lock`***, entonces obtendremos el ***lock*** y continuamos con la ejecución. Si otro hilo posee el ***lock***, entonces el hilo actual se bloquea hasta que el ***lock*** esté disponible. Solo el ***thread*** que posee el ***lock*** deberá llamar a la función ***`pthread_mutex_lock`.*** Hay situaciones en las que tendremos a múltiples hilos esperando el ***lock***, cuando se libera, lo obtendrá arbitrariamente cualquiera de los ***hilos***, pero solo uno.

Los *locks* para ser utilizados deben ser inicializados (y debidamente destruidos) para que puedan ser utilizados:

```c
int pthread_mutex_destroy(pthread_mutex_t *mutex);
int pthread_mutex_init(pthread_mutex_t *restrict mutex,
                 const pthread_mutexattr_t *restrict attr);

//ALTERNATIVA
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
```

Los programas pueden tener múltiples ***locks*** para poder manejar distintas secciones criticas, sin que surjan condiciones de carrera.

## Condition Variables

Las *condition variables* son muy útiles cuando queremos que ocurra cierto tipo de señalización entre *threads.*

```c
int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex);
int pthread_cond_signal(pthread_cond_t *cond);
```

Para utilizar estas variables, debemos tener un ***lock*** asociado a esta condición. obteniendolo antes de usar algunas de las rutinas.

La primer rutina `pthread_cond_wait()` suspende el ***thread*** actual, esperando a que otro hilo le envié una señal para continuar. Además, libera el ***lock*** que se le pasa por parámetro, volviendolo a adquirir luego de despertar. Desde otro ***thread*** utilizamos la rutina `pthread_cond_signal()` para despertar al primer hilo.

## Consejos

Hay un número de pequeñas pero importantes cosas a tener en cuenta cuando trabajamos con ***threads:***

- ***Simpleza:*** Por sobre todas las cosas, los mecanismos de sincronización entre hilos deben ser lo más simple posible.
- ***Minimizar Interacciones:*** Si minimizamos las interacciones entre hilos, entonces reducimos los ***bugs*** que podamos introducir al programa.
- *Inicializar variable:* Antes de utilizar los ***locks*** o ***condition variables***, debemos asegurarnos que estos estén inicializados.
- ***Código de Retorno:*** La mayoría de las funciones de la biblioteca pueden fallar, debemos siempre tener en cuenta este caso.
