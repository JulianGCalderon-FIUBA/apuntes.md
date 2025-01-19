Para comunicar distintas computadoras, es necesario intercambiar mensajes.

## Formato de Mensajes

Hay dos variantes para el formato de mensajes, el formato **binario** y el formato de **texto plano**.

### Binario

Al tener control total sobre los bytes del mensaje, podemos usar una representación muy eficiente de almacenar y serialiar. En estos casos, la compresión puede noser necesaria.

Para la serialización, tendremos que implementar una solución a mano, o utilizar algún DSL para generar el código correspondiente, como por ejemplo: Google Protobuf, Thrift, ASN.1.

Para interactuar con el sistema, necesitaremos un cliente especifico para interpretar y enviar los mensjes.

### Texto Plano

Al estar limitados a caracteres de texto, la representación no es tan eficiente de almacenar y serializar. Debido a esto, la compresión puede dar grandes mejoras, aunque agrega overhead.

Al serializar, podemos utilizar implementaciones existentes para el formato que utilicemos, como por ejemplo: JSON, XML, HTTP, etc.

Para interactuar con el sistema, podremos usar un cliente genérico que conozca el protocolo, como por ejemplo: cURL o Postman. Debido a esto, es más fácil de *debugguear*.

## Longitud de Paquetes

Si el dato que queremos enviar tiene longitud fija, entonces podremos enviarlo directamente. Esto es más fácil de serializar, ya que siempre leemos la misma cantidad.

Si el dato no tiene longitud fija, entonces tenemos dos alternativas:

- Incluir un delimitador para denotar el comienzo de un nuevo campo.
- Incluir la longitud del campo al comienzo.

Ambas alternativas agregan un overhead de longitud en el mensaje.

En un esquema mixto, tendremos campos fijos y campos variables, por lo que algunos campos necesitarán delimitadores, mientras que otros no.

Un ejemplo típico que funciona para muchos casos, es el esquema **TLV** (*type*, *length*, *value*).
