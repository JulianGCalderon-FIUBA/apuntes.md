---
title: Fragmentación
---

El MTU *(maximum transmission unit)* es el máximo tamaño de un paquete de datos que se puede transferir en IP. Si el paquete completo tiene un tamaño mayor al MTU, se deberá fragmentar.

Los paquetes no son reensamblados en el camino, sino en el host de destino. Si se pierde un fragmento, IP descartará el paquete completo.

Los headers de IP tienen tres campos utilizados para la fragmentación:

- **Identification:** Es un número de 16 bits que identifica cada paquete, permite definir de qué paquete provienen los fragmentos
- **Flags:** Son tres bits, el primero no es utilizado, siempre valdrá cero.
	- El segundo es el bit *Do Not Fragment*. Si vale uno, el paquete será descartado, si es necesario fragmentarlo
	- El tercer bit es el *More Fragments*. Vale cero si es el último fragmento de un paquete.
- **Fragment Offset:** Número de 13 bits que determina la posición del primer bit del fragmento con relación al paquete completo. Debido a que tenemos 3 bits menos, la posición real se obtiene tras multiplicar el *offset* por $2^3=8$. Debido a esto, el tamaño de *payload* de los fragmentos debe ser múltiplo de 8.

## Método de Fragmentación

1. Si el tamaño del **datagrama** $D$ (incluye *headers*) es mayor al $MTU$, debemos fragmentar.
2. Calculamos el tamaño del *payload* $P$ (sin headers) como:

	$$
    P = D -  \underbrace{\text{Header IP}}_\text{20}
    $$

3. Calculamos el máximo tamaño de *fragment payload* $FP$ permitido, como:

	$$
    \max FP = MTU - \text{Header IP}
    $$

4. Como nuestro fragmento debe tener un tamaño múltiplo de 8, entonces debemos hallar el máximo valor permitido múltiplo de 8, este será:

	$$
    FP = \bigg\lfloor\frac{\max FP}8\bigg\rfloor\cdot 8
    $$

5. A partir del nuestro *fragment payload size*, podremos calcular la cantidad de fragmentos que debemos enviar como

	$$
    \#\text{Fragments} = \bigg\lceil\frac{P}{FP}\bigg\rceil
    $$

6. Construiremos un fragmento con *payload size* $FP$, *datagram size* $FP + \text{Header IP}$, y *fragment offset* de 0.
7. Repetiremos el procedimiento para el resto de fragmentos que se necesitan enviar. El tamaño de todos los fragmentos enviados será el mismo $(P)$ excepto el último, que tendrá un tamaño menor (o igual). Los *fragment offset* incrementarán linealmente a razón de $P/8$ por cada fragmento enviado. El último fragmento tendrá el bit de *More Fragments* en 0. Lógicamente, todos los paquetes tendrán el bit de *Do Not Fragment* en 0.
