Existen distintos formatos para mensajes

- Binario
- Texto

## Binario

Los formatos binarios son mas eficientes. Comprimir no ayudara mucho.

Puede ser mas dificil de serializar. Existen biblitoecas que lo hacen automaticamente (por ejemplo: protobuf).

Requieren de un cliente especifico para cada aplicacion, ya que cada formato sera distinto. Dificulta la depuración.

## Texto

Los formatos son menos eficientes, pero podemos comprimirlos para mejorar el tamaño.

Son mas faciles de serializar. Podemos usar formatos human-readable.

El cliente puede ser unico, ya que los formatos son conocidos (por ejemplo: curl).

## Longitud de Paquetes

- Longitud Fija:
  Podemos enviar paquetes de longitud fija. Son mas faciles de serializar
- Longitud variable:
  Tenemos que delimitar los distintos campos, ya sea con un elemento delimitador, o indicando el tamaño de los campos.
- Longitud mixta:
  Tendremos campos de longitud fija y longitud variable. Son los mas comunes. Los campos variables necesitaran un delimitador, mientras que los otros no.

Un formato conocido para enviar paquetes variables es TLV: Type, Length, Value. El value puede contener subtipos.
