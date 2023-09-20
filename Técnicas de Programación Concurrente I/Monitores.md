## Variables de Condición

Un variable de condición es un mecanismo de sincronización que no guarda ningún valor, sino que tiene asociado una cola.

Consta de tres operaciones atómicas:

- La operación de `waitC(cond)` siempre bloquea el proceso hasta que sea desbloqueado con `signalC(cond)`. El proceso es agregado a una cola.
- La operación `signalC(cond)` desbloquea el último proceso de la cola. Si está vacía, no tiene ningún efecto.
- La operación `empty(cond)` nos permite verificar si la condición es cierta sin necesidad de bloquear el proceso. Esto es necesario, ya que si la condición es cierta, el proceso se bloquea igualmente.

## Monitores

Los monitores proveen una primitiva estructurada que se concentra la responsabilidad de la corrección de sus módulos. Son más fáciles de utilizar que los [[Semáforos]].

Son importantes en el mundo de la programación orientada a objetos, pues son una generalización del *objeto*.

Los monitores agregan el requerimiento de que únicamente un proceso pueda ejecutar una operación sobre un objeto al mismo tiempo. Por esta misma razón, los campos de los monitores siempre son privados.

```Java
class Contador {
	private int i = 0;
	public synchronized void incrementar() {
		i += 1;
	}
}
```

Los monitores proveen exclusión mutua, además de una serie de variables de condición que permiten sincronizar los distintos hilos. Tienen un mecanismo para señalizar otros hilos cuando su condición se cumple.

Desde dentro del monitor, los procesos pueden ejecutar una operación de `waitC` para liberar el monitor hasta que otro proceso los desbloquee (desde dentro del monitor).

Cuando son desbloqueados, tendremos dos procesos dentro del monitor, el que señalizo, y el que fue liberado. Esto es inválido. Se debe definir una precedencia entre los procesos liberados, los que señalizaron. Para resolver esto se creó el *immediate resumption requierement*.

El IRR indica que los procesos liberados se deben ejecutar primero que los procesos recién liberados.

## Estados de Procesos

Los procesos pueden tomar distintos estados frente a un monitor:

- Esperando para entrar al monitor.
- Ejecutando el monitor (solo un proceso a la vez puede, hay exclusión mutua).
- Bloqueada en la cola de variables de condición.
- Recién liberado de la cola.
- Recién completó una operación `signalC`.

## Java

En Java, los hilos son distintos a los hilos de Rust. Esto se debe a que no utilizan al sistema operativo. Están implementados por el propio lenguaje. Hay dos formas de crear hilos:

- Heredando la clase `Thread`.
- Implementando la interfaz `Runnable`.

### Secciones Críticas

Para la utilización de monitores, existen los bloques `synchronized`. Estos tienen dos partes:

- Un objeto que servirá como *lock*
- Un bloque de código a ejecutar en forma atómica

Los métodos `synchronized` son aquellos bloques de código que son un método funciono.

El funcionamiento es el siguiente:

- Cada objeto tiene un *lock* o monitor
- Solo un hilo a la vez puede tomar el *lock*
- El *lock* es reentrante. Esto implica que pueden ser interrumpidos.

Un ejemplo de uso puede ser un contador:

```Java
void incrementar(int cantidad) {
	synchronized(this) {
		this.valor += cantidad;
	}
}

synchronized void incrementar(int cantidad) {
	this.valor += cantidad;
}
```

Para métodos estáticos, tendremos:

```Java
static void escribirMensaje(int cantidad) {
	synchronized(Contador.class) {
		System.out.println("Mensaje del contador");
	}
}

static synchronized void escribirMensaje(int cantidad) {
	System.out.println("Mensaje del contador");
}
```

### Exclusión Mutua

La sincronización únicamente ocurre cuando un mismo objeto se le pasa como argumento a dos hilos distintos. Por ejemplo:

```Java
public static void main(String[] args) {
	Contador contador = new Contador();
	
	Thread hilo1 = new Thread(new Hilo(contador));
	Thread hilo2 = new Thread(new Hilo(contador));

	hilo1.start()
	hilo2.start()
}
```

### Señalización

Se debe tener el monitor adquirido para poder llamar a los siguientes métodos:

- Método `wait()`: Libera el monitor adquirido y suspende el hilo, hasta que otro hilo llame a `notify()` o `notifyAll()`.
- Método `notify()`: Despierta alguno de los hilos que espera por el monitor
- Método `notifyAll()`: Despierta todos los hilos que esperan por el monitor.

## Variables Volátiles

Los hilos guardan los valores de las variables compartidas en su memoria caché. Esto es más eficiente, pero implica que no siempre se obtendrá el valor más reciente.

La palabra clave `volatile` le indica al compilador que el valor de la variable no debe cachearse y debe leerse siempre de la memoria principal. De esta forma los hilos siempre verán el valor más actualizado de la variable.

La declaración de una variable como volátil no realiza ningún *lockeo* en dicha variable.
