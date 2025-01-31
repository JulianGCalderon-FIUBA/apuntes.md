La tolerancia a fallos estudia las necesidades de los sistemas confiables (*dependable systems*):

- Busca garantizar que se ejecuten y comporten de acuerdo a lo esperado por el usuario en distintas condiciones.
- Busca prevenir la aparición de fallas de cara al usuario, tanto normales como excepcionales. La idea es que el sistema nunca salga de estados definidos.
- Hay distintas alternativas para prevenir o tolerar cada situación.

Se permite definir la inversión y el nivel de tolerancia para cada tipo de sistema.

Algunas herramientas para lograr esto son:

- Recuperación.
- Redundancia (ej. replicación).
- Consenso (ej. esquema de votación)

## Generación de Fallos

Un fallo o *fault* causa la ocurrencia de un estado de error en el sistema. Esto eventualmente desencadena en un comportamiento incorrecto: falla o averia (*failure*).
