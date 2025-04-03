Es una abreviación de _Time of Check_ vs. _Time of Use_.

Un programa realiza una acción potencialmente riesgosa, por ejemplo, instalar un paquete de software. Antes de realizar la acción, verifica los datos, por ejemplo, la firma digital en el archivo de instalación. Pero no protege el recurso una vez verificado, en este caso el archivo de instalación, contra modificaciones, y hay una ventana de tiempo en que se puede modificar antes de la instalación.

Un ejemplo es Pulse Secure Client Privilege Escalation [CVE-2020-13162](https://nvd.nist.gov/vuln/detail/CVE-2020-13162)

Una posible mitigación es, antes de verificar el recurso a controlar, se protege el recurso de alguna manera (semáforos, hacer una copia).

Para más información, ver [CWE-367](https://cwe.mitre.org/data/definitions/367.html).
