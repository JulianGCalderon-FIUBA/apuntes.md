## Definiciones

Algunas definiciones útiles

- **Amenaza**: Una potencial violación de la seguridad.
- **Ataque**: Las acciones que hacen que una amenaza se efectivice.
- **Atacante**: La persona que realiza un ataque.
- **Vulnerabilidad**: Un defecto que permite que una amenaza se efectivice a través de un ataque.
- **Riesgo**: Combinación de la probabilidad de que un ataque suceda y el daño que produciría.
- **Mitigación**: Una medida que se toma para reducir un riesgo (reducir la probabilidad de que el ataque sea efectivo o reducir el daño que puede causar).

Un programa puede representarse como una máquina de estados. Mayormente, son los que planeaba el programador, aunque no todos y no siempre. Un _exploit_ es una entrada que consigue acceder a estos otros estados y controlar la _weird machine_.

Se dice que un programa o sistema es seguro cuando:

- Realiza la tarea para la cual fue escrito.
- Y nada más.
- Aun bajo ataques.

## Marco Conceptual

Conceptualmente, la seguridad informática se divide en cuatro elementos interconectados:

- **Políticas**: La enunciación de qué está y no está permitido y a quiénes:
  - Necesidad de autenticación.
  - Complejidad de contraseñas.
  - Permiso de acceso a datos según roles en la organización.
- **Mecanismos**: Métodos, herramientas o procedimientos para hacer cumplir una política:
  - Mecanismos de autenticación.
  - Filtros de contraseñas.
  - Control de acceso basado en roles.
- **Incentivos**: El nexo entre el sistema y el mundo exterior
  - Qué queremos cuidar y por qué.
  - Por qué las organizaciones eligen un mecanismo o política por sobre otros.
- **Confiabilidad** (_Assurance_): Cuánto puede uno apoyarse en cada mecanismo.
  - Vulnerabilidades, mitigaciones, la cosa sana.
