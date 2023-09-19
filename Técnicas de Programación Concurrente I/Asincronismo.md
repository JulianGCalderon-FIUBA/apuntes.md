Cuando una aplicación crea muchos hilos, cada uno puede ocupar una gran cantidad de memoria. Esto puede causar problemas.

Para resolver esto, se pueden utilizan **tareas asincrónicas** para intercalar tareas en un único hilo, o un *thread pool*.

Estas tareas son mucho más livianas que un hilo, son más fáciles de crear, es más eficiente de pasarle el control a ellas. Se pueden tener miles o decenas de miles de tareas, pero con la reserva de memoria para únicamente unos cuantos hilos.

Este modelo de programación asincrónica se conoce como concurrencia colaborativa, ya que son las mismas tareas asincrónicas las que realizan el *yield* cuando deben esperar a una operación bloqueante.

## Casos de Uso

El modelo de programación asincrónica se pensó para casos donde el procesador está mayoritariamente inactivo. Como lecturas de un archivo, consultas a una API, etc.

No está pensado para programas de cómputo intensivo, como calcular el determinante de una matriz, ni para programas con estado mutable compartido (sincronización de memoria entre hilos).

## Futuros

Invocar a una función asincrónica retorna inmediatamente, antes de que comience a ejecutarse el cuerpo de la función. Devuelven una promesa a dicho valor. En Rust, esta promesa implementa `Future`.

```Rust
trait Future {
	type Output;
	fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) 
		-> Poll<Self::Output>;
}
```

Para crear una función asincrónica, utilizaremos la sintaxis `async fn`. El compilador se encargará de dos cosas.

En primer lugar, cambiará el valor de retorno para que devuelva un tipo de dato que implemente `Future`. Las siguientes dos firmas de función son equivalentes:

```Rust
fn hello_world() -> impl Future<Output = String>;
async fn hello_world() -> String;
```

En segundo lugar, definirá el tipo de dato particular, con toda la información necesaria para completar el pedido. Esto incluye sus argumentos, espacio para sus variables locales, etc. Se puede pensar como capturar el todo el *call's stack frame* de la función como un valor ordinario.

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

## Pin

Los tipos de datos autogenerados de `async` que implementan `Future` guardan una referencia a sí mismas. Si estos son movidos (por estar en el *stack*), estas referencias no se actualizan.

Para resolver esto, se inventa el concepto de *pin*. Todos los tipos de dato por defecto implementan el *autotrait* `Unpin`. A menos que específicamente se marquen como `!Unpin`.

Las autorreferencias se encierran en un tipo de dato `Pin<Box<T>>`. Si `T` es `!Unpin`, `Pin` evita que se mueva haciendo imposible llamar métodos que requieran `&mut T` como `mem::swap`.

## Context

Los futuros necesitan una forma de notificar cuando pueden realizar algún tipo de avance, para esto se utiliza el tipo de dato `Context`. Estos proveen acceso a un valor del tipo `Waker`, que puede ser utilizado para despertar una tarea en específica.

Cada vez que se llama un `poll` en un futuro, esta llamada se realiza como parte de una "tarea", las tareas son futuros de primer nivel que fueron enviados a un ejecutor. El `Waker` provee un método `wake()` que puede ser utilizado para decirle al ejecutor que la tarea asociada debe ser despertada.

Esto permite que únicamente se llame a `Poll` cuando el futuro pueda realizar un avance, evitando llamadas innecesarias.

## Await

Al ejecutar `poll` por primera vez sobre el retorno, se ejecuta el cuerpo de la función hasta el primer `await`. Si la función no se completó, retorna `Pending`.

La siguiente invocación continuará desde el punto donde estaba el *future connect*. El futuro almacena el punto donde debe retomarse en el siguiente *poll*, y el estado local.

La expresión `await` toma *ownership* del futuro y llama a `poll`:

- Si el futuro está en estado `Ready`, el valor final del futuro es el valor devuelto en la expresión `await`. Luego, continúa la ejecución.
- En caso contrario, retorna `Pending` a la función que lo invocó.

Debido a este comportamiento, solo se puede invocar a `await` en un entorno asincrónico.

Si queremos esperar el valor de dos futuros simultáneamente, podremos utilizar la macro `join!`.

## Executor

Los futuros de Rust son *lazy*, no harán nada a menos que sean activamente conducidos hasta su finalización. Los ejecutores son un conjunto de futuros de alto nivel que se encargarán de esto.

Las tareas vivirán en un ejecutor que se asigna al inicio del programa, y se encarga de ejecutar las tareas asincrónicas y llamar a `poll`. Estos son externos a Rust, y hay varios. Los más comunes son Tokio y async-std.

Todas las ejecuciones pueden realizarse en un único hilo. Una llamada asincrónica ofrece la apariencia de una única llamada a una función que se ejecuta hasta que se completa, pero es realizara por una serie de llamadas sincrónicas al método `poll`, que retorna rápidamente hasta que se completa.

### Ejecución de un Futuro

Para ejecutar funciones asincrónicas desde un entorno sincrónico, utilizamos `block_on`. Es un adaptador entre el mundo sincrónico y el mundo asincrónico.

Esta función bloquea el hilo de ejecución hasta que la función asincrónica pasada por parámetro termine, y devuelve su valor. Debido a esto, no debe usarse desde un entorno asincrónico (se bloquearía la ejecución de todo el hilo).

### Tareas Asincrónicas

Para crear tareas asincrónicas, utilizamos `spawn_local`. Este recibe un futuro y lo agrega a un *pool* que realizará el *polling* en un `block_on`. Es análogo al *spawn* de un hilo.

Es irrelevante en que orden realizamos `await` de las tareas creadas, ya que una vez creadas, serán *polleadas* por el ejecutor en cuanto la tarea principal del `block_on` haya bloqueado.

Si no queremos depender de `block_on`, podemos utilizar `spawn`. Crea la tarea y la coloca en el *pool* de hilos dedicado a realizar `poll`. En este caso, no hay necesidad de ejecutar `block_on`.

### Computo Intenso

El cambio de una tarea a otra ocurre únicamente en las expresiones *await* (cuando este devuelve `Pending`). Un cómputo grande en una función no daría lugar a la ejecución de otras tareas (a diferencia de utilizar *threads*). Existen dos formas de solucionarlo.

Una forma de resolverlo es utilizar `yield_now`, que de forma voluntaria pasa el control a otra tarea. La primera vez que se realiza `poll` retornará `Pending`. La siguiente vez devolverá `Ready`.

La segunda forma de resolverlo es con la utilización de `spawn_blocking`. Coloca la tarea en otro hilo del sistema operativo, se utiliza para realizar cómputo pesado. Esto permite que no se rompa el esquema de concurrencia colaborativa.
