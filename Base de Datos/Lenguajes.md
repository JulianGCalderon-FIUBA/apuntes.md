Un sistema de base de datos provee un *data-definition language* (DDL), para especificar sus esquemas, y un *data-manipulation language* (DML), para expresar consultas y actualizaciones. En la práctica no son lenguajes separados; sino un único lenguaje, como SQL.

## Data-Definition Language

Especificamos la estructura de los datos y los métodos de acceso usados. Definen los detalles de implementación de nuestros esquemas. Los valores almacenados deben cumplir ciertas restricciones expresadas.

Los sistemas de bases de datos solo implementan restricciones que puedan ser verificadas sin mucha complicación:

- **Restricciones de Dominio:** Deben estar asociadas con cada atributo, al declarar un atributo como parte de un dominio particular estamos limitando los valores que puede tomar. Son el tipo más elemental de restricciones de integridad.
- **Integridad Referencial:** Hay casos donde debemos asegurarnos de que un valor aparezca en cierta relación para un conjunto dado de atributos. Por ejemplo: El atributo "nombre de departamento" en un curso debe coincidir con algún registro de la relación "departamento".
- **Autorización:** Queremos restringir los distintos usuarios de la base de datos a acciones particulares.

## Data-Manipulation Language

Existen dos tipos de DML:

- **Procedurales:** Requieren que el usuario especifique que información necesita, y como accederla
- **Declarativos:** Requiere que el usuario especifique que información necesita, pero sin especificar como accederla.

Los lenguajes declarativos son los más fáciles de aprender, pero requiere que el sistema descubra una forma eficiente de acceder a la información. Una **consulta** es una petición de cierta información de la base de datos. La porción del lenguaje que se encarga de esto se conoce como **lenguaje de consultas**.

Los lenguajes de consultas declarativos como [[SQL]] no son tan poderosos como una máquina de Turing universal. Existen algunas computaciones que no son posibles en estos lenguajes. Para hacerlas, necesitaremos de utilizar algún lenguaje de programación, utilizando consultas de SQL de por medio.
