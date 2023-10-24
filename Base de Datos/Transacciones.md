Podemos definir una [[Transacción]] con:

```SQL
START TRANSACTION [ ISOLATION LEVEL ...]
.... (sql commands)
COMMIT | ROLLBACK
```

También, podemos establecer el [[Anomalías#Niveles de Aislamiento|nivel de aislamiento]] de la transacción con:

```SQL
SET TRANSACTION ISOLATION LEVEL
READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SERIALIZABLE ;
```
