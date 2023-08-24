Un sistema de base de datos provee un *data-definition language* (DDL), para especificar sus esquemas, y un *data-manipulation language* (DML), para expresar consultas y actualizaciones. En la práctica no son lenguajes separados; sino un único lenguaje, como SQL.

## Data-Definition Language

Especificamos la estructura de los datos y los métodos de acceso usados. Definen los detalles de implementación de nuestros esquemas. Los valores almacenados deben cumplir ciertas restricciones expresadas.

Los sistemas de bases de datos solo implementan restricciones que puedan ser verificadas sin mucha complicación:

- **Restricciones de Dominio:** Deben estar asociadas con cada atributo, al declarar un atributo como parte de un dominio particular estamos limitando los valores que puede tomar. Son el tipo más elemental de restricciones de integridad.
- **Integridad Referencial:** Hay casos donde debemos asegurarnos de que un valor aparezca en cierta relación para un conjunto dado de atributos
