RustiShop es un sitio para que cualquiera pueda levantar una tienda por internet. Su proceso de *checkout* requiere conectarse con diferentes servicios:

- RustiPago para el cobro
- RustiStock para validar y asegurar el stock del producto
- RustiEnvios para planificar la entrega.

El *checkout* debe llevarse a cabo atómicamente, si cualquiera de los servicios falla o rechaza el pedido, se debe cancelar toda la operación.

## Solución

Para resolver esto, tendremos que utilizar él [[Transacciones#Lock de dos Fases|Locks de dos fases]] para bloquear los recursos antes de comenzar la operación. También se puede utilizar el algoritmo de [[Transacciones#Commit de dos Fases|Commit de dos fases]] para sincronizar el *commit* entre los servicios.
