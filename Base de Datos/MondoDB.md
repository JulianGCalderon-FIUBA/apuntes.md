Es un gestor basado en *hashes* para identificar objetos. No utiliza esquemas, ni existe un [[Lenguajes#Data-Definition Language|DLL]].

Los documentos tienen un formato JSON, por lo que almacena pares de clave/valor.

Organiza los datos de una base de datos en colecciones, que contienen documentos. Los documentos a su vez tienen múltiples campos.

Fue desarrollada en C++, pero tiene APIs en múltiples lenguajes, como Python, Java, C#, etc.

Los atributos pueden ser multivaluados, ya que un vector es un tipo de dato valido.

## Creación de Documentos

Para la creación de documentos, debemos primero crear una base de datos, luego una colección, y finalmente agregarle un documento.

```Python
from pymongo import MongoClient
conn = MongoClient()

# Creamos una nueva base de datos
bd_empresa = conn.base_empresa

# Le agregamos una colección
col_clientes = bd_empresa.clientes

# Le agregamos un documento a la colección
cliente1 = {
	"nombre": "Mario",
	"apellido": "Wilkerson",
	"domicilio": "Av. Entre Ríos 1560"
}

id_cliente1 = col_clientes.insert_one(cliente1).inserted_id
```

Los documentos dentro de una colección se identifican a través de un campo `_id`. Si no lo indicamos, MongoDB asignará un *hash* de 12 bytes. La función `ObjectId(h)` convierte un hash en una referencia al documento que dicho hash identifica.

El hash también asegura que no se pueda insertar dos veces el mismo documento en una colección.

## Consultas

Las consultas se realizan con la función `find()` sobre la colección. El resultado es un cursor que debe ser iterado.

```Python
# Buscamos todos los clientes que son de Morón
respuesta_query = col_clientes .find ({" localidad ": "Morón"})

for c in respuesta_query:
	pprint.pprint(c)
```

## Documentos Embebidos vs. Referenciados

Podemos utilizar los `ObjectId` para referenciar objetos.

```Python
pedido1 = {
	"cod_pedido" : 78303 ,
	"cliente" : id_cliente2 ,
	"productos" : [{"producto": id_producto2 , "cantidad": 3}],
	"fecha_entrega_limite ": datetime . datetime (2017 , 6, 18),
	"entregado" : False 
}

pprint.pprint ( pedido1 )
```

En este caso, el documento relativo al cliente queda **referenciado** dentro del pedido. En cambio, el atributo productos contiene como valor un vector de documentos que se encuentran **embebidos** o anidados.

```Python
result = col_pedidos.find({"productos.producto": id_producto3 })

for cliente_id in result.distinct("cliente"):
	result2 = col_clientes.find ({"_id": cliente_id })
	for cliente in result2:
		pprint.pprint( cliente )
```

Como `producto` está embebido, podemos utilizar `.` para indicar el subatributo. En cambio, como `cliente` es un documento referenciado, debemos hacer una subconsulta para ir a buscar sus datos.

## Juntas

MongoDB no está pensado para realizar operaciones de junta en forma eficiente. En general, cuando necesitamos hacer una junta la escribiremos a mano, como en el ejemplo anterior.

Si debemos acceder muy frecuentemente al documen