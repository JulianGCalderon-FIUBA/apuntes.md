Los monitores proveen una primitiva estructurada que se concentra la responsabilidad de la corrección de sus módulos. Son más fáciles de utilizar que los [[Semáforos]].

Son importantes en el mundo de la programación orientada a objetos, pues son una generalización del *objeto*.

Los monitores agregan el requerimiento de que únicamente un proceso pueda ejecutar una operación sobre un objeto al mismo tiempo. Por esta misma razón, los campos de los monitores siempre son privados.

```Java
class Contador {
	int i = 0;
	void incrementar() {
		int tmp = n;
		n = tmp + 1;
	}
}
```

## Variables de Condición

Un variable de condición tiene las siguientes propiedades:

- No guarda ningún valor
- Tiene asociado una cola

Consta de tres operaciones atómicas:

- `waitC(cond)`
- `signalC(cond)`
- `empty(cond)`

## Monitores

Nos permite sincronizar hilos con exclusión mutua y la posibilidad de esperar a que una condición se vuelva falsa. Tienen un mecanismo para señalizar otros hilos cuando su condición se cumple.

Un monitor consiste en:

- Un nombre
- Variables internas
- Procedimientos del monitor: rutinas que acceden directamente a las variables internas
- Una interfaz pública para que los procesos puedan acceder a las variables internas
- Inicialización de las variables internas
- Un conjunto de variables de condición que incorporan sincronismo al monitor.

Los procesos pueden tomar distintos estados:

- Esperando para entrar al monitor.
- Ejecutando el monitor (solo un proceso a la vez puede, hay exclusión mutua).
- Bloqueada en la cola de variables de condición.
- Recién liberado de la cola.
- Recién completó una operación `signalC`.

### Diferencias con un Semáforo

Algunas diferencias con los semáforos son:

- La operación `waitC` siempre bloquea, a diferencia de `wait` que puede hacerlo o no.
- La operación `signalC` no tiene efecto si la cola está vacía, a diferencia de `signal` que en caso de no haber procesos en la cola, incrementa el contador.
- Si no está vacía la cola, `signalC` desbloquea el proceso del tope de la cola. `signal` por el otro lado desbloquea un proceso arbitrario.
- Un proceso desbloqueado con `signalC` debe esperar que el proceso señalizador deje el monitor.

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
