La recuperación consiste en, tras un error, llevar el sistema a un estado correcto. Una forma de lograrlo es:

- **Almacenamiento estable**: En primer lugar, necesitamos un almacenamiento seguro.
- **Checkpoints**: Se guarda periódicamente el estado completo del sistema en almacenamiento estable. De esta forma, podemos volver a un escenario previo al fallo.
- **Message logging**: Se parte de un checkpoint válido y se repiten todos los mensajes intercambiados desde ese checkpoint.
- **Consenso**: En caso de ser necesario, se acuerda entre los componentes vivos el estado correcto.

Estos mecanismos son costosos, pero es mejor que no tener ninguna forma de restaurar el sistema.
