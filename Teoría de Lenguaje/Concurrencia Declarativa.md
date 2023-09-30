A través del concepto de concurrencia, podremos tener hilos independientes de ejecución. El orden de ejecución dependerá del *scheduler* del sistema operativo.

```Oz
declare A B C
thread
	A = B + C
end
C = 4
thread
	B = 10
end
{Browse A} % 14
```

Si el primer hilo se ejecuta primero, entonces esperará a que estén definidos los valores necesarios para continuar.

Gracias al las virtudes del modelo declarativo, este tipo de concurrencia es determinística. Esto no implica que siempre se ejecuta de la misma forma, sino que no hay diferencias observables entre dichas ejecuciones.

## Tipos de Hilos

Hay tres tipos de hilos:

- Los hilos pesados son diferentes procesos a nivel del sistema operativo
- Los hilos medianos pertenecen al mismo proceso, son definidos a nivel del kernel.
- Los hilos livianos, o *green threads* son a nivel de usuario. Se pueden implementar a nivel del lenguaje de programación.

## Interleaving

Los hilos se ejecutan de forma intercalada (*interleaving*). Los cómputos no se solapan (a menos que se tengan múltiples procesadores).

- Orden total: Hablamos de este tipo de orden cuando todas las ejecuciones están ordenadas. Cuando no hay diferentes caminos.
- Orden causal: Hablamos de este tipo de orden cuando a partir de una causa, 
