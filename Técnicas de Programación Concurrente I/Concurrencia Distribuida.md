A partir de ahora, vamos a estudiar como implementar sistemas de concurrencia en ambientes distribuidos. Esto permite ejecutar un programa en diferentes computadoras.

## Exclusión Mutua Distribuida

Tenemos una sección crítica que puede ser ejecutada a la vez por un solo proceso dentro de todo el sistema. Para resolver esto de forma cent, necesitaremos la ayuda de un coordinador:

1. Un proceso es elegido como **coordinador**. Usualmente, es denominado *lider*.
2. Cuando un proceso quiere entrar a la sección crítica, envía un mensaje al coordinador.
3. Si no hay ningún proceso en la sección crítica, el coordinador envía una confirmación; si hay, el coordinador no envía respuesta hasta que se libere la sección crítica.
