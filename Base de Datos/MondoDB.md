Es un gestor basado en *hashes* para identificar objetos. No utiliza esquemas, ni existe un [[Lenguajes#Data-Definition Language|DLL]].

Los documentos tienen un formato JSON, por lo que almacena pares de clave/valor.

Organiza los datos de una base de datos en colecciones, que contienen documentos. Los documentos a su vez tienen múltiples campos.

Fue desarrollada en C++, pero tiene APIs en múltiples lenguajes, como Python, Java, C#, etc.

Los atributos pueden ser multivaluados, ya que un vector es un tipo de dato valido.

## Creación de Documentos

```Python
from pymongo import MongoClient
conn = MongoClient()

conn.database_names()

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

id_clie
```