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

Si queremos que sea **empaquetado**, entonces tenemos que crear un registro con sus propios métodos. Esta implementación además es **cerrada**.

```Oz
fun {NewStack}
	local S Push Popt IsEmpty in
		S = {NewCell nil}
		proc {Push E} C := E|@C end
		proc {Pop ?E}
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

Si ahora queremos hacerlo **abierto**, entonces basta con agregar la celda en el registro. Si queremos sacarle el estado, tenemos que crear un nuevo registro luego de cada operación.
