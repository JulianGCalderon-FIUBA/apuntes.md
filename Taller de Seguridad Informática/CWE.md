---
aliases:
  - Common Weakness Enumeration
---

No son vulnerabilidades concretas, sino una taxonomía de fallos.

Está organizada en 4 tipos de entidades:

- **Pilar**: El tipo más abstracto y general de una debilidad.
  - Es independiente de la tecnología.
- **Clase**: Agrupación de debilidades dentro de un pilar, por alguna característica en común.
  - Casi siempre es dependiente de la tecnología.
- **Base**:
  - Bastante específico de la tecnología
  - Hay suficiente detalle como para tener métodos específicos de detección.
- **Variante**:
  - Específico de una tecnología.

Por ejemplo, la vulnerabilidad _Out-of-bounds write_ es una clase: [CWE-787](https://cwe.mitre.org/data/definitions/787.html).
