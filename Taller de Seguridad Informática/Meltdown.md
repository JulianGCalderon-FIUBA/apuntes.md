Las instrucciones en los procesadores Core de Intel se ejecutan en varias etapas

Ante un acceso ilegal, se envía SIGSEGV y se hace rollback:

- El SIGSEGV se da al final de la ejecución de la instrucción.
- El SIGSEGV se puede atrapar y no resultar en la terminación del proceso.
- El rollback no es completo, ya que los datos traídos al caché quedan en el caché.

El sistema operativo solía mapear la memoria del kernel en el espacio del proceso

- Por motivos de performance.
- Pero solamente se podía acceder transfiriendo el control al kernel.
- La vulnerabilidad permitía a un proceso acceder al espacio de memoria del kernel.

La mitigación consistió en no mapear la memoria del kernel al espacio de memoria del proceso.

Para más información, ver [CWE-203](https://cwe.mitre.org/data/definitions/203.html) y [Meltdown: Reading Kernel Memory from User Space](https://meltdownattack.com/meltdown.pdf).
