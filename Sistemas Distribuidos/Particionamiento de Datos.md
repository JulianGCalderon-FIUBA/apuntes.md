Los datos se pueden particionar por distintos motivos:

- **Performance**: Mejora de velocidad de escritura y de lectura, ya que puedo tener particiones específicas de escritura, y otras de lectura.
- **Conflictos**: Evita colisiones o reduce los conflictos.
- **Redundancia**: Permite recuperación ante fallas (al guardar las particiones en más de un lugar).

## Tipo de Particionamiento

Hay dos enfoques principales para realizar la partición de datos:

- **Horizontal**: La información se segrega por registros entre cada partición. Los registros se encuentran *completos* en alguna partición.
- **Vertical**: La información se segrega por atributos. Los registros se encuentran en todas las particiones, por lo que no son eficientes para consultas de filas completas.

## Función de Partición

La función de partición, que determine en que partición se encuentra cada dato, puede definirse de varias maneras:

- Por valor de Clave: Separa cada valor en una partición. Por ejemplo, tomo la primer letra del ID como partición.
- Por rango de Clave: Separa cada rango de valores en una partición.
- Por Hash: Se aplica el hash a la clave, para obtener una distribución más uniforme.

También hay enfoques mixtos, como:

- Generar múltiples particiones para un valor.
- Particionar por claves secundarias.

## Enrutamiento

Hay distintas formas de obtener un dato en una base de datos particionada:

- Si no conozco la función de partición, debo consultar en alguna de las particiones, y que esta me indique en que partición se encuentra.
- En algunos casos, existirá un nodo *centinela* que conocerá en que partición se encuentran los datos.
- Si conozco la función de particionamiento, puedo calcular en que partición se encuentra utilizando el dato.

![[Data Intensive Applications 1737301563.png]]
