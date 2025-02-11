En este sistema, los servidores ya no proveen servicios sino objetos. Existe un middleware que oculta la complejidad:

- Referencias a objetos remotos.
- Invocación de acciones sobre objetos.
- Manejo de errores o excepciones.
- Recolección de basura.

![[Objetos Distribuidos 1739233497.png]]

Los objetos pueden estar replicados, o migrarse de una réplica a otra.

A diferencia de en [[Remote Procedure Control]], en los objetos hay estado de llamadas previas, y es relevante con cuál replica se comunica.

Un ejemplo de objetos distribuidos es CORBA, aunque está en vías de deprecación. Otro ejemplo es RMI, que es un mecanismo de Java que ofrece invocaciones remotas. Cuenta con un directorio de servicios que es consultado por el cliente, quien luego realiza invocaciones al servicio que desea.
