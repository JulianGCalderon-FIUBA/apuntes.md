El programa copia datos que no controla en un buffer, sin verificar que la memoria asignada sea suficiente.

Esto puede causar desde corrupción de datos hasta la ejecución de código arbitrario, debido a que las variables y la dirección de retorno de una función se guardan en la misma zona de memoria.

Si el desbordamiento sucede accidentalmente, lo más probable es que el programa intente acceder a una posición de memoria sobre la cual no tiene permisos, reciba una señal de violación de memoria, y termine.

Si el desbordamiento es provocado por un atacante que conoce la organización del proceso en memoria, este puede llegar a controlar el flujo de programa.

Para más información, ver [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
