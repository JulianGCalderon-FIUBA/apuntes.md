Un numero binario en representación es aquel que indica su signo con el primer digito. Si el primer digito es un $0$, el numero es positivo. Si el primer digito es un $1$, el numero es negativo.

Si trabajando con determinado numero de bits, el numero obtenido luego de una suma es demasiado grande, obtendremos un **overflow**. Se indica con un cambio de signo en el primer bit. (flag V)

En el caso de los naturales, esto se indica con el digito extra en el **carry.**

Si quiero sumar dos números con diferentes cantidades de bits, entonces debo extender el primer bit tantas posiciones como sea necesario. Esto se hace para contemplar si es negativo o positivo.

## Convenciones

- **Magnitud y Signo:** Se leen todos los dígitos salvo el primero. El primer digito indica el signo
- **Complemento a la 1:** Se debe aplicar complemento a la 1 y leer todos los dígitos menos el primero. El primer digito antes del complemento indica el signo.
- **Complemento a la 2:** Se debe aplicar complemento a la 2 y leer todos los dígitos menos el primero. El primer digito antes del complemento indica el signo.

	En la convenció de complemento a 2, se pueden realizar operaciones de suma. Además, el rango de valores es mayor. $[-2^{n-1};2^{n-1}-1]$
