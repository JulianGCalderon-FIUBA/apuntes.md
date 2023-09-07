Cuando una aplicación crea muchos hilos, cada uno puede ocupar una gran cantidad de memoria. Esto puede causar problemas.

Para resolver esto, se pueden utilizan **tareas asincrónicas** para intercalar tareas en un único hilo, o un *thread pool*.

Estas tareas son mucho más livianas que un hilo, son más fáciles de crear, es más eficiente de pasarle el control a ellas. Se pueden tener miles o decenas de miles de tareas, pero con la reserva de memoria para únicamente unos cuantos hilos.

Este modelo de programación asincrónica se conoce como concurrencia colaborativa.

## Casos de Uso

El modelo de programación asincrónica se pensó para casos donde el procesador está mayoritariamente inactivo. Como lecturas de un archivo, consultas a una API, etc.

No está pensado para programas de cómputo intensivo, como calcular el determinante de una matriz, ni para programas con estado mutable compartido (sincronización de memoria entre hilos).

## Futuros

Invocar a una función asincrónica retorna inmediatamente, antes de que comience a ejecutarse el cuerpo de la función. Devuelven una promesa a dicho valor.

En Rust, esta promesa implementa `Future`. Almacena toda la información necesaria para realizar el pedido hecho por la invocación.

```Rust
trait Future {
	type Output;
	fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) 
		-> Poll<Self::Output>;
}
```

Para no tener que indicar que una función devuelve un `Future`, podemos utilizar la palabra clave `async`. Esta permite que el compilador #todo

Las siguientes dos firmas de funcion son equivalentes:

```Rust
fn hello_world() -> impl Future<Output = String>;
async fn hello_world() -> String;
```

## Poll

El `Future` tiene un método `poll` para consultar si la operación se completó o no. El resultado tiene dos valores posibles

```Rust
enum Poll<T> {
	Ready(T),
	Pending,
}
```

Lo único que se puede realizar con un futuro es *golpearlo* con `poll` hasta que el valor esté disponible. Esto se conoce como el **modelo piñata**.

El sistema operativo provee *system calls* para que estas operaciones de consulta sean eficientes.

Cada vez que se llama `poll` en un `Future`, la tarea avanza todo lo que puede avanzar. Nunca bloqueará el hilo de ejecución.

## Await

Al ejecutar `poll` por primera vez sobre el retorno, se ejecuta el cuerpo de la función hasta el primer `await`. Si la función no se completó, retorna `Pending`.

La siguiente invocación continuará desde el punto donde estaba el *future connect*. El futuro almacena el punto donde debe retomarse en el siguiente *poll*, y el estado local.

La expresión `await` toma *ownership* del futuro y llama a `poll`:

- Si el futuro está en estado `Ready`, el valor final del futuro es el valor devuelto en la expresión `await`. Luego, continúa la ejecución.
- En caso contrario, retorna `Pending` a la función que lo invocó.

Debido a este comportamiento, solo se puede invocar a `await` en un entorno asincrónico.

## Executor

Las tareas vivirán en un *runtime* que se asigna al inicio del programa, y se encarga de ejecutar las tareas asincrónicas y llamar a `poll`.

La arquitectura asincrónica de Rust está diseñada para ser eficiente. Solo se llama a `poll`cuando vale la pena.

Para ejecutar funciones asincrónicas desde un entorno sincrónico, utilizamos `block_on`. Es un adaptador entre el mundo sincrónico y el mundo asincrónico.

Esta función bloquea el hilo de ejecución hasta que la función asincrónica pasada por parámetro termine, y devuelve su valor:

- No debe usarse desde un entorno asincrónico (se bloquearía la ejecución de todo el hilo).
- Duerme el hilo hasta que pueda llamarse nuevamente a `poll`.

## Tareas Asincrónicas

Para crear tareas asincrónicas, utilizamos `spawn_local`. Este recibe un Future y lo agrega a un *pool* que realizará el *polling* en un `block_on`. Es análogo al *spawn* de un hilo.

También podemos utilizar `spawn`. Crea la tarea y la coloca en el *pool* de hilos dedicado a realizar `poll`. No hay necesidad de ejecutar `block_on`.

Los *lifetimes* de las variables deben ser *static*, pues deben poder ejecutarse hasta el final del programa.

Todas las ejecuciones pueden realizarse en un único hilo. Una llamada asincrónica ofrece la apariencia de una única llamada a una función que se ejecuta hasta que se completa, pero es realizara por una serie de llamadas sincrónicas al método `poll`, que retorna rápidamente, hasta que se completa.

El cambio de una tarea a otra ocurre únicamente en las expresiones *await* (cuando este devuelve `Pending`). Un cómputo grande en una función no daría lugar a la ejecución de otras tareas (a diferencia de utilizar *threads*).

Una forma de resolverlo es utilizar `yield_now`, que de forma voluntaria pasa el control a otra tarea. La primera vez que se realiza `poll` retornará `Pending`. La siguiente vez devolverá `Ready`.

También existe `spawn_blocking`. Coloca la tarea en otro hilo del sistema operativo, se utiliza para realizar cómputo pesado. Esto permite que no se rompa el esquema de concurrencia colaborativa.

## Pin

Los tipos de datos autogenerados de `async` existen en el que implementan `Future` guardan una referencia a si mismas. Si estos son movidos (por estar en el *stack*), estas referencias no se actualizan.

Para resolver esto, se inventa el concepto de *pin*. Todos los tipos de dato por defecto implementan el *autotrait* `Unpin`. A menos que específicamente se marquen como `!Unpin`.

Las autorreferencias se envuelven en un tipo `Pin`.
