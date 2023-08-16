---
title: Pilas, Colas y Listas
---

## Pila

Una pila es una estructura de datos, que agrupa elementos. En la pila, solo podemos leer el último elemento apilado, y no podemos leer el próximo hasta deshacernos de ese. **LIFO: "Last in, First Out"**

Funciones definidas para el TDA pila

- Crear *(create)*
- Apilar *(push)*
- Tope *(top)*
- Desapilar *(pop)*
- Destruir *(destroy)*
- Vacía *(is_empty)*

Cada TDA tiene un uso particular, no es útil usar una pila si vamos a querer estar accediendo a elementos que no están en la última posición.

### Implementación

Hay 3 formas de implementar la pila.

- **Vector Estático**: Es útil cuando sabemos de antemano el tamaño máximo que vamos a necesitar
- **Vector Dinámico:** Es útil cuando no sabemos de antemano el tamaño máximo que vamos a necesitar
- **Lista de Nodos Enlazados:** Es similar al caso anterior, con la excepción de que no necesitamos memoria contigua

	Un **nodo simple** es un tipo de dato que contiene un elemento, y una dirección de memoria que apunta al siguiente elemento. De esta forma, teniendo la dirección de un solo nodo, se puede acceder al resto.

## Cola

Una cola es una estructura de datos, en la que solo podemos leer el elemento más antiguo, y no podemos leer el próximo hasta deshacernos de ese. **FIFO: "First in, First Out"**

Funciones definidas para el TDA pila:

- Crear *(create)*
- Encolar *(enqueue)*
- Primero *(first)*
- Desencolar *(dequeue)*
- Destruir *(destroy)*
- Vacía *(is_empty)*

### Implementación

- **Vector Estático:** Como vamos a estar liberando elementos del principio, estas posiciones del vector ya no las usaríamos más. Por lo que deberíamos hacer algo con estos espacios de la memoria. Tenemos dos soluciones:
	- Desplazar los elementos a medida que vamos agregando nuevos.
	- **Cola circular:** Esta solución consiste en posicionar el tope del vector en la posición anterior del principio (elemento más antiguo). De esta forma, una vez que ocupamos el fin del vector, empezamos a posicionar elementos desde el inicio del vector hasta este tope.
- **Vector Dinámico:** En esta solución seguimos teniendo el mismo problema que antes, por lo que podemos considerar directamente el uso de un nodo enlazado.
- **Nodos Enlazados:** Consiste en guardar los nodos de la posición del principio y el final, y que cada nodo esté conectado con el siguiente. De esta forma, cuando encolamos un elemento modificamos el final, y cuando desencolamos modificamos el principio.

## Lista

Una lista es una estructura de datos, en la que podemos acceder a cualquier elemento, y puedo insertar elementos en cualquier posición.

Funciones definidas para el TDA lista:

- Crear *(create)*
- Insertar *(insert_at)*
- Buscar *(find)*
- Eliminar *(delete_at)*
- Vacía *(is_empty)*
- Destruir *(destroy*

### Implementación

Vamos a centrarnos únicamente en la implementación con nodos:

- **Simplemente Enlazada:** Se mantiene referencia al primer nodo, cada nodo apunta al elemento siguiente
- **Doblemente Enlazada**: Se mantiene referencia al primer nodo, cada nodo apunta tanto al elemento siguiente, como al elemento anterior. De esta forma, cuando tenemos que acceder al nodo anterior, podemos hacerlo rápidamente, en lugar de tener que recorrer la lista nuevamente.
- **Lista Circular:** Se mantiene la referencia al primer nodo, el último nodo guarda la referencia al primer nodo. Al tener un solo elemento, este elemento apunta a sí mismo. Puede ser tanto simple como doblemente enlazada.
