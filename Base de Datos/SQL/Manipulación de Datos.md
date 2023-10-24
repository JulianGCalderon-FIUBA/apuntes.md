## Inserciones

Las inserciones se realizan con el comando `INSERT INTO`. Si no especificamos las columnas, debemos colocar todas y en el orden definido. Se deben respetar las restricciones definidas.

```SQL
INSERT INTO Tabla VALUES
	(a1, a2, ..., an),
	(b1, b2, ..., bn),
	...

INSERT INTO Tabla(Col1, Col2, ..., Col3) VALUES
	(a1, a2, ..., an),
	(b1, b2, ..., bn),
	...
```

También, podemos insertar el resultado de una subconsulta, con

```SQL
INSERT INTO T(Col1, Col2, ..., Col3)
SELECT ...
```

Si se alcanza a un error, se deshace la operación completa.

## Eliminaciones

El borrado se realiza con el comando `DELETE FROM`. Se deben respetar las restricciones definidas.

```SQL
DELETE FROM Tabla
WHERE ...
```

Si se alcanza a un error, se deshace la operación completa.

## Modificaciones

La actualización se realiza con el comando `UPDATE`. Se deben respetar las restricciones definidas.

```SQL
UPDATE Tabla
SET A1=c1, A2=c2, Ak=ck
WHERE ...
```

Se pueden modificar muchas filas con un solo `UPDATE`.

Si se alcanza a un error, se deshace la operación completa.
