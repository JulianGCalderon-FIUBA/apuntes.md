La virtualización surge como una necesidad de independencia real de los recursos, ofreciendo seguridad en el acceso de los recursos.

Consiste en abstraer el hardware subyacente en una plataforma, para crear un entorno en el que un servidor físico se divide en varios servidores virtuales.

## Hipervisor

Sobre la capa del hardware, se encontrará la capa de *hipervisor*. Este realiza la virtualización del hardware, permitiendo múltiples sistemas operativos en una misma computadora.

Hay distintos tipos de hipervisores, según como se ejecutan:

- **Nativo**: Es un software que se ejecuta directamente sobre el hardware físico.
- **Hosted**: Sobre el hardware físico se encuentra el sistema operativo *host*, el cual a su vez ejecuta el hipervisor.
- **Hibrido**: Sobre el hardware físico, se encuentra el sistema operativo *host*, y un hipervisor, los cuales interactúan entre sí.

## Contenedores

A diferencia de las máquinas virtuales, los contenedores se ejecutan sobre el sistema operativo *host*.

![[Virtualización de Hardware 1737292502.png]]

Un contenedor es un empaquetado de todo el código y sus dependencias, pero no contiene el sistema operativo.

El motor de contenedores se encargará de a aislar la ejecución de contenedores para que puedan ser ejecutados a la vez.

Algunos ejemplos son Docker, y Podman (open source).
