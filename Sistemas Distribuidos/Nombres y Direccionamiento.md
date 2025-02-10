Los **nombres** permiten inequívocamente a una entidad dentro de un sistema. Deben describir a la entidad. Abstraer al recurso de las propiedades que lo atan al mismo con el sistema (lugar geográfico, dirección de red)

El **direccionamiento**, o _addressing_, es la relación entre un **nombre** y una **dirección**. La dirección puede cambiar, pero el nombre no. La dirección puede ser reutilizada por otros servicios.

Algunos ejemplos de la diferencia entre estos conceptos:

- Es una red local, la dirección IP identifica a un nodo, y su para llegar a él necesitamos la dirección Ethernet.
- El nombre de dominio identifica a una página web, mientras que para llegar a él necesitamos la dirección IP. El protocolo que ofrece esta traducción es DNS.

Existen servicios de _service discovery_ que permiten hallar la dirección de una entidad a partir de su nombre.
