Para comunicar distintas computadoras, es necesario intercambiar mensajes.

## Formato

Hay dos variantes para el formato de mensajes, el formato **binario** y el formato de **texto plano**.

### Binario

Al tener control total sobre los bytes del mensaje, podemos usar una representación muy eficiente de almacenar y serialiar. En estos casos, la compresión puede noser necesaria.

Para la serialización, tendremos que implementar una solución a mano, o utilizar algún DSL para generar el código correspondiente, como por ejemplo: Google Protobuf, Thrift, ASN.1.

Para interactuar con el sistema, necesitaremos un cliente especifico para interpretar y enviar los mensjes.

### Texto Plano

Al estar limitados a caracteres de texto, la representación no es tan eficiente de almacenar y serializar. Debido a esto, la compresión puede dar grandes mejoras, aunque agrega overhead.

Al serializar, podemos utilizar implementaciones existentes para el formato que utilicemos, como por ejemplo: JSON, XML, HTTP, etc.

Para interactuar con el sistema, 
