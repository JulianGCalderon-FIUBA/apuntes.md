El objetivo de escalabilidad es el crecimiento,

- **Respecto del tamaño**: Agregando usuarios o recursos a controlar.
- **Respecto de la distribución geográfica**: Permitiendo dispersión, y acceder a usuarios en lugares lejanos.
- **Respecto de los objetivos administrativos del sistema**: Nuevas sintaxis, semánticas y servicios ofrecidos.

Para escalar un servicio, podemos usar **plataformas** para alta concurrencia. Estas plataformas aplican patrones ya conocidos y probados, y ofrecen escalamiento automático (con cierto límite). Están fuertemente vinculadas con una infraestructura o producto, y no será tan simple migrarlo a otra plataforma.

Otra opción es utilizar arquitecturas ad hoc y **personalizadas**, aunque necesitan de configuración y soporte adicional, y el escalamiento es manual (o automatizado por humanos). Al ser una solución manual, tenemos la posibilidad de migraciones a distintas plataformas.

## Patrones de Carga

A partir de como evoluciona la carga en el sistema según el tiempo, se definen distintos patrones de carga:

- **Predictable Burst**: Se conoce que en cierto determinado momento, la carga en el sistema aumenta. Por ejemplo: Navidad.
- Unpredictable Burst:
- Per

![[Escalabilidad 1737314465.png]]

## Técnicas

- **Escalamiento vertical**:
	- Agregar recursos a un nodo
- **Escalamiento horizontal**:
	- Redundancia
	- Balanceadores de carga
	- Proximidad geográfica
- **Fragmentación de datos**:
	- Fraccionar para optimizar.
	- Mantener juntos datos "cercanos"
- **Componentización**:
	- Separar servicios
- **Optimizar algoritmos**:
	- Performance
	- Mensajería
- **Asincronismo**:
	- Mantener sincrónico sólo lo estrictamente necesario
	- Limitado por el negocio
