Permiten trabajar con una base de datos de forma cómoda y segura.

## Funciones Principales

Algunas de las funciones principales de un gestor de base de datos son:

- Permiten accesos a la base de datos por muchos usuarios de forma concurrente.
- Tiene operaciones atómicas que previenen errores
- Previene accesos no autorizados, o restringe el acceso a consultas particulares.
- Tiene un sistema de recuperación ante fallas.
- Tiene un [[Lenguajes|lenguaje de consultas]] (SQL) para buscar información efectivamente.
- Asegura la integridad de datos a través de restricciones que deben satisfacer los datos.
- Accede a la información de forma eficiente, sin necesidad de iterar.

## Transacciones

Supongamos que en nuestra base de datos tenemos cuentas de banco, y queremos realizar un depósito en una cuenta, y una extracción en otra.

Es esencial que una operación no sea interrumpida, u ocurre totalmente, o no lo hace. Esta característica de *todo o nada* se conoce como **atomicidad**.

El valor retirado de una cuenta, debe ser el agregado en otra cuenta, esto se conoce como **consistencia**.

Luego de una operación exitosa, los nuevos valores del balance deben persistir, a pesar de la posibilidad de una falla del sistema. Esto se conoce como **durabilidad**.

Una **transacción** es un conjunto de operaciones que realizan una única función lógica. Son una sola unidad, en términos de atomicidad y consistencia.

Asegurar estas propiedades es trabajo del sistema de la base de datos. Debe detectar fallas y recuperar el sistema ante una. Además, estas propiedades se deben mantener incluso ante acceso concurrente a la base de datos.

El **administrador de transacciones** se encargará tanto del *administrador de control de concurrencia*, y el *administrador de recuperación ante fallas*.

## Usuarios

Existen distintos tipos de usuarios, con capacidades y roles distintos.

El administrador de la base de datos, o *database administrator* (DBA) tiene control total de la información. Algunas de las funciones del administrador son:

- **Definición de Esquemas:** Crea o actualiza el esquema de la base de datos, ejecutando instrucciones en el DDL.
- **Definición de la Estructura:** Especifica parámetros relacionados con la organización física de los datos.
- **Autorizaciones:** Otorga autorizaciones específicas a cada usuario. Las autorizaciones pueden ser de lectura, inserción, actualización, y eliminación, así como acceso a partes específicas de la base de datos.
- **Rutinas de Mantenimiento:** Entre ellas, se encuentra:
	- Realizar copias de seguridad de forma periódica.
	- Asegurarse de que hay suficiente espacio en el disco.
	- Monitorizar tareas ejecutándose en la base de datos.

Al encargado de diseñar la arquitectura de una base de datos se le suele llamar **diseñador** de la base de datos.

## Historia

En los años 50, se reemplazaron los ficheros de información (físicos) por cintas magnéticas. Los datos frecuentemente se ingresaban con tarjetas perforadas. Estas cintas solo permitían acceso secuencial.

En los años 60 surgen los discos magnéticos, y con la posibilidad de acceso directo a los datos. Aquí surgen los primeros gestores de bases de datos:

- El IMS *(Information Management System)* de IBM utilizaba un modelo de datos jerárquico
- El IDS *(Integrated Data Store)* de General Electric utilizaba un modelo de datos en red.

En estos modelos, los datos estaban relacionados con modelos. Finalmente, en el año 72 se propuso el primer modelo relacional (teóricamente). No fue hasta los años 80 que surgieron las primeras implementaciones. Oracle fue el primero, y luego apareció PostgreSQL

En las bases de datos relacionales, los datos no se relacionan con punteros, sino con claves foráneas (no necesita iterar la información, sino indexarla). Con los punteros, el programador debía seguir los punteros (este trabajo luego fue asumido por los gestores).

> [!definition] Gestor de Base de Datos
> Es un conjunto de programas que gestiona y controla la creación, manipulación y acceso a la base de datos.

Esto permite abstraer el programa de los datos, permitiendo cambiar los datos sin romper los programas ya existentes.
