Algunos principios de la abstracción de datos son:

- **Encapsulamiento:** Con un TDA buscamos encapsular ciertos atributos o comportamientos en una estructura.
- **Composición:** Los TDA pueden contener dentro a otros TDA, luego estar compuestos.
- **Instanciación:** Un tipo de dato refiere una estructura, la cual puede ser *instanciada*.

## Categorización

Un tipo de dato abstracto, o TDA, puede ser categorizado según distintas características:

- **Abierto/Cerrado:** Se dice que es abierto cuando su representación interna es accesible
- **Con/Sin Estado:** Se dice que tiene estado cuando tiene variables internas que puede mutar.
- **Empaquetado/No Empaquetado:** Se dice que es empaquetado cuando sus funciones sabe con qué datos aplicarse, o si debemos especificarlo.

## Implementación de Stack

En Oz, la implementación más simple de un Stack es: **abierto**, **sin estado**, y **no empaquetado**.

```Oz
fun {NewStack} nil end  
fun {Push S E} E|S end  
fun {Pop S E}
	case S of X|S1 then E=X S1 end  
end  
fun {IsEmpty S} S==nil end
```

Si queremos que tenga **estado**, entonces debemos utilizar celdas.

```Oz
fun {NewStack} {NewCell nil} end
proc {Push S E} S := E|@C end
proc {Pop S ?E}
	case @S of X|S1 then
		E = X
		S := S1
	end
end
fun {IsEmpty S} @S == nil end
```

Si queremos que sea **empaquetado**, entonces tenemos que crear un registro con sus propios métodos. Esta implementación además es **cerrada**. Si ahora queremos hacerlo **abierto**, entonces basta con agregar la celda en el registro.

```Oz
fun {NewStack}
	local S Push Popt IsEmpty in
		S = {NewCell nil}
		proc {Push E} C := E|@C end
		proc {Pop E}
			case @C of X|S1 then
				E = X
				C := S1
			end
		end
		fun {IsEmpty} @S == nil end
		stack(push:Push, pop:Pop, isEmpty:isEmpty)
	end
end
```

Si queremos hacerlo **sin estado**, tenemos que crear un nuevo registro luego de cada operación. Nuevamente, la implementación es **cerrada**, pero para hacerla **abierta** basta con agregar el estado interno al registro.

```Oz
fun {NewStack}
	local StackOperations in
		fun {StackOperations S}
			local Push Pop IsEmpty in
				proc {Push E} {StackOperations E|S} end
				proc {Pop E}
					case S of X|S1 then
						E = X
						{StackOperations S1}
					end
				end
				fun {IsEmpty} S == nil end
				stack(push:Push, pop:Pop, isEmpty:isEmpty)
			end
		end
		{StackOperations nil}
	end
end
```

Si queremos una implementación **no empaquetada** y **cerrada**, necesitamos tener una clave para pseudo-encriptar el estado. Envolvemos el valor en algo que solo desde dentro de la función se puede desencriptar.

```Oz
proc {NewWrapper Wrap UnWrap}
	local Key in 
		Key = {NewName}
		fun {Wrap X}  
			fun {$ K}  
				if (K==Key) then X end  
			end  
		end  
		fun {Unwrap W}  
			{Wrap Key}  
		end
	end
end
```

Una vez tenemos esta estructura, podríamos utilizarla en nuestra implementación de Stack, **no empaquetado** y **cerrado**.

```Oz
fun {StackOperations}
	local Wrap Unwrap NewStack Push Pop IsEmpty in
		{NewWrapper Wrap UnWrap}
		fun {NewStack} {Wrap nil} end  
		fun {Push S E} {Wrap E|{Unwrap S}} end  
		fun {Pop S E}
			case {Unwrap S} of X|S1 then 
				E=X
				{Wrap S1}
			end  
		end  
		fun {IsEmpty S} {Unwrap S}==nil end
		stack(new:NewStack, push:Push, pop:Pop, isEmpty:isEmpty)
	end
end
```

## Capabilities

Un cómputo es seguro si está claramente definido, independiente de la existencia de otros.

Una **capability** es un *token* asociado a un objeto, que da autoridad para usarlo. Son parte escencial en "lenguajes seguros". `Wrap/Unwrap` son usados como tal.
