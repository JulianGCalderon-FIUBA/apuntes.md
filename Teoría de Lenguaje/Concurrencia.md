A través del concepto de concurrencia, podremos tener hilos independientes de ejecución. Estos programas son no determinísticos, pues el orden de ejecución dependerá del *scheduler* del sistema operativo.

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
