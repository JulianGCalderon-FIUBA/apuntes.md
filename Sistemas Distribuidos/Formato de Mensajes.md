Existen distintos formatos para mensajes

- Binario
- Texto

## Binario

Los formatos binarios son más eficientes. Comprimir no ayudará mucho.

Puede ser más difícil de serializar. Existen bibliotecas que lo hacen automáticamente (por ejemplo: protobuf).

Requieren de un cliente específico para cada aplicación, ya que cada formato será distinto. Dificulta la depuración.

## Texto

Los formatos son menos eficientes, pero podemos comprimirlos para mejorar el tamaño.

Son más fáciles de serializar. Podemos usar formatos human-readable.

El cliente puede ser único, ya que los formatos son conocidos (por ejemplo: curl).

## Longitud de Paquetes

- Longitud Fija:
  Podemos enviar paquetes de longitud fija. Son más fáciles de serializar
- Longitud variable:
  Tenemos que delimitar los distintos campos, ya sea con un elemento delimitador, o indicando el tamaño de los campos.
- Longitud mixta:
  Tendremos campos de longitud fija y longitud variable. Son los más comunes. Los campos variables necesitarán un delimitador, mientras que los otros no.

Un formato conocido para enviar paquetes variables es TLV: Type, Length, Value. El value puede contener subtipos.
