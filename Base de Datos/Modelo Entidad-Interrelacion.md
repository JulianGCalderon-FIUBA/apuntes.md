---
title: Modelo Entidad-Interrelación
---

El modelo de **Entidad-Interrelación**, en inglés conocido como *ER diagram (entity-relationship)*, tiene tres elementos principales:

- **Tipo de Entidad:** Es un tipo de clase a la cual pertenecen los objetos. Se representa con un rectángulo.
- **Atributo:** Propiedades de una clase, tienen un valor asociado en cada identidad. Se representa con un óvalo, conectado al tipo de entidad
- **Tipo de Interrelación:** Define una relación entre dos tipos de entidades. Se representa con un rombo conectado entre medio de ambos tipos de entidades.

![[Untitled.png|400]]

## Atributo

Cada entidad deberá tener valores para los atributos definidos para su tipo de identidad.

Cada atributo que se coloca a una entidad tiene un **dominio**, esto es, el *tipo de dato* del atributo. Representa qué valores posibles puede tomar. Algunos atributos permiten un valor nulo.

Los atributos compuestos se componen de atributos simples, y le dan un certificado particular a cada componente.

> [!example] Tarjeta de Crédito
> El número de una tarjeta de crédito puede ser separado en distintos componentes, cada uno otorgando información particular. Depende de la implementación si quiero o no separar esta información.

Los atributos **multi-evaluados** pueden tener más de un valor, pero esto trae problemas a nivel de implementación. Para atributos importantes, es mejor separarlo a su propio tipo de entidad. En el diagrama, se representan con un doble óvalo.

![[Pasted image 20230822205456.png|425]]

Los atributos **derivados** son aquellos que pueden ser calculados a partir de los datos de la base de datos (de la propia entidad, o de otros elementos). En el diagrama, se representa con un óvalo punteado.

![[Pasted image 20230822205509.png|425]]

## Entidades

El **conjunto de entidades** es el conjunto de ocurrencias o instancias de un determinado tipo de entidad en un estado determinado de la base de datos.

Toda entidad almacenada en la base de datos debe tener **atributos clave** que identifiquen inequívocamente cada entidad. Esto nos asegurará que no existan dos entidades iguales, ya que, a lo sumo, diferirán en su clave. Esta restricción se conoce como restricción de **unicidad**. En el diagrama esto se representa subrayando los atributos clave.

![[Pasted image 20230822205950.png|425]]

El conjunto de atributos clave debe ser **minimal**, aunque es posible que exista más de un conjunto de atributos clave posibles.

## Interrelaciones

La aridad o grado de una interrelación es la cantidad de tipos de identidad que participan en el mismo.

En las interrelaciones binarias, participan únicamente dos tipos de entidades. En las interrelaciones ternarias, pueden participar tres. De igual forma, existen las interrelaciones $n$-arias.

La cardinalidad es la máxima cantidad de instancias de cada tipo de entidad que pueden relacionarse con una instancia concreta de los tipos de entidades restantes.

La participación es la mínima cantidad de instancias de cada tipo de entidad que deben relacionarse con una instancia concreta de los tipos de entidad restante. Si una entidad $A$ debe tener un vínculo con otra entidad $B$, entonces se dice $A$ que tiene una **dependencia existencial** o **participación total** en $B$, en caso contrario, tiene **participación parcial**. En el diagrama, se indicará como $(\min, \max)$

![[Pasted image 20230822210401.png|450]]

Las interrelaciones, a su vez, pueden contener atributos:

![[Pasted image 20230822210627.png|450]]

En los tipos de interrelaciones también debemos identificar un conjunto de atributos clave. Solo pueden formar parte de él los atributos clave de los tipos de identidades que participan en la interrelación. La elección de atributos clave está fuertemente condicionada por la cardinalidad.

---

Para identificar una relación inequívocamente, podemos utilizar los propios miembros de la relación como atributos clave. En el diagrama, esto se representa con una doble raya en la relación de la entidad-relación. Esto se conoce como **entidad débil**, ya que depende de la otra. Dependerá de un atributo externo, y algún atributo propio conocido como **discriminante**.

## Entidades Fuertes y Debiles

A veces, la identificación de una identidad depende de su interrelación con otra entidad, a la cual está **subordinada**. Esto se denotará con un rectángulo que englobe tanto el tipo de entidad como la relación que lo identifican.

![[Pasted image 20230822211305.png|575]]

Cuando una entidad depende de otra, se dice que es una entidad débil. Su clave se compone de las claves de sus entidades **identificadoras**, más algunos atributos propios, que se denominan **discriminantes**.

Para modelar múltiples veces el mismo tipo de interrelación entre dos entidades, no es correcto modelarlo con múltiples interrelaciones. Debemos crear un tipo de entidad que represente esta interrelación. Luego, esta será una entidad débil que dependerá de sus participantes.

![[Pasted image 20230822211627.png|625]]

## Interrelaciones Ternarias

Son aquellas que participan tres tipos de identidad. Aquí, la cardinalidad de un tipo de relación determina la cantidad de instancias de interrelación en que puede aparecer, fijadas las instancias de los otros dos tipos de entidades

![[Pasted image 20230822211921.png|500]]

> [!example]
> Dado un cantante y una ronda, ¿cuántos jurados puede haber? Muchos, luego la cardinalidad de jurado es $N$

Notemos que para dos tipos de entidad cualesquiera de una interrelación ternaria, la cardinalidad de ambos lados siempre será $N$, ya que si no fuese el caso se podría prescindir de una interrelación ternaria, y utilizar una relación binaria.

## Agregación

En el diseño anterior, la existencia de cualquiera de las entidades es obligatoria. No puede no haber un jurado. Para permitir este comportamiento, se utilizan las agregaciones.

![[Pasted image 20230822212245.png|500]]

Participación es una entidad que representa la relación entre cantante y ronda. Luego, esta participación puede (o no) tener jurados (y, por lo tanto, puntaje)

## Generalización y Especialización

La generalización y la especialización nos permiten representar relaciones del tipo "es un" en el modelo de datos.

![[Pasted image 20230822212443.png|425]]

Los subtipos de entidad son subclases del tipo de entidad padre. A través de especialización, se heredan atributos y tipos de interrelaciones del tipo de entidad padre. A su vez, los subtipos de entidad pueden tener atributos propios.
