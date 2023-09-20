Los monitores proveen una primitiva estructurada que se concentra la responsabilidad de la corrección de sus módulos. Son más fáciles de utilizar que los [[Semáforos]].

Son importantes en el mundo de la programación orientada a objetos, pues son una generalización del *objeto*.

Los monitores agregan el requerimiento de que únicamente un proceso pueda ejecutar una operación sobre un objeto al mismo tiempo. Por esta misma razón, los campos de los monitores siempre son privados.

```Java
class Contador {
	private int i = 0;
	public synchronized void incrementar() {
		this.i += 1;
	}
}
```

Los monitores proveen exclusión mutua, además de una serie de [[Variables de Condición]] que permiten sincronizar los distintos hilos. Tienen un mecanismo para señalizar otros hilos cuando su condición se cumple.

- Desde dentro del monitor, los procesos pueden ejecutar una operación de `waitC`, bloqueándose y liberando el monitor hasta que otro proceso los desbloquee.
- Desde dentro del monitor, los procesos pueden ejecutar una operación de `signalC` para liberar procesos esperando.

Cuando son desbloqueados, tendremos dos procesos dentro del monitor, el que señalizo, y el que fue liberado. Esto es inválido. Se debe definir una precedencia entre los procesos liberados $W$, los que señalizaron $S$, y los que están en espera de la entrada del monitor $E$. Para resolver esto se creó el *immediate resumption requierement*.

El IRR indica que los procesos se ejecutan según $W > S > E$. Los liberados se deben ejecutar primero, luego el proceso que señalizo, y finalmente siguen los procesos en la cola. Esto implica que la operación de `signalC` dentro de los monitores son, de cierto modo, bloqueantes.

En Java, por otro lado, se ejecutan según $S > W = E$. Primero continua proceso que señaliza, y luego, sin preferencia, los procesos liberados y los procesos en la cola del monitor.

## Estados de Procesos

Los procesos pueden tomar distintos estados frente a un monitor:

- Esperando para entrar al monitor.
- Ejecutando el monitor (solo un proceso a la vez puede, hay exclusión mutua).
- Bloqueada en la cola de variables de condición, tras un `waitC`.
- Recién liberado de la cola, esperando a continuar su ejecución.
- Recién completó una operación `signalC`, esperando a continuar su ejecución.

![[Monitores 1695234944.png]]

## Monitores en Java

### Hilos

En Java, los hilos no utilizan al sistema operativo. Son conocidos como *green threads* y están implementados por el propio lenguaje. Hay dos formas de crear hilos:

- Heredando la clase `Thread`.
- Implementando la interfaz `Runnable`.

### Sección Crítica

Para la utilización de monitores, existen los bloques `synchronized`. Estos deben recibir una variable la cual sincronizarán a partir de un *lock* exclusivo.

Solo un proceso puede estar dentro de un bloque `synchronized`. El *lock* es reentrante, esto implica que pueden ser interrumpidos.

Los métodos `synchronized` son aquellos bloques de código que son un método completo. La utilización de un método `synchronized` convierte automáticamente la clase en un monitor.

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
- Método `notify()`: Despierta alguno de los hilos que espera por el monitor, el cual podrán efectivamente en cuanto el hilo actual salga del monitor.
- Método `notifyAll()`: Despierta todos los hilos que esperan por el monitor.

## Variables Volátiles

Los hilos guardan los valores de las variables compartidas en su memoria caché. Esto es más eficiente, pero implica que no siempre se obtendrá el valor más reciente.

La palabra clave `volatile` le indica al compilador que el valor de la variable no debe cachearse y debe leerse siempre de la memoria principal. De esta forma los hilos siempre verán el valor más actualizado de la variable.

La declaración de una variable como volátil no realiza ningún *lockeo* en dicha variable.
