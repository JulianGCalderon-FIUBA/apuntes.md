En este sistema, los servidores ya no proveen servicios sino objetos. Existe un middleware que oculta la complejidad:

- Referencias a objetos remotos.
- Invocación de acciones sobre objetos.
- Manejo de errores o excepciones.
- Recolección de basura.

A diferencia de en [[Remote Procedure Control]], en los objetos hay estado. Este cambio debe persistirse ante migración o replicación.

Un ejemplo de objetos distribuidos es CORBA, aunque está en vías de deprecación. Otro ejemplo es RMI, que es un mecanismo de Java que ofrece invocaciones remotas.
