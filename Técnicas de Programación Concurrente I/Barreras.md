Una barrera es una estructura similar a un semáforo. Permite a múltiples hilos sincronizarse temporalmente para que los hilos esperen a que todos los hilos hayan llegado a cierto punto del código.

Se puede pensar como un semáforo, en el que el `wait` en lugar de esperar a que haya recurso disponible, espera a que no haya recurso disponible.

Luego, si todos $n$ hilos realizan `wait` de un semáforo con capacidad `n`, entonces se liberarán una vez todos hayan hecho `wait`.

## Barreras en Rust

Permiten sincroniza varios hilos en puntos determinados de un cálculo o algoritmo.

- Para crear una barrera, utilizamos `fn new(n: usize)`
- Para bloquear el hilo hasta que todos se encuentren en el punto, utilizamos `fn wait(&self)`.

El método `is_leader()` devolverá `true` en el hilo líder. Al levantar la barrera, el último hilo en llamar `wait()` se designa como líder.

Las barreras son reutilizables automáticamente.
