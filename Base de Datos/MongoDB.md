Es un gestor basado en *hashes* para identificar objetos. No utiliza esquemas, ni existe un [[Lenguajes#Data-Definition Language|lenguaje de definición de datos]].

Fue desarrollada en C++, pero tiene APIs en múltiples lenguajes, como Python, Java, C#, etc.

Utiliza un modelo distribuido de procesamiento conocido como [[Modelo Sharding]].

## Estructura

Una base de datos está formada por colecciones, las cuales almacenan documentos.

Los documentos tienen un formato JSON, por lo que almacena pares de clave/valor. Organiza los datos de una base de datos en colecciones, que contienen documentos. Los documentos a su vez tienen múltiples campos.

Los atributos pueden ser multivaluados, ya que un vector es un tipo de dato válido.

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

## Consultas

Las consultas se realizan con la función `find()` sobre una colección. El resultado es un cursor que debe ser iterado

```Python
# Buscamos todos los clientes que son de Morón
respuesta_query = col_clientes.find ({" localidad ": "Morón"})

for c in respuesta_query:
	pprint.pprint(c)
```

## Claves

Los documentos dentro de una colección se identifican a través de un campo `_id`. Si nosotros no lo especificamos, entonces se asignará automáticamente.

El hash también asegura que no se pueda insertar dos veces el mismo documento en una colección.

Los documentos a su vez pueden referenciar otros documentos a través de esta clave, conocida como `ObjectId`. Por otro lado, los documentos pueden anidar otros documentos dentro del mismo.

```Python
pedido1 = {
	"cod_pedido" : 78303 ,
	"cliente" : id_cliente2 ,
	"productos" : [{"producto": id_producto2 , "cantidad": 3}],
	"fecha_entrega_limite ": datetime.datetime (2017 , 6, 18),
	"entregado" : False 
}

pprint.pprint(pedido1)
```

## Juntas

MongoDB no está pensado para realizar operaciones de junta en forma eficiente. En general, cuando necesitamos hacer una junta, la escribimos a mano.

```Python
# Buscamos los clientes que pidieron el producto 3:
result = col_pedidos.find({"productos.producto": id_producto3 })

for cliente_id in result.distinct ("cliente"):
	result2 = col_clientes.find ({"_id": cliente_id })
	for cliente in result2:
		pprint.pprint(cliente)
```

A lo sumo, deberiamos ir a buscar documentos referenciados concretos para una consulta particular, pero esto es rápido debido al *hashing*.

Si debemos acceder muy frecuentemente a un documento referenciado, hay que pensar si no sería conveniente tenerlo directamente embebido.

La no redundancia de datos y la normalización es sacrificada en las bases de datos NoSQL, y MongoDB en particular.

## Agregación

MongoDB implementa agregación a través de un *pipeline* secuencial que combina etapas de agrupamiento, selección, etc. El conjunto de resultados que devuelve una operación será utilizado como entrada por la siguiente operación.

```Python
result = col_clientes.aggregate ( [
	{ "$group": {"_id": "$localidad", "cantidad": { "$sum": 1 } } },
	{ "$match": {"cantidad": { "$lte": 1 } } } ])

for cliente in result:
	pprint.pprint(cliente)
```

El pipeline de agregación de MongoDB ofrece las siguientes operaciones, entre otras:

- `match`: Filtrado de resultados.
- `group`: Agrupamiento de los resultados por uno o más atributos, aplicando funciones de agregación.
- `sort`: Ordenamiento de resultados.
- `limit`: Limitado de resultados.
- `sample`: Selección aleatoria de resultados.
- `unwind`: Deconstrucción de un atributo de tipo vector. Se genera un documento nuevo completo por cada elemento del vector.

Un mismo tipo de operación podría ser utilizado más de una vez dentro del pipeline.
