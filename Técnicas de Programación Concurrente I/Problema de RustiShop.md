RustiShop es un sitio para que cualquiera pueda levantar una tienda por internet. Su proceso de *checkout* requiere conectarse con diferentes servicios:

- RustiPago para el cobro
- RustiStock para validar y asegurar el stock del producto
- RustiEnvios para planificar la entrega.

El *checkout* debe llevarse a cabo atómicamente, si cualquiera de los servicios falla o rechaza el pedido, se debe cancelar toda la operación.
