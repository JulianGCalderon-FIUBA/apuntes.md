La disponibilidad del sistema se mide con la probabilidad de que el sistema esté disponible:

- $P = 0.9$: 36.5 días caídos por año.
- $P = 0.999$: 8.76 horas caídas por año.

Se suele medir con la cantidad de 9's.

## Cálculo de Disponibilidad

Si tenemos un solo nodo por componente, entonces la disponibilidad se calculará multiplicando la disponibilidad de cada nodo.

![[Alta Disponibilidad 1737319048.png]]

En sistemas con redundancia, debemos analizar el caso donde todas las réplicas estén caídas.

![[Alta Disponibilidad 1737319117.png]]

En sistemas con *clusters*, multiplicamos la disponibilidad de cada *cluster*.

![[Alta Disponibilidad 1737319191.png]]

## Terminología

En la industria se utilizan diversos acrónimos:

- **SLA** (*Service Level Agreement*): Es el contrato de disponibilidad pactado con el cliente. También define qué sucede si el mismo no se respeta (e.g. BigQuery SLA).
- **SLO** (*Service Level Objectives*): Es lo que se debe cumplir para no invalidar el SLA (e.g. Disponibilidad mayor a 99.95%).
- **SLI** (*Service Level Indicators*): Son las - Métricas a ser comparadas con los SLOs
	- Siempre deben ser superiores al threshold del SLO
	- Por lo general requiere una plataforma de observability
	- Analizar impacto del despliegue de los servicios
