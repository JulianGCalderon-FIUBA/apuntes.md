Ante cada acceso a un objeto, se deben verificar antes los derechos de acceso del sujeto:

- Si el permiso se verificó antes, y el sujeto tenía permiso, se debe volver a verificar.
- La mayor parte de los sistemas operativos no implementan este principio hasta donde deberían (un archivo abierto para el que se revocan los permisos de lectura podrá seguir siendo leído).
