Una vulnerabilidad es un defecto en un programa que permiten violar algún atributo de la seguridad de la información.

Se clasifican en:

- [[CWE]]: Common Weakness Enumeration.
- [[CVSS]]: Common Vulnerability Scoring System.
- [[CVE]]: Common Vulnerabilities and Exposures.

## Combatir vulnerabilidades

Hay distintas formas de combatir bugs de seguridad

Se pueden tratar de encontrar nuevas vulnerabilidades/bugs.

- Revisión de código.
- Pruebas de condiciones de contorno.
- Pruebas automatizadas.
- Análisis estático (sin ejecutar código).
- Análisis dinámico (durante la ejecución del programa).
- [[Penetration Test]]

Se pueden tratar de mitigar vulnerabilidades para no se puedan explotar más, o que sea más difícil hacerlo.

- W XOR X: Una página no puede ser escribible (W) o ejecutable (X) a la vez. Esto hace a los ataques de inyección de código más difíciles, pero no imposibles (ver ROP).
- Stack Canaries: valor secreto al comienzo del stack, para verificar al retornar que no sea alterado.
- CFI (Control Flow Integrity): el control de flujo del programa no puede cambiar una vez compilado.
- ASLR (Address Space Layout Randomization): aleatoriza la ubicación donde los ejecutables se cargan en memoria.
- Cambios de configuración para inhabilitar la funcionalidad que falla.

## Vulnerabilidades Comunes

- [[Buffer Overflow]]
- [[Write-What-Where]]
- [[TOCTOU]]
- [[Meltdown]]
- [[Spectre]]
