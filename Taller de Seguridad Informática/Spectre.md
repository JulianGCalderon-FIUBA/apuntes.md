Es una familia de vulnerabilidades basadas en la ejecución especulativa:

- Para maximizar performance, se trata de predecir la dirección de un salto y se adelanta su ejecución (sin leer realmente la dirección).
- Los procesos comparten los predictores de saltos y otras unidades de cada núcleo. Antes no lo hacían, pero cambiaron algunos supuestos, no lo vieron.
- El predictor de saltos indexa por la dirección virtual del salto, por lo que pueden provocarse colisiones. Es decir, que dos procesos salten a la misma dirección virtual
- Las instrucciones ejecutadas por error dejan trazas en el caché, por lo que se puede acceder a información sensible.

Hay varias formas de mitigar este tipo de ataque:

- Los saltos indirectos son susceptibles a ataques del tipo _spectre_. Se puede simular un _return_ al colocar la dirección del salto en el stack, y realizar un _return_.
- Utilizar instrucciones para prevenir la ejecución especulativa.

Para más información, ver [CWE-200](https://cwe.mitre.org/data/definitions/200.html) y [Spectre Attacks: Exploiting Speculative Execution](https://spectreattack.com/spectre.pdf).
