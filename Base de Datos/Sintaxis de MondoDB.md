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

MongoDB no está pensado para realizar operaciones de junta en forma eficiente. En general, cuando necesitamos hacer una junta, la escribiremos a mano, como en el ejemplo anterior.

Si debemos acceder muy frecuentemente al documento referenciado, hay que pensar si no sería conveniente tenerlo directamente embebido.

La no redundancia de datos y la normalización la sacrificamos, ya que NoSQL, y MongoDB en particular rompen con el paradigma del modelo relacional.

A lo sumo, deberemos buscar documentos referenciados concretos para una consulta en particular. Esto se resuelve de forma eficiente gracias a la utilización de *hash*.

Desde la versión 3.2 de MongoDB, existe el comando *lookup*, que permite realiza la junta entre dos colecciones.

## Agregación

MongoDB implementa la agregación a través de un pipeline secuencial que combina etapas de agrupamiento, selección, etc. La función `agregate()` opera a partir de un vector de documentos JSON, en donde cada documento describe una operación.

```Python
result = col_clientes . aggregate ( [
	{ "$group": {"_id": "$localidad", "cantidad": { "$sum": 1 } } },
	{ "$match": {"cantidad": { "$lte": 1 } } } ])

for cliente in result:
	pprint.pprint( cliente )
```

El pipeline de agregación de MongoDB ofrece las siguientes operaciones, entre otras:

- `match`: Filtrado de resultados.
- `group`: Agrupamiento de los resultados por uno o más atributos, aplicando funciones de agregación.
- `sort`: Ordenamiento de resultados.
- `limit`: Limitado de resultados.
- `sample`: Selección aleatoria de resultados.
- `unwind`: Deconstrucción de un atributo de tipo vector. Se genera un documento nuevo completo por cada elemento del vector.

El conjunto de resultados que devuelve una operación será utilizado como entrada por la siguiente operación del *pipeline*.

Un mismo tipo de operación podría ser utilizado más de una vez dentro del pipeline.
