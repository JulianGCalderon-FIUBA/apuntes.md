La tolerancia a fallos estudia las necesidades de los sistemas confiables (*dependable systems*):

- Busca garantizar que se ejecuten y comporten de acuerdo a lo esperado por el usuario en distintas condiciones.
- Busca prevenir la aparición de fallas de cara al usuario, tanto normales como excepcionales.
- Hay distintas alternativas para prevenir o tolerar cada situación.

La idea es que el sistema nunca salga de estados definidos. Todo escenario debe estar contemplado, y debe haber una forma para volver al flujo habitual.

Se permite definir la inversión y el nivel de tolerancia para cada tipo de sistema.

Algunas herramientas para lograr esto son:

- Recuperación.
- Redundancia (ej. replicación).
- Consenso (ej. esquema de votación)

> En presencia de fallos, el sistema distribuidos continúa operando de forma aceptable

## Condiciones de Trabajo

Para definir el nivel de tolerancia a fallos de un sistema, es necesario indicar en que condiciones opera el sistema.

Las condiciones se pueden separar en dos tipos:

- **Condiciones del entorno**:
	- Entorno físico del hardware, como temperatura, polvo, etc.
	- Interferencia y ruido.
	- *Drift* del reloj.
- **Condiciones operacionales**:
	- Especificaciones, valores límite y tiempos de respuesta.
	- Ancho de banda, latencia
	- Protocolos soportado

## Estrategias de Manejo de Fallos

Hay distintas estrategias para manejar los fallos:

- **Fault removal**: Eliminar los errores antes de que sucedan. Por ejemplo: estrategias de *code correction* para evitar cambios de bits.
- **Fault prevention:** Evitar las condiciones que llevan a los errores. Por ejemplo: con componentes que impidan que haya fallos (relojes atómicos, componentes de grado militar).
- **Fault forecasting:** Determinar la probabilidad de que un componente pueda fallar, y reemplazarlo. Por ejemplo: reemplazar componentes cada cierta cantidad de horas de uso.
- **Fault tolerance:** Procesas los errores del sistema, en lugar de evitar que sucedan. Es la estrategia más común en software.
