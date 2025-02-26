La computación Cloud es una metáfora para internet y todo el contenido (y servicios) que ofrece. No es una tecnología nueva en sí, sino una nueva forma de ofrecer recursos.

## Niveles de Abstracción

Hay distintos niveles de abstracción, según que servicios se consumen:

- **IaaS** (Infrastructure as a Service): Ofrece almacenamiento y virtualización de equipos. Permite definir redes y técnicas de adaptación para capacidad frente a cargas.
- **PaaS** (Platform as a Service): Son frameworks para desplegar código, sin importar donde se despliega. Se ofrecen servicios para el desarrollo (logs, monitoreo, etc.).
- **SaaS** (Software as a Service): Ofrecen servicios, pero sin conocer el código que está detrás. Tiene soluciones muy genéricas y configurables. Los protocolos y la arquitectura están pensadas para la integración.

![[Cloud 1737418461.png]]

Cuanto más arriba estemos en la pirámide de abstracción, menos control tenemos del sistema:

![[Cloud 1737418864.png]]

En el siguiente diagrama, se ven servicios del ecosistema Google en diferentes lugares de la piramide de abstracción:

![[Computación Cloud 1737428530.png]]

## Platform as a Service (PaaS)

Es un sistema que ofrece una plataforma para desarrollar, esto incluye:

- **Infraestructura**: Permite desplegar fácilmente, sin tener que preocuparnos por el hardware.
- **Plataforma de desarrollo**: Se ofrecen sistemas operativos definidos, bibliotecas y todas las dependencias necesarias para desarrollar una aplicación.
- **Persistencia**: Se ofrecen distintos mecanismos de persistencia, aunque la variedad generalmente es limitada.
- **Monitoreo**: Hay monitoreo automático de las aplicaciones de distinto tipo.
- **Escalabilidad**: Facilita la escalabilidad del sistema, con balanceo de carga y sistemas elásticos.

![[Computación Cloud 1737420468.png]]

Si bien estas cosas nos facilitan el desarrollo, también nos sacan el control. Perdemos control sobre, por ejemplo, el sistema operativo utilizado.

## Beneficios de Cloud

Algunos de los principales beneficios de Cloud, son:

- **Accesibilidad**: Los componentes pueden ser accedidos desde todos lados. Hay movilidad y visibilidad constante de los recursos.
- **Time-to-Market**: Los recursos están disponibles de forma instantánea.
- **Escalabilidad:** Hay capacidades "ilimitadas" para alquilar recursos: almacenamiento, ancho de banda, cómputo, memoria, etc., siempre y cuando tenga la plata suficiente.
- **Costos:** El pago es a demanda (*pay as you go*), por lo que puedo controlar el gasto según el uso. La accesibilidad, escalabilidad, y confiabilidad es mucho más barata que antes.

## Nubes Privadas

La necesidad de utilizar nubes privadas dependerá del contexto. En una nube pública:

- Los servidores compartidos con otros usuarios. En situaciones extremas, las plataformas de nube se priorizan a sí mismas.
- La disponibilidad de los recursos están garantizados con SLA.
- Los costos son variables (*pay as you go*)
- Se accede mediante internet

Por otro lado, en una nube privada:

- Los *datacenters* son propios de la empresa
- Los recursos son dedicados, permitiendo controlarlos de forma completa.
- Tiene costos fijos de mantenimiento y expansión. En algunas situaciones es mejor que el costo variable.
- Se accede mediante intranet.

## Adopción de la Nube

Hay factores políticos que causan la resistencia a la nube:

- Licenciamiento, jurisdicción y perdida de gobernabilidad sobre los datos. No podemos controlar por donde pasan los datos, y a veces esto es importante, en especial para los gobiernos.
- Incapacidad de influir sobre la toma de decisiones que afecta al hardware. Hay situaciones donde no elijo el sistema operativo, o los lenguajes.

Por otro lado, también existen factores técnicos:

- Hay sistemas obsoletos que son muy costosos de migrar a la nube.
- Los datos sensibles quedarán expuestos, si los sistemas de seguridad no están adaptados para esto.
- Al ser una arquitectura y tecnología nueva, se genera una resistencia al cambio.
