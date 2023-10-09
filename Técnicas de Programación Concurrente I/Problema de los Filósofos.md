Cinco filósofos se sientan alrededor de una mesa y pasan su vida cenando y pensando. Cada filósofo tiene un plato de fideos y un palito chino a la izquierda de su plato.

Para comer los fideos son necesarios dos palitos, y cada filósofo solo puede tomar los que están a su izquierda y derecha.

Si cualquier filósofo toma un palito y el otro está ocupado, se quedará esperando, con el palito en la mano, hasta que pueda tomar el otro palito, para luego empezar a comer.

## Solución con [[Locks]]

Si cada filósofo toma los palitos en cualquier orden, entonces se puede llegar a un *deadlock*. Por ejemplo: todos los filósofos toman el palito de la derecha.

La forma de resolverlo es imponiendo un orden específico. Numeramos los palitos del uno al cinco, y cada filósofo toma los palitos cercanos en orden numérico.

Esto nos asegura nunca llegar a un *deadlock*, pues nunca se tendrá que todos los filósofos tomen el palito de la derecha, ya que uno tomará el palito de la izquierda.

## Solución con [[Técnicas de Programación Concurrente I/Canales]]

Modelaremos los cinco tenedores con cinco canales. No es relevante el elemento que se envía, sino el hecho de enviarlo.

```C
loop
	Think;
	forks[i] -> dummy;
	forks[i+1] -> dummy;
	Eat;
	forks[i] <- true;
	forks[i+1] <- true;
```

También necesitaremos un proceso por cada tenedor, que lo administre

```C
loop
	forks[i] -> true;
	forks[i] <- dummy;
```
