Es un acrónimo que representa principios básicos para diseñar buen código.

## Single Responsibility Principle

Cada elemento debe tener uno y solo una responsabilidad. Si un elemento tiene varias responsabilidades, se podrá subdividir para respetar el principio.

## Open-Closed Principle

Código abierto para la extensión, pero cerrado para la modificación. Usualmente, se utiliza la herencia para poder extender el funcionamiento de una clase sin modificarla.

## Liskov Substitution Principle

En cualquier lugar del programa, una entidad padre deberá poder ser remplazada por su entidad hija, sin alterar el funcionamiento el programa.

Si una entidad debe reutilizar una parte del comportamiento, podemos utilizar composición en lugar de herencia.

## Interface Segregation Principle

Muchas interfaces pequeñas son mejores que una interfaz general, ya no obligan a las entidades implementar elementos que no necesita de una interfaz grande. Sinó unicamente las subentidades que requiere realmente.

La biblioteca estándar de Go es un buen ejemplo de este principio: https://pkg.go.dev/io@go1.22.1#pkg-types

## Dependency Inversion Principle

Se debe depender de las abstracciones, no de las implementaciones.
