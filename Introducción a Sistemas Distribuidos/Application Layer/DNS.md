Para identificar un ***host*** en la red, utilizamos ***IP addresses***. Estas tienen una estructura jerárquica y consisten en cuatro secciones de separadas por puntos, cada una conteniendo un número de 4 bits. Estas direcciones se escanean de izquierda a derecha, obteniendo información acerca del host.

## 1. Services Provided by DNS

Necesitamos un servicio que permita traducir ***hostnames*** en direcciones IP. El sistema ***DNS*** es una base de datos distribuida implementada con una jerarquía de servidores, con una protocolo de capa de aplicación que permite a los ***hosts*** consultar a la base de datos.

Este sistema ***DNS*** provee algunos servicios importantes:

- ***Host aliasing:*** Un ***host*** con un ***hostname*** complicado puede tener uno o múltiples ***aliases.*** Al ***hostname*** original se lo denomina ***canónico.***
- ***Mail server aliasing:*** Similar al anterior, permite tener múltiples aliases para un único servidor de mails.
- ***Load distribution:*** Se puede utilizar este sistema para redirigir a los usuarios a los servidores a otros servidores, a partir de un ***hostname*** común. Para hacer esto, el ***DNS*** devuelve todas las direcciones **IP** asociadas al ***hostname***, pero rotando el orden cada vez.

## 2. Overview of How Dns Works

### A Distributed, Hierarchical Database

El sistema ***DNS*** utiliza un gran número de servidores organizados de forma jerárquica y distribuidos a lo largo del mundo. Se pueden separar en tres clases:

- **Root:** Es una base de datos distribuida, todos estos ***servidores*** comparten la misma información y están gestionados por 13 organizaciones distintas.
- ***Top-Level Domain (TLD):*** Por cada top-level domain, tendremos un servidor (o multiples). Son los que están al final de la *url.* Ej: ***.com.ar***.
- ***Authoritative:*** Cada organización con ***hosts*** públicos tiene que proveer registros públicos para conectar sus ***hostnames*** con la dirección IP. Entre ellos, tendremos.edu.uba. Estos pueden estar anidados, como por ejemplo ***"fi.uba.ar"***.
- ***Local:*** Los servidores locales DNS no pertenecen estrictamente a la jerarquía, pero son centrales en la arquitectura. Cada ***ISP*** tiene uno. Cuando un ***host*** hace una consulta ***DNS***, esta se le envía a su ***DNS local*** el cual se encarga de hacer la consulta.

Las consultas pueden ser tanto recursivas como iterativas. Por lo general, el *DNS local utiliza consultas recursivas,* mientras todo el resto utilizan consultas iterativas.

Las consultas *recursivas* se encargan de la consulta, devolviendo la **IP** buscada, mientras que las consultas ***iterativas*** únicamente devuelven el siguiente en la cadena de *DNS look-up*

### DNS Caching

Es una característica importante del sistema ***DNS***. Cuando un servidor recibe una respuesta ***DNS***, entonces puede guardarla en su memoria local. Cuando otro cliente le pregunta por ese mismo ***hostname***, puede devolver el valor guardado. Estos valores son descartados después de un tiempo.

Además, permiten que las consultas no atraviesen los servidores ***root***, almacenando las direcciones de los *TLD servers.*

## 3. DNS Records and Messages

Los servidores ***DNS*** almacenan ***resource records (RR)***. Estos tienen la siguiente estructura.

$$
\text{(Name, Value, Type, TTL)}
$$

***TTL*** representa el tiempo de vida del recurso, cuando debería ser removido del cache. El significado de ***name*** y ***value*** dependerán de ***type***

- ***Type A:*** Entonces, ***name*** es el hostname ***y*** value ***es la dirección IP.***
- Type NS***:*** Entonces*, name* es el dominio, y *value* es el ***hostname*** de los servidores que sabe encontrar la *dirección IP* buscada.
- ***Type CNAME: Entonces, value*** es el ***hostname*** canónico para el *host* con alias ***name***.
- *Type MX:* Entonces ***value***s el nombre canónico para el ***mail server*** con *alias name.*

### DNS Messages

Tanto las ***DNS queries*** como los ***replies*** tienen el mismo formato. Los primeros 12 ***bytes*** son la ***header section***. Estos contienen un identificador de la query, los ***flags*** de la misma, y contadores de ocurrencias de los tipos de datos que le siguen al ***header***.

Luego del ***header tendremos question section***, la cual tiene información sobre la consulta realizada. Después, la **answer section** contiene los **RR** de la consulta.

En la ***authority*** section estarán los **RR** de otros ***authoritative servers.*** en *additional section se encuentran RR ú*tiles.

## Inserting Records into the DNS Database

Un ***registrar*** es una entidad comercial que verifica la unicidad de un dominio, e ingresa el dominio en la base de datos.

Cuando registramos un nombre, debemos proveer los nombres y las direcciones de su primario y secundario ***authoritative server***.

El ***registrar se encargará de que los*** registros ***proporcionados*** se ingresen en los servidores del dominio.
