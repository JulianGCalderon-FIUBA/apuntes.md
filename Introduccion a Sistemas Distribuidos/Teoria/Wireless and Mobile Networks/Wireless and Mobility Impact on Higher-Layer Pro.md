---
title: Wireless and Mobility Impact on Higher-Layer Pro
---

Si bien los protocolos de capa de transporte como TCP o UDP pueden operar en redes inalámbricas, experimentan diferencias en el rendimiento de las redes inalámbricas de las redes cableadas.

Recordemos que la ventana de congestión de TCP disminuye cuando se pierden paquetes, esto se debe a que asume que la perdida ocurre debido a la congestión de la red, y no debido a un *handoff* o corrupción de bits. Cuando ocurre esto, no hay una razón real para disminuir la ventana de congestión.

Existen tres tipos de enfoques distintos para lidiar con este problema:

- **Local recovery:** Estos protocolos se encargan de recuperar los errores de bits donde ocurren. En estos enfoques, TCP no está al tanto de que los segmentos que atraviesan los paquetes son inalámbricos.
- **TCP sender awareness of wireless links:** Otro enfoque es que TCP pueda distinguir entre estos enlaces y únicamente invocar control de congestión cuando se pierda un paquete debido a la congestión.
- **Split-connection approaches:** En estos enfoques, la conexión punto a punto entre un usuario móvil y otro punto se separa en dos conexiones de capa de transporte. Una desde el móvil hasta el *wireless access point*, y otra desde allí al otro *end point*.

Por otro lado, consideremos la movilidad desde la capa de aplicación. Aquellas aplicaciones que operan sobre enlaces inalámbricos deben tratar el ancho de banda como un recurso escaso. Aunque la movilidad ofrece desafíos, ofrece la posibilidad de aplicaciones dependientes de la localización del contexto, como aplicaciones de navegabilidad.
