El sistema no debería otorgar permisos basado en una sola condición, o al menos permisos importantes.

Por ejemplo, el comando `su`. Este comando permite que un usuario asuma los privilegios del administrador en una máquina UNIX, provisto:

- Que el usuario conozca la contraseña de *root*.
- Que el usuario pertenezca al grupo *wheel*.

Muchos sistemas no permiten que *root* se conecte remotamente.
