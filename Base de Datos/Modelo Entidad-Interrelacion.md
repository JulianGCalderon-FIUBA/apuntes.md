---
title: Modelo Entidad-Interrelación
---

El modelo de **Entidad-Interrelación**, en inglés conocido como *ER diagram (entity-relationship)*, tiene tres elementos principales:

- **Tipo de Entidad:** Es un tipo de clase a la cual pertenecen los objetos. Se representa con un rectángulo.
- **Atributo:** Propiedades de una clase, tienen un valor asociado en cada identidad. Se representa con un óvalo, conectado al tipo de entidad
- **Tipo de Interrelación:** Define una relación entre dos tipos de entidades. Se representa con un rombo conectado entre medio de ambos tipos de entidades.

![[Modelo Entidad-Interrelacion 1.png|350]]

## Atributo

Cada entidad deberá tener valores para los atributos definidos para su tipo de identidad.

Cada atributo que se coloca a una entidad tiene un **dominio**, esto es, el *tipo de dato* del atributo. Representa qué valores posibles puede tomar. Algunos atributos permiten un valor nulo.

Los atributos compuestos se componen de atributos simples, y le dan un significado particular a cada componente. Los atributos que no son indivisibles se los denominan atributos *atómicos*.

> [!example] Tarjeta de Crédito
> El número de una tarjeta de crédito puede ser separado en distintos componentes, cada uno otorgando información particular. Depende de la implementación si quiero o no separar esta información.

Los atributos **multi-evaluados** pueden tener más de un valor, pero esto trae problemas a nivel de implementación. Para atributos importantes, es mejor separarlo a su propio tipo de entidad. En el diagrama, se representan con un doble óvalo.

![[Modelo Entidad-Interrelacion 2.png|450]]

Los atributos **derivados** son aquellos que pueden ser calculados a partir de los datos de la base de datos (de la propia entidad, o de otros elementos). En el diagrama, se representa con un óvalo punteado.

![[Modelo Entidad-Interrelacion 3.png|450]]

En algunos casos, una entidad puede no tener ningún valor particular para un atributo. En ese caso, el atributo admite un valor **nulo**. El significado de este valor dependerá del contexto.

Un atributo **complejo** es aquel que es compuesto, y a algunos de sus componentes son, a su vez, multi-evaluados.

## Entidades

El **conjunto de entidades** es el conjunto de ocurrencias o instancias de un determinado tipo de entidad en un estado determinado de la base de datos.

Un tipo de entidad representa el **esquema** o la intensión de un conjunto de entidades que comparten una la misma estructura.

El conjunto de todas las entidades de un mismo tipo de entidad se denomina su **extensión**.

Toda entidad almacenada en la base de datos debe tener **atributos clave** que identifiquen inequívocamente cada entidad. En el diagrama esto se representa subrayando los atributos clave.

![[Modelo Entidad-Interrelacion 4.png|475]]

Esto nos asegurará que no existan dos entidades iguales, ya que, a lo sumo, diferirán en su clave. Esta restricción se conoce como restricción de **unicidad**.

Si hay más de un atributo clave, entonces dicha combinación de atributos clave será única.

El conjunto de atributos clave debe ser **minimal**, aunque es posible que exista más de un conjunto de atributos clave posibles.

## Interrelaciones

Un tipo de interrelación define un conjunto de interrelaciones entre entidades de determinados tipos de entidad. No pueden existir dos interrelaciones iguales entre las mismas entidades.

La aridad o grado de una interrelación es la cantidad de tipos de identidad que participan en el mismo. En las interrelaciones binarias, participan únicamente dos tipos de entidades. En las interrelaciones ternarias, pueden participar tres. De igual forma, existen las interrelaciones $n$-arias.

Cada tipo de entidad que participa en una interrelación juega un **rol** particular en dicha interrelación. El nombre del rol nos lo indica.

Los roles suelen ser útiles en las interrelaciones recursivas, estas son aquellas que relacionan dos entidades del mismo tipo de entidad.

> [!example] Interrelaciones Recursivas
> Un ejemplo de interrelación recursiva es: "[Persona] es amiga de [Persona]"

La cardinalidad es la máxima cantidad de instancias de cada tipo de entidad que pueden relacionarse con una instancia concreta de los tipos de entidades restantes.

La participación es la mínima cantidad de instancias de cada tipo de entidad que deben relacionarse con una instancia concreta de los tipos de entidad restante. Si una entidad $A$ debe tener un vínculo con otra entidad $B$, entonces se dice $A$ que tiene una **dependencia existencial** o **participación total** en $B$, en caso contrario, tiene **participación parcial**. En el diagrama, se indicará como $(\min, \max)$

![[Modelo Entidad-Interrelacion 5.png|525]]

Las interrelaciones, a su vez, pueden contener atributos. En las interrelaciones $1{:}N$ o $1{:}1$, estos atributos pueden pertenecer a uno de los tipos de entidad. En las interrelaciones $N{:}N$, deben obligatoriamente pertenecer al tipo de interrelación.

![[Modelo Entidad-Interrelacion 6.png|525]]

En los tipos de interrelaciones también debemos identificar un conjunto de atributos clave. Solo pueden formar parte de él los atributos clave de los tipos de identidades que participan en la interrelación. La elección de atributos clave está fuertemente condicionada por la cardinalidad.

## Entidades Fuertes y Debiles

A veces, la identificación de una identidad depende de su interrelación con otra entidad, a la cual está **subordinada**. Esto se denotará con un rectángulo que englobe tanto el tipo de entidad como la relación que lo identifican.

![[Modelo Entidad-Interrelacion 7.png|525]]

Cuando una entidad depende de otra, se dice que es una entidad débil. Su clave se compone de las claves de sus entidades **identificadoras**, más algunos atributos propios, que se denominan **discriminantes**.

Obligatoriamente, el lado

Para modelar múltiples veces el mismo tipo de interrelación entre dos entidades, no es correcto modelarlo con múltiples interrelaciones. Debemos crear un tipo de entidad que represente esta interrelación. Luego, esta será una entidad débil que dependerá de sus participantes.

![[Modelo Entidad-Interrelacion 8.png|600]]

## Interrelaciones Ternarias

Son aquellas que participan tres tipos de identidad. Aquí, la cardinalidad de un tipo de relación determina la cantidad de instancias de interrelación en que puede aparecer, fijadas las instancias de los otros dos tipos de entidades

![[Modelo Entidad-Interrelacion 9.png|475]]

> [!example]
> Dado un cantante y una ronda, ¿cuántos jurados puede haber? Muchos, luego la cardinalidad del jurado es $N$

Notemos que para dos tipos de entidad cualesquiera de una interrelación ternaria, la cardinalidad de ambos lados siempre será $N$, ya que si no fuese el caso se podría prescindir de una interrelación ternaria, y utilizar una relación binaria.

## Agregación

En el diseño anterior, la existencia de cualquiera de las entidades es obligatoria. No puede no haber un jurado. Para permitir este comportamiento, se utilizan las agregaciones.

![[Modelo Entidad-Interrelacion 10.png|500]]

Participación es una entidad que representa la relación entre cantante y ronda. Luego, esta participación puede (o no) tener jurados (y, por lo tanto, puntaje)

## Generalización y Especialización

La generalización y la especialización nos permiten representar relaciones del tipo "es un" en el modelo de datos.

![[Modelo Entidad-Interrelacion 11.png|375]]

Los subtipos de entidad son subclases del tipo de entidad padre. A través de especialización, se heredan atributos y tipos de interrelaciones del tipo de entidad padre. A su vez, los subtipos de entidad pueden tener atributos propios.
