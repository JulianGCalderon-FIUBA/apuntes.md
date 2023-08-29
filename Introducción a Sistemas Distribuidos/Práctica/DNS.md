El sistema DNS es el sistema mediante el cual se traducen los nombres de dominio (google.com, fiuba.com.ar), a direcciones IP.

$$
\underbrace{\text{www}}_\text{ Subdomain }\underbrace{\text{.fiuba}}_\text{ Domain }\underbrace{\text{.com}}_\text{ Second-level domain }\underbrace{\text{.ar}}_\text{ Top-level Domain }
$$

Para resolverlo, existen servidores DNS ordenados de forma jerárquica que conocen las direcciones IP y los nombres de dominio de otros servidores conectados directamente.

Por encima de la jerarquía, están los servidores **raíz** que conocen las direcciones de los servidores TDL *(top level domain)*

El servidor autoritario es aquel que conoce la dirección de un dominio completo. Puede haber cualquier número de servidores DNS intermedios, desde el servidor raíz hasta el servidor autoritario.

Por otro lado, también existen los servidores DNS locales. Cada ISP contiene uno, que se encarga de realizar las consultas provenientes de los usuarios.

Existen dos tipos de consultas, las consultas iterativas y las consultas recursivas.

- Cuando se realiza una consulta recursiva, si el receptor no conoce la dirección asociada al nombre de dominio dado, entonces se encargará de hallar la dirección a partir de consultas iterativas sucesivas.
- Cuando se realiza una consulta iterativa, si el receptor no conoce la dirección asociada al nombre de dominio dado, devolverá una lista de servidores que conocerán la dirección buscada. Si la conoce, devolverá la dirección buscada (o una lista de ellas)

Usualmente, todas las consultas son iterativas, excepto la consulta al servidor local. Este realizará consultas sucesivas, comenzando por el servidor raíz hasta llegar al servidor autoritario. Una vez obtenida la dirección, finalmente se la devuelve al cliente que inicio la consulta.

Los servidores utilizan *DNS caching* para devolver direcciones que ya fueron consultadas frecuentemente y así acelerar el proceso de consultas DNS. Los registros en el caché tienen un tiempo de vida determinado y serán eliminados luego de este.
