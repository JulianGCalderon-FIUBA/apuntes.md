## Principios

Algunos principios básicos que son utilizados en la programación orientada a objetos son:

- **SOLID:** Es un acrónimo para.
	- **SIngle Responsibility.**
	- **Open / Closed:** Abierto para agregar funcionalidad, y cerrado para modificarla.
	- **Liskov Substitution:** Se debería poder representar cualquier objeto por un subtipo.
	- **Interface Segregation:** Los comportamientos se deberían separar en interfaces.
	- **Dependency Inversion:** No debemos depender de implementaciones, sino de interfaces.
- **GRASP:** Es un acrónimo para *"General responsibility assignment software patterns"*.
	- **Polimorfismo.**
	- **Alta cohesión:** Los elementos de una misma clase deben estar muy relacionadas entre sí.
	- **Bajo acoplamiento:** Los objetos no deben depender mucho de otras clases.

## Tipado

El tipado puede ser según cuando se define: **dinámico** o **estático**.

El tipado puede ser según cómo se define: **implícito** (inferido), o **explicito**.

Cuando hablamos de objetos, tenemos que definir que tan especifico es el tipado:

- **Nominal:** Se guarda no solo el tipo de dato, sino además la jerarquía.
- **Estructural:** No se guarda la jerarquía, sino solo las implementaciones. Si cumple con cierta implementación, entonces cumple con cierta interfaz. Se define en tiempo de compilación.
- **Duck Typing:** Igual que estructural, pero se define en tiempo de ejecución.

## Objetos

Definiremos un objeto como una función con memoria interna. Esta memoria interna debe ser mutable, por lo que recurriremos al [[Estado Explícito]].

Las funciones capturan su entorno, a partir del concepto de [[Scoping]]

```Oz
declare C Bump

C = {NewCell 0}
Bump = proc {$}
	C := @C + 1
end

Read = fun {$}
	@C
end
	
{Browse {Read}} % 0
{Bump}
{Browse {Read}} % 1
```

## Clases

Las clases nos permiten tener múltiples instancias de un mismo objeto. Una clase es una fábrica de objetos.

```Oz
declare NewCounter Counter1 Counter2

NewCounter = fun {$}
	local C Bump Read in
		C = {NewCell 0}
		Bump = proc {$}
			C := @C + 1
		end
		Read = fun {$}
			@C
		end
		counter(bump:Bump read:Read)
	end
end

Counter1 = {NewCounter}
Counter2 = {NewCounter}

{Browse {Counter1.read}} % 0
{Counter1.bump}
{Browse {Counter1.read}} % 1

{Browse {Counter2.read}} % 0
```

## Herencia

La herencia ocurre cuando una clase extiende a otra clase, heredando sus propiedades y métodos.

## Mixin

Un *mixin* es una clase que existe solamente para agregar comportamiento a otros a través de composición o herencia. A veces se conoce como **trait**. Se usan para herencia múltiple.

## Delegation & Forwarding

La herencia no es el único mecanismo de extender funcionalidad.

- **Delegation:** Se define en los objetos, en lugar de las clases. Permite extender la funcionalidad de una instancia particular.
- **Forwarding:** Se define sobre la instancia, pero no comparten los atributos del objeto original. Es externo. De esta forma, define a que otra instancia enviarle un mensaje que desconoce.
