## Copiar

El comando `COPY` de SQL (PostgreSQL) permite copiar una tabla y exportarla en (o importarla desde) formato de texto plano.

Es importante notar que la expresión será ejecutada desde el lado del servidor, por lo que se guardara en el sistema de archivos de la base de datos. Para hacerlo desde el lado del cliente, entonces usamos el comando de `psql` llamado: `\copy`.

Si el comando se ejecuta desde una *query tool* de pgAdmin, la importación será relativa desde la carpeta de *data* de PostgreSQL.

```PostgreSQL
COPY teams
FROM 'dataset/teams.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';
```

La exportación, por otro lado, es siempre absoluta.

``` PostgreSQL
COPY teams
TO '/var/lib/postgresql/data/dataset/teams2.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';
```

## Importar

Para importar una base de datos, primero debemos crear la base de datos en la cual cargar la información:

```bash
createdb -U admin -T template0 schooldb
```

Utilizamos `template0`, ya que `template1` puede tener información personal que no queremos en nuestra base de datos.

Luego, realizamos la importación:

```bash
pg_dump -U admin -d schooldb < schooldb.sql
```

Si queremos exportar en archivo no de texto plano, podemos utilizar `-F`, seguido de un tipo de archivo, para indicar un formato particular:

```bash
pg_dump -U admin -d schooldb -F c > schooldb.dump
```

Para exportar en format *tar*, usamos:

```bash
pg_dump -U admin -d schooldb -F t > schooldb.tar
```

## Exportar

Para exportar, basta con usar `psql` de la base de datos:

```bash
psql -U admin -d schooldb > schooldb.sql
```

Para exportar de un formato no de texto plano, entonces utilizamos `pg_restore`:

```bash
pg_restore -U admin -d schooldb schooldb.dump
pg_restore -U admin -d schooldb schooldb.tar
```
