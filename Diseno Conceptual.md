---
title: Diseño Conceptual
---

Un modelo de datos, debe incluir los siguientes elementos:

- Un conjunto de objetos, con sus propiedades e interrelaciones entre ellos.
- Un conjunto de operaciones, o lenguaje, que permite manipular los datos
- Restricciones sobre los objetos, las interrelaciones y las operaciones.

## Modelo Entidad-Interrelación

En inglés es conocido como *ER diagram (entity-relationship)*. También podemos utilizar otros modelos, como UML.

El modelo solo representa el diseño, y no los datos en sí. Tiene tres elementos principales:

- **Tipo de Entidad:** Es un tipo de clase a la cual pertenecen los objetos. Se representa con un rectángulo.
- **Atributo:** Propiedades de una clase, tienen un valor asociado en cada identidad. Se representa con un óvalo, conectado al tipo de entidad
- **Tipo de Interrelación:** Define una relación entre dos tipos de entidades. Se representa con un rombo conectado entre medio de ambos tipos de entidades. Puede contener sus propios atributos. La relación tiene una cardinalidad a cada lado.

El **conjunto de entidades** representa los datos del problema, son las instancias particulares de cada clase, con sus atributos asociados.

Cada atributo que se coloca a una entidad tiene un **dominio**, esto es, el *tipo de dato* del atributo. Representa qué valores posibles puede tomar. Algunos atributos permiten un valor nulo.

Los atributos compuestos se componen de atributos simples, y le dan un certificado particular a cada componente.

> [!example] Tarjeta de Crédito
> El número de una tarjeta de crédito puede ser separado en distintos componentes, cada uno otorgando información particular. Depende de la implementación si quiero o no separar esta información.

Los atributos **multi-evaluados** pueden tener más de un valor, pero esto trae problemas a nivel de implementación. Para atributos importantes, es mejor separarlo a su propio tipo de entidad.

Los atributos **derivados** son aquellos que pueden ser calculados a partir de los datos de la base de datos (de la propia entidad, o de otros elementos). Si decidimos almacenar o no estos atributos, dependerá de la implementación.

Toda entidad almacenada en la base de datos debe tener **atributos clave** que identifiquen inequívocamente cada entidad. Esto nos asegurará que no existan dos entidades iguales, ya que, a lo sumo, diferirán en su clave. Esta restricción se conoce como restricción de **unicidad**. En el diagrama esto se representa subrayando el atributo clave.

El conjunto de atributos clave debe ser **minimal**.

En las interrelaciones binarias, participan únicamente dos tipos de entidades. En las interrelaciones ternarias, pueden participar tres. De igual forma, existen las interrelaciones $n$-arias.

La cardinalidad puede tener un **mínimo** y un **máximo**, se representa como $(x,y)$ en cada lado de la relación. Si una entidad debe tener un vínculo con otra, entonces se dice que tiene una **dependencia existencial**.

Para modelar múltiples relaciones entre dos entidades, no es correcto modelarlo con múltiples asociaciones. Debemos crear una entidad nueva que represente esta interrelación. Luego, cada miembro de la relación tendrá, a su vez, una relación con esta entidad-relación.

Para identificar una relación inequívocamente, podemos utilizar los propios miembros de la relación como atributos clave. En el diagrama, esto se representa con una doble raya en la relación de la entidad-relación. Esto se conoce como **entidad débil**, ya que depende de la otra. Dependerá de un atributo externo, y algún atributo propio conocido como **discriminante**.




