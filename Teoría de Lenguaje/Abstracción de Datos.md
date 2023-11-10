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

En Oz, podemos implementar un TDA Stack, no empaquetado, abierto, y sin estado.

```Oz
fun {NewStack} nil end  
fun {Push S E} E|S end  
fun {Pop S E} 
	case S of X|S1 
	then E=X S1 
	end  
end  
fun {IsEmpty S} S==nil end
```
